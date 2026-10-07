"""
LexAI Practice Area (AoP) Classifier
Classifies legal queries, petitions, and client briefs into top law firm practice areas.
"""

from typing import List, Dict

PRACTICE_AREAS = {
    "AoP-1: Corporate Law & M&A": ["companies act", "nclt", "nclat", "mca", "merger", "acquisition", "oppression", "mismanagement", "shareholder", "board resolution", "section 241", "rights issue"],
    "AoP-2: Banking, Finance & Insolvency": ["ibc", "cirp", "insolvency", "bankruptcy", "ibbi", "rbi", "drt", "drat", "sarfaesi", "financial creditor", "operational creditor", "resolution plan"],
    "AoP-3: Competition & Antitrust": ["cci", "competition act", "abuse of dominance", "cartel", "anti-competitive", "compat", "combination", "relevant market"],
    "AoP-4: Securities & Capital Markets": ["sebi", "sat", "insider trading", "lodr", "takeover code", "pfutp", "ipo", "listing regulations"],
    "AoP-5: White-Collar Crime & Enforcement": ["ed", "enforcement directorate", "pmla", "sfio", "cbi", "money laundering", "bribe", "bns", "ipc", "bail"],
    "AoP-6: Taxation & Revenue": ["itat", "cestat", "gst", "income tax", "customs", "tax audit", "transfer pricing", "assessment order"],
    "AoP-7: Commercial Arbitration & Dispute Resolution": ["arbitration", "section 11", "section 34", "diac", "mcia", "uncitral", "interim relief", "section 9", "commercial court"],
    "AoP-8: Constitutional & Administrative Litigation": ["writ petition", "article 32", "article 226", "supreme court", "high court", "fundamental rights", "habeas corpus", "mandamus"]
}

class PracticeAreaClassifier:
    @classmethod
    def classify(cls, text: str) -> List[Dict[str, float]]:
        """Classifies text into relevant practice areas with confidence scores."""
        text_lower = text.lower()
        scores = {}

        for aop, keywords in PRACTICE_AREAS.items():
            matches = sum(1 for kw in keywords if kw in text_lower)
            if matches > 0:
                scores[aop] = round(matches / len(keywords), 3)

        sorted_aops = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        if not sorted_aops:
            return [{"aop": "AoP-8: Constitutional & Administrative Litigation", "score": 1.0}]
        
        return [{"aop": k, "score": v} for k, v in sorted_aops]
