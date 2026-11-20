from src.cleaning import remove_control_chars, remove_invisible_chars, normalise_unicode, normalise_whitespace


def test_remove_control_chars():
    sample_text = {"text": "Hello\x00world\nNext line"}
    result = remove_control_chars(sample_text)
    assert result["text"] == "Helloworld\nNext line"


def test_remove_invisible_chars():
    sample_text = {"text": "Hello\u200bWorld\u00a02026"}
    result = remove_invisible_chars(sample_text)
    assert result["text"] == "HelloWorld\u00a02026"


def test_normalise_whitespace():
    sample_text = {"text": "Hello    world\n\n\n\nNext paragraph"}
    result = normalise_whitespace(sample_text)
    assert result["text"] == "Hello world\n\nNext paragraph"

def test_normalise_unicode():
    sample_text = {"text": "Cafe\u0301"}
    result = normalise_unicode(sample_text)
    assert result["text"] == "Café"


def test_normalise_whitespace_idempotent():
    sample_text = {"text": "Hello    world\n\n\nNext paragraph"}
    first_result = normalise_whitespace(sample_text.copy())
    second_result = normalise_whitespace(first_result.copy())
    assert first_result == second_result

