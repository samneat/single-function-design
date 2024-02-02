from lib.check_sentence_grammar import *

def test_with_valid_sentence():
    result = check_sentence_grammar("Hello, this is a fine day.")
    assert result == True

def test_with_no_capital_no_grammar():
    result = check_sentence_grammar("hello, this is a fine day")
    assert result == False

def test_with_capital_no_end_grammar():
    result = check_sentence_grammar("Hello, this is a fine day")
    assert result == False

def test_with_capital_letter_and_question_mark():
    result = check_sentence_grammar("Hello, this is a fine day?")
    assert result == True

def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar("Hello, this is a fine day!")
    assert result == True

def test_with_capital_letter_and_comma():
    result = check_sentence_grammar("Hello, this is a fine day,")
    assert result == False

def test_start_with_lowercase_letter_and_valid_punctuation():
    result = check_sentence_grammar("hello, this is a fine day.")
