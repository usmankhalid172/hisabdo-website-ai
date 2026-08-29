from services.support.faq_service import search_faq


def test_customer_faq():

    result = search_faq(
        "How can I add a customer?"
    )

    assert result["found"] is True
    assert result["verified"] is True


def test_expense_faq():

    result = search_faq(
        "How can I add an expense?"
    )

    assert result["found"] is True
    assert result["verified"] is True


def test_unknown_question():

    result = search_faq(
        "What is the weather today?"
    )

    assert result["found"] is Falses