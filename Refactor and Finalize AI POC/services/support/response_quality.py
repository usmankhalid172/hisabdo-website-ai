"""
Response quality checks for the HisabDo AI POC.
"""

import re
from typing import Dict


def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def extract_words(text: str):
    return set(re.findall(r"\b[a-zA-Z0-9]+\b", normalize_text(text)))


def relevance_score(query: str, answer: str) -> float:
    """
    Lightweight lexical relevance score.

    This is a deterministic POC metric, not an ML confidence score.
    """
    query_words = extract_words(query)
    answer_words = extract_words(answer)

    if not query_words or not answer_words:
        return 0.0

    overlap = query_words.intersection(answer_words)

    return round(len(overlap) / len(query_words), 2)


def is_clear(answer: str) -> bool:
    if not answer or not answer.strip():
        return False

    if len(answer.strip()) < 10:
        return False

    return True


def has_unnecessary_generic_intro(answer: str) -> bool:
    generic_phrases = [
        "as an ai",
        "i am an ai",
        "i'm an ai",
        "certainly",
        "of course",
        "i would be happy to",
    ]

    text = normalize_text(answer)

    return any(phrase in text for phrase in generic_phrases)


def evaluate_response(
    query: str,
    answer: str,
    verified: bool,
    confidence: float,
) -> Dict:

    score = relevance_score(query, answer)

    checks = {
        "verified": verified,
        "clear": is_clear(answer),
        "relevant": score >= 0.20,
        "confidence_ok": confidence >= 0.65,
        "generic_content_check": not has_unnecessary_generic_intro(answer),
    }

    passed = all(checks.values())

    return {
        "passed": passed,
        "relevance_score": score,
        "checks": checks,
    }


def improve_response(result: Dict, query: str) -> Dict:
    """
    Run a search_faq() result through the quality checks and decide
    whether it's good enough to return to the user as-is.

    - On pass: the result is returned unchanged, plus a "quality_check"
      field so callers/tests can see why it passed.
    - On fail: result["found"] is set to False so app.py's existing
      "QUALITY FAILURE" branch (step 11 in faq_help()) takes over and
      swaps in a safe fallback message instead of a weak answer.

    This does not mutate "verified" or "answer" itself - app.py is
    responsible for what happens once "found" is False.
    """

    answer = result.get("answer", "")
    verified = result.get("verified", False)
    confidence = result.get("confidence", 0)

    evaluation = evaluate_response(
        query,
        answer,
        verified,
        confidence,
    )

    result["quality_check"] = evaluation

    if not evaluation["passed"]:
        result["found"] = False

    return result