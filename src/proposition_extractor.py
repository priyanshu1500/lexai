"""
LexAI Single-Line Proposition Extractor (Senior Advocate Mode)
Distills verbose client prompts into a single, sharp legal proposition of law.
"""

import re
from typing import Dict, Any

class PropositionExtractor:
    @classmethod
    def extract_proposition(cls, verbose_prompt: str) -> Dict[str, Any]:
        """Converts lengthy factual prompts into a single-line proposition of law."""
        prompt_clean = verbose_prompt.strip()

        # Simulated prompt distillation logic (in production connects to LLM prompt distillation pipeline)
        # Identifies issue framing pattern: "Whether [Action/Fact] under [Statute/Rule] constitutes [Legal Offense/Right]"
        
        proposition = f"Whether the facts and transactions described give rise to a maintainable claim or statutory breach under the applicable Indian legal framework."
        
        if "minority" in prompt_clean.lower() or "shareholder" in prompt_clean.lower() or "dilut" in prompt_clean.lower():
            proposition = "Whether the issuance of rights shares resulting in equity dilution of a minority shareholder without mandatory notice constitutes oppression and mismanagement under Section 241/242 of the Companies Act, 2013."
        elif "insolvency" in prompt_clean.lower() or "default" in prompt_clean.lower() or "cirp" in prompt_clean.lower():
            proposition = "Whether initiation of Corporate Insolvency Resolution Process (CIRP) under Section 7 of IBC is maintainable in the existence of a pre-existing dispute prior to Section 8 notice."
        elif "pmla" in prompt_clean.lower() or "ed" in prompt_clean.lower() or "attachment" in prompt_clean.lower():
            proposition = "Whether provisional attachment of property under Section 5 of PMLA is sustainable without a scheduled offence registered by the predicate investigating agency."
        elif "arbitration" in prompt_clean.lower() or "section 11" in prompt_clean.lower() or "stamp" in prompt_clean.lower():
            proposition = "Whether an unstamped or inadequately stamped arbitration agreement is enforceable at the referral stage under Section 11(6) of the Arbitration & Conciliation Act, 1996."

        return {
            "original_length_chars": len(verbose_prompt),
            "single_line_proposition": proposition,
            "framing_style": "Senior Advocate Ratio Decidendi Standard"
        }
