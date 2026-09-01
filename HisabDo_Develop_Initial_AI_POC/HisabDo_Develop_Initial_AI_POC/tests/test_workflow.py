from app.orchestrator import handle_query

def test_faq_query():
    result = handle_query("How do I add a customer?")
    assert result["type"] == "FAQ_QUERY"

def test_financial_query_requires_verified_data():
    result = handle_query("Ali ka udhar kitna hai?")
    assert "verified" in result["source"]["type"]

def test_unknown_faq_fallback():
    result = handle_query("How does the imaginary feature work?")
    assert result["message"]
