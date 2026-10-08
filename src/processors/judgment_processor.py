"""
LexAI PDF Ingestion & Text Processing Pipeline
Extracts clean legal text, metadata (Coram, Bench, Dates, CNR), and strips artifacts.
"""

import os
import re
import json
from typing import Dict, Any, Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

class JudgmentProcessor:
    @classmethod
    def extract_text_from_pdf(cls, pdf_path: str) -> Dict[str, Any]:
        """
        Extracts clean text and structural layout from a judgment PDF using PyMuPDF.
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        if fitz is None:
            raise ImportError("PyMuPDF (fitz) is not installed. Please install via: pip install pymupdf")

        doc = fitz.open(pdf_path)
        num_pages = len(doc)
        full_text = []
        page_chunks = []

        for page_idx in range(num_pages):
            page = doc[page_idx]
            raw_text = page.get_text("text")
            cleaned_page = cls._clean_page_artifacts(raw_text)
            full_text.append(cleaned_page)
            page_chunks.append({
                "page_number": page_idx + 1,
                "text": cleaned_page,
                "char_count": len(cleaned_page)
            })

        combined_text = "\n\n".join(full_text)
        metadata = cls._extract_legal_metadata(combined_text)

        return {
            "source_file": os.path.basename(pdf_path),
            "total_pages": num_pages,
            "char_count": len(combined_text),
            "metadata": metadata,
            "text": combined_text,
            "pages": page_chunks
        }

    @staticmethod
    def _clean_page_artifacts(text: str) -> str:
        """
        Strips repetitive headers, page numbers, and reporter watermarks.
        """
        # Remove typical Indian court page headers/footers
        text = re.sub(r'(?i)Page\s+\d+\s+of\s+\d+', '', text)
        text = re.sub(r'(?i)SCC\s+Online\s+Web\s+Edition.*', '', text)
        text = re.sub(r'©\s*Eastern\s*Book\s*Company.*', '', text)
        # Normalize multiple blank lines
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    @classmethod
    def _extract_legal_metadata(cls, text: str) -> Dict[str, Any]:
        """
        Extracts high-confidence regex metadata from the judgment opening lines.
        """
        metadata = {
            "neutral_citation": None,
            "scc_citation": None,
            "coram": [],
            "date_of_judgment": None,
            "case_number": None,
            "cnr_number": None
        }

        # 1. Neutral Citation (e.g. 2024 INSC 835)
        insc_match = re.search(r'(\b\d{4}\s+INSC\s+\d+\b)', text, re.IGNORECASE)
        if insc_match:
            metadata["neutral_citation"] = insc_match.group(1).upper()

        # 2. SCC Citation (e.g. (2024) 4 SCC 120)
        scc_match = re.search(r'\(\d{4}\)\s+\d+\s+SCC\s+\d+', text, re.IGNORECASE)
        if scc_match:
            metadata["scc_citation"] = scc_match.group(0)

        # 3. CNR Number (e.g. SCIN010023412024)
        cnr_match = re.search(r'\b[A-Z]{4}\d{12}\b', text)
        if cnr_match:
            metadata["cnr_number"] = cnr_match.group(0)

        # 4. Date of Judgment
        date_match = re.search(r'(?i)(?:dated|decided\s+on|date\s*:\s*)\s*([0-9]{1,2}(?:st|nd|rd|th)?[\s\/\-\.][A-Za-z0-9]+[\s\/\-\.][0-9]{4})', text)
        if date_match:
            metadata["date_of_judgment"] = date_match.group(1).strip()

        # 5. Coram / Bench Names (Hon'ble Justice ...)
        coram_matches = re.findall(r'(?i)(?:HON\'?BLE\s+(?:MR\.|MS\.|DR\.)?\s*JUSTICE\s+[A-Z\.\s]+(?:\,\s*C\.?J\.?I\.?)?)', text)
        if coram_matches:
            # Deduplicate bench names
            unique_judges = list(dict.fromkeys([j.strip() for j in coram_matches[:4]]))
            metadata["coram"] = unique_judges

        return metadata
