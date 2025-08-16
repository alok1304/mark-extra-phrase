import re
from src.insert_phrase import replace_between

# define test patterns
patterns = [
    re.compile(r"(Neither the name of )(.*?)( nor the)", re.IGNORECASE)
]

def test_already_has_extra_phrase():
    text = "Neither the name of [[6]] nor the"
    result = replace_between(text, patterns, extra_phrase="[[6]]")
    assert result == text

def test_insert_when_empty():
    text = "Neither the name of  nor the"
    result = replace_between(text, patterns, extra_phrase="[[6]]")
    assert result == "Neither the name of [[6]] nor the"

def test_replace_existing_words():
    text = "Neither the name of SomeCompany nor the"
    result = replace_between(text, patterns, extra_phrase="[[6]]")
    assert result == "Neither the name of [[6]] nor the"

def test_case_insensitivity():
    text = "neither the name of ABC Corp nor the"
    result = replace_between(text, patterns, extra_phrase="[[6]]")
    assert result == "neither the name of [[6]] nor the"

def test_multiple_occurrences():
    text = "Neither the name of X nor the, Neither the name of Y nor the"
    result = replace_between(text, patterns, extra_phrase="[[6]]")
    assert result == "Neither the name of [[6]] nor the, Neither the name of [[6]] nor the"
