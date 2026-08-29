from services.support.response_quality import (
    relevance_score,
    improve_response
)


def test_relevance_score():

    score = relevance_score(
        "How can I add a customer?",
        "Add a customer from the customer section."
    )

    assert score > 0


def test_quality_pass():

    result = {
        "found": True,
        "answer": (
            "Add a customer from the customer section."
        ),
        "verified": True,
        "confidence": 0.90,
        "category": "Customers"
    }

    result = improve_response(
        result,
        "How can I add a customer?"
    )

    assert result["quality"]["passed"] is True


def test_unverified_quality():

    result = {
        "found": True,
        "answer": "Unsupported answer.",
        "verified": False,
        "confidence": 0.90,
        "category": "Unknown"
    }

    result = improve_response(
        result,
        "What is HisabDo?"
    )

    assert result["found"] is False