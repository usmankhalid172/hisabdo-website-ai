def generate_ai_response(query):
    """
    Basic AI assistant query handler.
    """

    query = query.strip()

    if not query:
        return {
            "success": False,
            "message": "Please enter a valid question."
        }

    query_lower = query.lower()

    # Basic verified responses
    if "add expense" in query_lower or "add an expense" in query_lower:
        answer = (
            "To add an expense in HisabDo, open the expense section, "
            "select Add Expense, enter the required details, and save it."
        )

    elif "expense" in query_lower:
        answer = (
            "HisabDo allows you to record and manage your expenses. "
            "You can add an expense by providing its basic details."
        )

    elif "budget" in query_lower:
        answer = (
            "You can use the budget section to manage and monitor "
            "your planned spending."
        )

    elif "help" in query_lower:
        answer = (
            "I can help you with expenses, budgets, and basic HisabDo "
            "features. Please ask your question."
        )

    else:
        answer = (
            "I couldn't find a verified answer for this question yet. "
            "Please try asking about expenses, budgets, or HisabDo features."
        )

    return {
        "success": True,
        "query": query,
        "answer": answer
    }