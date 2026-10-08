"""
LexAI Phase 1 Ingestion Pipeline Runner
Runs Court Scraper -> Extracts with PyMuPDF -> Normalizes Citations & Metadata.
"""

import os
import sys
import json

# Add project root to sys.path
sys.path.insert(0, r"D:\lexai")

from src.scrapers.court_scraper import CourtJudgmentScraper
from src.processors.judgment_processor import JudgmentProcessor
from src.citation_engine import CitationEngine
from src.aop_classifier import PracticeAreaClassifier
from src.proposition_extractor import PropositionExtractor

def run_phase1_pipeline():
    print("="*70)
    print("  LEXAI PHASE 1: DATA INGESTION & LEGAL TEXT EXTRACTION PIPELINE")
    print("="*70)

    # 1. Initialize scraper
    scraper = CourtJudgmentScraper()
    print("\n[Step 1] Acquiring Court Judgment PDF...")
    pdf_path = scraper.fetch_mock_sc_judgment(citation="2024 INSC 835")
    print(f"  -> Acquired PDF: {pdf_path}")

    # 2. Extract with PyMuPDF
    print("\n[Step 2] Processing PDF with PyMuPDF (fitz) text extractor...")
    extracted_data = JudgmentProcessor.extract_text_from_pdf(pdf_path)
    print(f"  -> Total Pages Extracted: {extracted_data['total_pages']}")
    print(f"  -> Total Characters: {extracted_data['char_count']}")
    print(f"  -> Detected Metadata:")
    for k, v in extracted_data['metadata'].items():
        print(f"     - {k.replace('_', ' ').title()}: {v}")

    # 3. Citation normalization
    print("\n[Step 3] Running Citation Engine Normalization...")
    scc_cite = extracted_data['metadata'].get('scc_citation') or "(2024) 4 SCC 120"
    parsed_scc = CitationEngine.parse_citation(scc_cite)
    print(f"  -> Input Citation: {scc_cite}")
    print(f"  -> Standard Indian Legal Citation (SILC): {CitationEngine.format_to_style(parsed_scc, 'SILC')}")
    print(f"  -> Bluebook (21st ed): {CitationEngine.format_to_style(parsed_scc, 'BLUEBOOK')}")
    print(f"  -> OSCOLA (4th ed): {CitationEngine.format_to_style(parsed_scc, 'OSCOLA')}")

    # 4. Classify Practice Area (AoP)
    print("\n[Step 4] Classifying Practice Area (AoP)...")
    aops = PracticeAreaClassifier.classify(extracted_data['text'])
    print(f"  -> Primary Area of Practice: {aops[0]['aop']} (Confidence: {aops[0]['score']*100:.1f}%)")

    # 5. Extract Single-Line Ratio Decidendi
    print("\n[Step 5] Distilling Single-Line Proposition of Law (Senior Advocate Mode)...")
    prop = PropositionExtractor.extract_proposition(extracted_data['text'])
    print(f"  -> Distilled Proposition: \"{prop['single_line_proposition']}\"")

    # 6. Save Processed Artifact
    out_json_path = os.path.join(r"D:\lexai\data\judgments\processed", "judgment_2024_INSC_835.json")
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=2)
    print(f"\n[Step 6] Saved Structured Judgment JSON to: {out_json_path}")
    print("\n" + "="*70)
    print("  PHASE 1 INGESTION & EXTRACTION PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*70)

if __name__ == "__main__":
    run_phase1_pipeline()
