from services.support.language import detect_language


def test_english():

    assert detect_language(
        "How can I add a customer?"
    ) == "english"


def test_roman_urdu():

    assert detect_language(
        "customer kaise add karun?"
    ) == "roman_urdu"


def test_urdu():

    assert detect_language(
        "میں کسٹمر کیسے شامل کروں؟"
    ) == "urdu"