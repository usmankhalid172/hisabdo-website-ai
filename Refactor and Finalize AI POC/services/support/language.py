"""
English / Urdu / Roman Urdu detection for the HisabDo POC.
"""

import re


URDU_RANGE = re.compile(r"[\u0600-\u06FF]")


ROMAN_URDU_WORDS = {
    "kya",
    "hai",
    "he",
    "kaise",
    "kese",
    "karun",
    "karna",
    "ka",
    "ki",
    "ke",
    "mein",
    "mujhe",
    "aap",
    "ap",
    "yeh",
    "ye",
    "mera",
    "meri",
    "account",
    "customer",
    "khata",
    "expense",
    "backup",
}


def detect_language(text: str) -> str:
    if not text or not text.strip():
        return "english"

    if URDU_RANGE.search(text):
        return "urdu"

    words = set(text.lower().split())

    roman_matches = len(words.intersection(ROMAN_URDU_WORDS))

    if roman_matches >= 1:
        return "roman_urdu"

    return "english"