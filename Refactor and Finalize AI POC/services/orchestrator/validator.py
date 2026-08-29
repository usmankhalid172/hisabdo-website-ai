"""
Response validation for the HisabDo AI POC.
"""

import re
from typing import Dict


FINANCIAL_TERMS = [
    "profit",
    "revenue",
    "income",
    "expense",
    "balance",
    "amount",
    "sales",
    "loss",
    "rupees",
    "rs",
    "pkr",
    "usd",
    "inr",
]


def contains_financial_request(query: str) -> bool:
    text = query.lower()
    return any(term in text for term in FINANCIAL_TERMS)


def contains_numeric_claim(answer: str) -> bool:
    """
    Detect simple numerical claims.
    """
    return bool(re.search(r"\b\d+(?:\.\d+)?\b", answer))


def validate_response(
    query: str,
    answer: str,
    verified: bool = False,
) -> Dict:

    if not answer or not answer.strip():
        return {
            "valid": False,
            "reason": "empty_response",
        }

    if not verified:
        return {
            "valid": False,
            "reason": "unverified_content",
        }

    if contains_financial_request(query):
        if contains_numeric_claim(answer):
            return {
                "valid": False,
                "reason": "financial_number_requires_verified_data",
            }

    return {
        "valid": True,
        "reason": "validated",
    }