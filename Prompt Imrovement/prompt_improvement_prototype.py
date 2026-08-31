"""
HisabDo AI Copilot - Prompt Improvement Prototype
Prepared By: Muhammad Taha

This is a lightweight local prototype for demonstrating prompt-policy
construction and validation. It does not connect to a real LLM, database,
or financial API.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class AIRequest:
    message: str
    language: str = "auto"
    intent: str = "UNKNOWN"
    verified_context: str = ""


SYSTEM_RULES = [
    "Do not invent financial values.",
    "Use verified context for factual product answers.",
    "Do not expose unauthorized user data.",
    "Respond in the user's language when supported.",
    "Ask for clarification when an entity or context is ambiguous.",
    "Use a safe fallback when verified information is unavailable.",
]


def normalize_roman_urdu(text: str) -> str:
    replacements = {
        "kitny": "kitna",
        "kitnay": "kitna",
        "paisay": "paisa",
        "pese": "paisa",
        "udharr": "udhaar",
        "udhar": "udhaar",
        "btao": "batao",
    }
    normalized = text.lower()
    for source, target in replacements.items():
        normalized = normalized.replace(source, target)
    return normalized


def build_prompt(request: AIRequest) -> str:
    normalized_message = normalize_roman_urdu(request.message)

    return f"""SYSTEM RULES:
{chr(10).join(f"- {rule}" for rule in SYSTEM_RULES)}

REQUEST:
Original message: {request.message}
Normalized message: {normalized_message}
Language: {request.language}
Intent: {request.intent}

VERIFIED CONTEXT:
{request.verified_context or "[No verified context available]"}

RESPONSE REQUIREMENT:
Answer only within the available verified context when factual accuracy is
required. If required information is unavailable, do not guess; use a safe
fallback or request clarification.
"""


def validate_response(response: str, intent: str,
                      has_verified_context: bool) -> List[str]:
    issues = []

    if intent in {"CUSTOMER_BALANCE_QUERY", "EXPENSE_QUERY",
                  "RECEIVABLE_QUERY"} and not has_verified_context:
        issues.append(
            "Financial response cannot be approved without verified context."
        )

    forbidden = ["i made up", "probably", "i guess"]
    lower_response = response.lower()

    for phrase in forbidden:
        if phrase in lower_response:
            issues.append(f"Potential unsupported statement: '{phrase}'")

    return issues


def run_demo() -> None:
    request = AIRequest(
        message="Ali ka kitny paisay udhar hain?",
        language="roman-urdu",
        intent="CUSTOMER_BALANCE_QUERY",
        verified_context="Customer: Ali; Balance: PKR 25,000",
    )

    prompt = build_prompt(request)

    print("=== GENERATED PROMPT ===")
    print(prompt)

    sample_response = "Ali ka current outstanding balance PKR 25,000 hai."

    issues = validate_response(
        sample_response,
        request.intent,
        bool(request.verified_context),
    )

    print("\n=== VALIDATION ===")
    print("PASS" if not issues else "FAIL")
    for issue in issues:
        print("-", issue)


if __name__ == "__main__":
    run_demo()
