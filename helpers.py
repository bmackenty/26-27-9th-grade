"""
helpers.py  --  small functions that other files (and the tests) can use.

Units 1-3.

WHY THIS FILE EXISTS
The examples in python_basics/ are written to be READ and RUN. They print a lot
of explanatory text, which makes them poor to import: importing a file runs
everything in it, and you would get pages of output every time.

So the functions we actually want to reuse and test live here, clean and quiet,
with no print() at the top level. That separation -- explanation in one place,
reusable code in another -- is a real pattern, not a classroom convenience.

Every function here is checked by tests/test_helpers.py. Run them with:
    pytest
"""


def calculate_grade(score):
    """Convert a percentage into an IB 1-7 grade.

    Args:
        score: a number from 0 to 100.

    Returns:
        A whole number from 1 to 7.

    Note the order of the checks: highest boundary first. Reverse them and a
    score of 95 would match `score >= 40` and return 2. The program would run
    without complaint and be completely wrong -- which is exactly the kind of
    bug that tests exist to catch.
    """
    if score >= 90:
        return 7
    elif score >= 80:
        return 6
    elif score >= 70:
        return 5
    elif score >= 60:
        return 4
    elif score >= 50:
        return 3
    elif score >= 40:
        return 2
    else:
        return 1


def average(numbers):
    """Average of a list of numbers.

    Returns 0.0 for an empty list instead of crashing with ZeroDivisionError.
    That choice is a design decision, and you should be ready to defend it:
    returning None would also be reasonable, and arguably more honest.
    """
    if len(numbers) == 0:
        return 0.0
    return sum(numbers) / len(numbers)


def count_by_key(records, key):
    """Count how many records share each value of a given key.

    Args:
        records: a list of dictionaries.
        key:     which key to group by, e.g. "pathway".

    Returns:
        A dictionary of value -> count.

    This is the Python version of SQL's GROUP BY. Compare it with the queries
    in data_work/sql_version.py -- same job, different tool. Knowing when to
    do this work in Python and when to let the database do it is a real skill.
    """
    counts = {}

    for record in records:
        # .get(key) returns None rather than crashing if the key is missing.
        value = record.get(key)

        # counts.get(value, 0) means "the count so far, or 0 if it is new".
        counts[value] = counts.get(value, 0) + 1

    return counts


def is_valid_grade_level(value):
    """Check that something is a plausible grade level (6 to 12).

    Written to accept text as well as numbers, because data arriving from a CSV
    file or a web form is always text. Real input validation always has to deal
    with the wrong type turning up.
    """
    try:
        # try/except: attempt the risky thing, and catch the failure if it comes.
        number = int(value)
    except (ValueError, TypeError):
        # ValueError: the text was not a number, e.g. "nine".
        # TypeError:  it was something int() cannot handle at all, e.g. None.
        # Catching only the errors you expect is important. A bare `except:`
        # swallows everything, including your own typos, and hides real bugs.
        return False

    return 6 <= number <= 12
    # Python allows chained comparison. It reads exactly as it looks:
    # 6 is less than or equal to number, which is less than or equal to 12.


# ---------------------------------------------------------------------------
# TODO (Unit 1, Week 5): write this function.
#
# tests/test_helpers.py already contains tests for it. They fail right now.
# Your job is to make them pass. Working this way round -- test first, code
# second -- has a name: test-driven development.
#
# Delete the `pass` and write real code.
# ---------------------------------------------------------------------------

def count_vowels(text):
    """Count the vowels (a, e, i, o, u) in a piece of text.

    Should not care about capital letters: "AEIOU" has five vowels.

    Args:
        text: a string.

    Returns:
        A whole number.
    """
    # `pass` means "do nothing". It is a placeholder that lets an unfinished
    # function exist without a syntax error. Replace it.
    pass
