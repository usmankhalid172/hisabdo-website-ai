from services.support.intent import (
    detect_intent,
    is_ambiguous_query
)


def test_product_intent():

    intent, confidence = detect_intent(
        "What is HisabDo?"
    )

    assert intent == "product_info"
    assert confidence > 0


def test_feature_intent():

    intent, confidence = detect_intent(
        "What features does HisabDo have?"
    )

    assert intent == "feature"


def test_how_to_intent():

    intent, confidence = detect_intent(
        "How can I add a customer?"
    )

    assert intent == "how_to"


def test_support_intent():

    intent, confidence = detect_intent(
        "My backup is not working."
    )

    assert intent == "support"


def test_unknown_intent():

    intent, confidence = detect_intent(
        "What is the weather today?"
    )

    assert intent == "unknown"


def test_ambiguous_query():

    assert is_ambiguous_query(
        "How do I do it?"
    )