"""
Intent detection for the HisabDo AI POC.

Two-stage, deterministic classification (no ML model):

  Stage 1 - chitchat / escalation pre-filter (regex)
            catches greetings, thanks, and human-escalation requests
            before they're treated as product questions.

  Stage 2 - topic categorization (keyword scoring)
            only runs if stage 1 found nothing - classifies the
            query as product_info / feature / how_to / faq / support.

This replaces the old separate intent.py + intent_router.py, which
both defined a detect_intent(query) function with different return
types. There is now a single detect_intent(query) -> (intent, confidence).
"""

import re
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Stage 1: chitchat / escalation pre-filter
# ---------------------------------------------------------------------------

GREETING_PATTERNS = [r"^\s*(hi|hello|hey|salam|assalam|asalam)\b"]
THANKS_PATTERNS = [r"\b(thanks|thank you|shukriya|shukria)\b"]
ESCALATION_PATTERNS = [
    r"\b(human|agent|representative|talk to (a )?(person|someone)|real person)\b",
    r"\b(complain|complaint|frustrated|angry|not working at all)\b",
]

# Deterministic confidence for stage-1 matches: regex hit = fully confident.
STAGE1_CONFIDENCE = 1.0


def _detect_chitchat_or_escalation(text: str) -> str:
    """
    Returns one of: 'escalation', 'greeting', 'thanks', or '' (no match).
    Checked in this order on purpose - escalation must win over a
    greeting/thanks that happens to appear in the same message
    (e.g. "hi, I want to talk to a human").
    """
    for pattern in ESCALATION_PATTERNS:
        if re.search(pattern, text):
            return "escalation"
    for pattern in GREETING_PATTERNS:
        if re.search(pattern, text):
            return "greeting"
    for pattern in THANKS_PATTERNS:
        if re.search(pattern, text):
            return "thanks"
    return ""


# ---------------------------------------------------------------------------
# Stage 2: topic categorization
# ---------------------------------------------------------------------------

INTENT_KEYWORDS: Dict[str, List[str]] = {
    "product_info": [
        "what is hisabdo",
        "what does hisabdo do",
        "about hisabdo",
        "hisabdo app",
        "hisabdo kya hai",
        "hisabdo kya he",
    ],
    "feature": [
        "feature",
        "features",
        "khata",
        "ledger",
        "customer",
        "customers",
        "analytics",
        "report",
        "reports",
        "pdf",
        "voice",
        "calculator",
        "reminder",
        "multi currency",
    ],
    "how_to": [
        "how do i",
        "how can i",
        "how to",
        "kaise",
        "kese",
        "kis tarah",
        "add",
        "create",
        "record",
        "view",
        "update",
        "delete",
    ],
    "faq": [
        "faq",
        "account",
        "signup",
        "sign up",
        "login",
        "password",
        "transaction",
        "payment",
        "backup",
        "restore",
    ],
    "support": [
        "help",
        "problem",
        "issue",
        "error",
        "not working",
        "cannot",
        "can't",
        "failed",
        "failure",
        "masla",
        "mushkil",
        "kaam nahi",
    ],
}


def _detect_topic(text: str) -> Tuple[str, float]:
    """
    Return (intent, confidence) using keyword-count scoring.
    Confidence is a simple deterministic score, not an ML probability.
    """
    scores = {}

    for intent, keywords in INTENT_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword in text:
                score += 1
        scores[intent] = score

    best_intent = max(scores, key=scores.get)
    best_score = scores[best_intent]

    if best_score == 0:
        return "unknown", 0.0

    confidence = min(1.0, 0.5 + (best_score * 0.15))
    return best_intent, confidence


# ---------------------------------------------------------------------------
# Ambiguous-query detection
# ---------------------------------------------------------------------------

AMBIGUOUS_PHRASES = [
    "help",
    "problem",
    "issue",
    "not working",
    "doesn't work",
    "does not work",
    "error",
    "something wrong",
    "it's broken",
    "broken",
    "stuck",
    "confused",
    "i don't understand",
    "masla",
    "mushkil",
    "kaam nahi",
]

# A query at or under this length that only contains a generic
# complaint phrase (no specific feature/topic named) is treated as
# ambiguous, e.g. "help", "it is not working", "there's an issue".
AMBIGUOUS_WORD_LIMIT = 5


def is_ambiguous_query(query: str) -> bool:
    """
    Return True when the query is too vague to answer directly and
    should trigger a clarifying question instead of a search/fallback.
    """
    if not query or not query.strip():
        return True

    text = query.strip().lower()
    word_count = len(text.split())

    if word_count <= AMBIGUOUS_WORD_LIMIT and any(
        phrase in text for phrase in AMBIGUOUS_PHRASES
    ):
        return True

    return False


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def detect_intent(query: str) -> Tuple[str, float]:
    """
    Return (intent, confidence) for the given query.

    Possible intents:
      'escalation', 'greeting', 'thanks'                        (stage 1)
      'product_info', 'feature', 'how_to', 'faq', 'support'     (stage 2)
      'unknown'                                                  (no match)
    """
    text = query.lower().strip() if query else ""

    if not text:
        return "unknown", 0.0

    stage1_result = _detect_chitchat_or_escalation(text)
    if stage1_result:
        return stage1_result, STAGE1_CONFIDENCE

    return _detect_topic(text)