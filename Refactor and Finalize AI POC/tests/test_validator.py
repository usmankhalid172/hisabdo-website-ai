from services.support.validator import (
    validate_response,
    contains_financial_request,
    contains_numeric_claim
)


def test_verified_response():

    result = validate_response(
        query="What is HisabDo?",
        answer="HisabDo is a khata application.",
        verified=True
    )

    assert result["valid"] is True


def test_unverified_response():

    result = validate_response(
        query="What is HisabDo?",
        answer="Some unsupported information.",
        verified=False
    )

    assert result["valid"] is False


def test_financial_request():

    assert contains_financial_request(
        "What is my profit?"
    )


def test_numeric_claim():

    assert contains_numeric_claim(
        "Your profit is 5000."
    )