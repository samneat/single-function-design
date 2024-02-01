# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text,
assuming that I can read 200 words a minute

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def estimate_reading_time(text):
    #Parameters:
        #text: a string representing human-readable text
    #Returns:
        #a float representing reading time
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
given text of 200 words
it will return a reading time of 1.0
"""
estimate_readin_time("...200...") => 1.0

"""
given text of 400 words
it will return a reading time of 2.0
"""

estimate_readin_time("...400...") => 2.0

"""
given text of 300 words
it will return a reading time of 1.5
"""

estimate_readin_time("...300...") => 1.5

"""
given empty text
it will return 0
"""

estimate_readin_time("") => 0

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
