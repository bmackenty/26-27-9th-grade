"""
test_helpers.py  --  automatic checks on the functions in helpers.py.

RUN THEM:
    pytest                      run every test
    pytest -v                   show each test by name
    pytest tests/test_helpers.py    just this file

WHAT A TEST IS
Code that checks other code. You state what you EXPECT, and pytest tells you
whether reality agrees. If it does, you see a dot. If it does not, you get told
exactly which check failed and what it got instead.

WHY BOTHER
You already test your code -- by running it and looking at the output. The
problem is that you only test the thing you just changed, and only once. Tests
check everything, every time, in under a second. The first time a test catches
something you broke in a part of the program you had not touched in a fortnight,
the habit sells itself.

HOW PYTEST FINDS TESTS
  - files named  test_*.py
  - functions named  test_*
Nothing to register. Follow the naming and pytest finds it.
"""

import pytest

# Import the functions we want to check. This works because of conftest.py.
from helpers import (
    average,
    calculate_grade,
    count_by_key,
    count_vowels,
    is_valid_grade_level,
)


# ---------------------------------------------------------------------------
# TESTING calculate_grade
# ---------------------------------------------------------------------------

def test_calculate_grade_top_band():
    """A score of 95 should be a 7.

    `assert` is the whole mechanism. It means: this must be true. If it is,
    nothing happens and the test passes. If it is not, the test fails and
    pytest shows you both values.
    """
    assert calculate_grade(95) == 7


def test_calculate_grade_middle_band():
    assert calculate_grade(75) == 5


def test_calculate_grade_bottom_band():
    assert calculate_grade(12) == 1


def test_calculate_grade_boundaries():
    """The edges are where bugs live.

    90 should be a 7 and 89 should be a 6. An "off-by-one" error -- writing >
    where you meant >= -- would pass every test above and fail these two. Always
    test the boundary, not just the comfortable middle of a range.
    """
    assert calculate_grade(90) == 7
    assert calculate_grade(89) == 6
    assert calculate_grade(80) == 6
    assert calculate_grade(79) == 5


# ---------------------------------------------------------------------------
# TESTING average
# ---------------------------------------------------------------------------

def test_average_normal_case():
    assert average([10, 20, 30]) == 20


def test_average_single_item():
    assert average([7]) == 7


def test_average_empty_list():
    """The awkward case. This is the test that matters most.

    An empty list would divide by zero without the guard clause in average().
    Every function that takes a collection should be tested with an empty one.
    """
    assert average([]) == 0.0


def test_average_gives_a_decimal():
    """1 + 2 = 3, divided by 2 is 1.5 -- not 1.

    In Python 3 the / operator always produces a float. In some older languages
    this would give 1, silently throwing the half away.
    """
    assert average([1, 2]) == 1.5


# ---------------------------------------------------------------------------
# TESTING count_by_key
# ---------------------------------------------------------------------------

def test_count_by_key_groups_correctly():
    records = [
        {"name": "Ana", "pathway": "Game"},
        {"name": "Ben", "pathway": "CS"},
        {"name": "Cara", "pathway": "Game"},
    ]

    result = count_by_key(records, "pathway")

    # Comparing whole dictionaries at once. Order does not matter in a
    # dictionary comparison, which is exactly what we want here.
    assert result == {"Game": 2, "CS": 1}


def test_count_by_key_with_missing_key():
    """A record without the key should be counted under None, not crash.

    Real data is always missing something. Decide what your code does about it
    deliberately, then write a test that pins that decision down.
    """
    records = [
        {"name": "Ana", "pathway": "Game"},
        {"name": "Igor"},   # no pathway at all
    ]

    result = count_by_key(records, "pathway")

    assert result == {"Game": 1, None: 1}


# ---------------------------------------------------------------------------
# TESTING is_valid_grade_level
# ---------------------------------------------------------------------------

# @pytest.mark.parametrize runs the SAME test with different values. Far better
# than writing eight nearly identical functions. Each pair below is
# (input, expected result).
@pytest.mark.parametrize("value,expected", [
    (9, True),          # a normal number
    ("9", True),        # the same thing as text, as it arrives from a CSV
    (6, True),          # bottom boundary
    (12, True),         # top boundary
    (5, False),         # just below
    (13, False),        # just above
    ("nine", False),    # words, not digits
    (None, False),      # nothing at all
])
def test_is_valid_grade_level(value, expected):
    assert is_valid_grade_level(value) is expected
    # `is` compares identity rather than equality. For True, False and None it
    # is the more precise check, and it stops 1 quietly counting as True.


# ---------------------------------------------------------------------------
# TESTS THAT FAIL ON PURPOSE
#
# count_vowels() in helpers.py is unfinished. These tests describe what it
# should do, and they fail until you write it. That is deliberate: the test
# comes first, then the code that satisfies it.
#
# xfail means "expected to fail". pytest reports it without turning the whole
# run red. When you finish the function these will report XPASS -- unexpectedly
# passing -- at which point delete the two xfail lines and they become normal
# tests.
# ---------------------------------------------------------------------------

@pytest.mark.xfail(reason="count_vowels is not written yet -- Unit 1 Week 5")
def test_count_vowels_simple():
    assert count_vowels("hello") == 2


@pytest.mark.xfail(reason="count_vowels is not written yet -- Unit 1 Week 5")
def test_count_vowels_ignores_case():
    assert count_vowels("AEIOU") == 5
    assert count_vowels("Programming") == 3
    assert count_vowels("") == 0
    assert count_vowels("rhythm") == 0
