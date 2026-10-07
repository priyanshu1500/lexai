"""
LexAI Boolean Search Builder (Lawyer's Perspective)
Generates advanced legal Boolean search expressions for court portals and databases.
"""

from typing import List, Dict, Any

class BooleanSearchBuilder:
    @classmethod
    def build_query(cls, proposition: str, practice_area: str) -> Dict[str, Any]:
        """Formulates optimized Boolean query strings with proximity and section operators."""
        words = [w.strip(".,()") for w in proposition.split() if len(w) > 3]
        
        # Extract key legal terms
        key_terms = [w for w in words if w.lower() not in {"whether", "under", "constitutes", "without", "described", "facts"}]
        
        boolean_query = " AND ".join([f'"{term}"' for term in key_terms[:4]])
        
        if "Companies Act" in proposition or "Section 241" in proposition:
            boolean_query = '("Companies Act" OR "Section 241" OR "Section 242") AND ("oppression" NEAR/5 "mismanagement") AND "dilution"'
        elif "IBC" in proposition or "Section 7" in proposition:
            boolean_query = '("Insolvency and Bankruptcy Code" OR "IBC") AND "Section 7" AND ("pre-existing dispute" OR "default")'
        elif "PMLA" in proposition or "Section 5" in proposition:
            boolean_query = '("PMLA" OR "Money Laundering") AND "Section 5" AND "provisional attachment" AND "scheduled offence"'

        return {
            "proposition": proposition,
            "practice_area": practice_area,
            "boolean_search_string": boolean_query,
            "google_advanced_query": boolean_query.replace("NEAR/5", ""),
            "e_courts_keywords": [kt for kt in key_terms[:5]]
        }
