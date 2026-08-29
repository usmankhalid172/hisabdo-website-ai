from services.support.fallback import get_fallback


def test_unknown_english():

    result = get_fallback(
        "english",
        "unknown"
    )

    assert result
    assert "verified" in result.lower()


def test_roman_urdu_fallback():

    result = get_fallback(
        "roman_urdu",
        "unknown"
    )

    assert result


def test_urdu_fallback():

    result = get_fallback(
        "urdu",
        "unknown"
    )

    assert result


def test_ambiguous():

    result = get_fallback(
        "english",
        "ambiguous"
    )

    assert "clarify" in result.lower()