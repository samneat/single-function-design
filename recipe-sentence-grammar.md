# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts wit a capital letter and ends with a suitable sectence-ending punctuation mark

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def check_sentence_grammar(text):
    #Parameters:
        #text: a string representing human-readable text
    # Returns:
        #boolean, true if valid, false if not
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given a sentence with a capital letter and full stop
Returns true
"""
check_sentence_grammar("Hello, this is a fine day.") => true

"""
Given a sentence with a capital letter and question mark
Returns true
"""
check_sentence_grammar("Hello, this is a fine day?") => true

"""
Given a sentence with a capital letter and exclamation mark
Returns true
"""
check_sentence_grammar("Hello, this is a fine day!") => true

"""
Given a sentence with a capital letter and comma
Returns false
"""
check_sentence_grammar("Hello, this is a fine day,") => false

"""
Given a sentence with a capital letter and colon
Returns false
"""
check_sentence_grammar("Hello, this is a fine day:") => false

"""
Given a sentence with a capital letter and no punctuation
Returns false
"""
check_sentence_grammar("Hello, this is a fine day") => false

"""
Given a sentence with no capital letter and a full stop
Returns false
"""
check_sentence_grammar("hello, this is a fine day") => false
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

```

Ensure all test function names are unique, otherwise pytest will ignore them!
