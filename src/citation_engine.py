"""
LexAI Citation Engine
Supports Indian Legal Citation Standards:
- SCC: (YYYY) Vol SCC Page
- INSC: YYYY INSC Number (Supreme Court Neutral Citation)
- AIR: AIR YYYY SC Page
- SCR: [YYYY] Vol SCR Page
- Academic: SILC, ILI, Bluebook, OSCOLA
"""

import re
from typing import Dict, Any, Optional

class CitationEngine:
    # Regex patterns for Indian Legal Citations
    SCC_PATTERN = r'\((?P<year>\d{4})\)\s+(?P<vol>\d+)\s+SCC\s+(?P<page>\d+)'
    INSC_PATTERN = r'(?P<year>\d{4})\s+INSC\s+(?P<num>\d+)'
    AIR_PATTERN = r'AIR\s+(?P<year>\d{4})\s+(?P<court>SC|Bom|Del|Cal|Mad)\s+(?P<page>\d+)'
    SCR_PATTERN = r'\[(?P<year>\d{4})\]\s+(?P<vol>\d+)\s+SCR\s+(?P<page>\d+)'

    @classmethod
    def parse_citation(cls, citation_str: str) -> Dict[str, Any]:
        """Parses legal citation and returns normalized canonical format."""
        citation_str = citation_str.strip()

        # Check INSC neutral citation
        match = re.search(cls.INSC_PATTERN, citation_str, re.IGNORECASE)
        if match:
            d = match.groupdict()
            return {
                "type": "INSC Neutral Citation",
                "canonical": f"{d['year']} INSC {d['num']}",
                "year": int(d['year']),
                "identifier": d['num']
            }

        # Check SCC
        match = re.search(cls.SCC_PATTERN, citation_str, re.IGNORECASE)
        if match:
            d = match.groupdict()
            return {
                "type": "Supreme Court Cases (SCC)",
                "canonical": f"({d['year']}) {d['vol']} SCC {d['page']}",
                "year": int(d['year']),
                "volume": int(d['vol']),
                "page": int(d['page'])
            }

        # Check AIR
        match = re.search(cls.AIR_PATTERN, citation_str, re.IGNORECASE)
        if match:
            d = match.groupdict()
            return {
                "type": "All India Reporter (AIR)",
                "canonical": f"AIR {d['year']} {d['court'].upper()} {d['page']}",
                "year": int(d['year']),
                "court": d['court'].upper(),
                "page": int(d['page'])
            }

        # Check SCR
        match = re.search(cls.SCR_PATTERN, citation_str, re.IGNORECASE)
        if match:
            d = match.groupdict()
            return {
                "type": "Supreme Court Reports (SCR)",
                "canonical": f"[{d['year']}] {d['vol']} SCR {d['page']}",
                "year": int(d['year']),
                "volume": int(d['vol']),
                "page": int(d['page'])
            }

        return {"type": "Unrecognized / Custom Citation", "canonical": citation_str}

    @classmethod
    def format_to_style(cls, parsed: Dict[str, Any], style: str = "SCC") -> str:
        """Formats a parsed citation into specified style standard (SCC, SILC, Bluebook, OSCOLA)."""
        if parsed.get("type") == "INSC Neutral Citation":
            return parsed["canonical"]

        year = parsed.get("year", "2024")
        vol = parsed.get("volume", 1)
        page = parsed.get("page", 1)

        if style.upper() == "SILC":
            return f"({year}) {vol} SCC {page} (India)"
        elif style.upper() == "BLUEBOOK":
            return f"({year}) {vol} S.C.C. {page}"
        elif style.upper() == "OSCOLA":
            return f"[{year}] {vol} SCC {page}"
        else: # Default SCC
            return f"({year}) {vol} SCC {page}"
