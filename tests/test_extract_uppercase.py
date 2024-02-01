from lib.extract_uppercase import *

def test_with_empty_string():
    assert extract_uppercase("") == []

def test_with_only_lowercase_words():
    assert extract_uppercase("hello world") == []

def test_with_one_uppercase_word():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

def test_with_mixed_case_words():
    result = extract_uppercase("hello WoRLD YES")
    assert result == ["YES"]

def test_with_punctuation_returns_only_words():
    result = extract_uppercase("THIS: is COOL")
    assert result == ["THIS", "COOL"]