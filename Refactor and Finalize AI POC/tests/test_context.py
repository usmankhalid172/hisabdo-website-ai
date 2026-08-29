from services.support.context import ConversationContext


def test_context_storage():

    context = ConversationContext()

    context.update(
        query="How can I add a customer?",
        intent="how_to",
        category="Customers",
        answer="Add a customer from the customer section."
    )

    assert context.has_context()

    data = context.get_context()

    assert data["last_intent"] == "how_to"
    assert data["last_category"] == "Customers"


def test_follow_up():

    context = ConversationContext()

    context.update(
        query="How can I add a customer?",
        intent="how_to",
        category="Customers",
        answer="Add a customer."
    )

    enriched = context.enrich_follow_up(
        "What information do I need?"
    )

    assert "Customers" in enriched