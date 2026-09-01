def classify_intent(message: str) -> str:
    text = message.lower()
    if any(k in text for k in ["how", "feature", "customer", "backup", "report", "export"]):
        return "FAQ_QUERY"
    if any(k in text for k in ["balance", "udhar", "owe", "expense", "receivable"]):
        return "FINANCIAL_QUERY"
    if len(text.strip()) < 3:
        return "UNKNOWN"
    return "GENERAL_CONVERSATION"
