KNOWLEDGE_BASE = {
    "add customer": "To add a customer, open the customer section and use the add customer option.",
    "backup": "HisabDo backup and restore should use the application's supported backup workflow.",
    "export report": "Reports can be exported using the available report/export feature when supported by the application."
}

def search_knowledge(query: str):
    q = query.lower()
    for key, value in KNOWLEDGE_BASE.items():
        if key in q or any(word in q for word in key.split()):
            return {"content": value, "verified": True}
    return None
