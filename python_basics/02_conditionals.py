"""
02_conditionals.py  --  making decisions with if, elif and else.

Unit 1, Week 3.

RUN IT:
    python python_basics/02_conditionals.py

THE HABIT THIS FILE IS REALLY TEACHING
Write the decision in English before you write it in Python. Every professional
does this, on paper or in comments. Skipping it is how you end up with code
that runs and gives the wrong answer -- much harder to spot than code that
crashes.
"""

# ---------------------------------------------------------------------------
# 1. COMPARISON -- questions that produce True or False
# ---------------------------------------------------------------------------

print("Comparisons:")
print(f"  5 > 3   is {5 > 3}")
print(f"  5 < 3   is {5 < 3}")
print(f"  5 == 5  is {5 == 5}")     # == asks "are these equal?"
print(f"  5 != 3  is {5 != 3}")     # != asks "are these different?"
print(f"  5 >= 5  is {5 >= 5}")
print(f"  'a' == 'A' is {'a' == 'A'}")   # False: case matters

# THE MOST COMMON BEGINNER BUG IN ANY LANGUAGE:
#   =   assignment. Put this value into this name.
#   ==  comparison. Are these two things equal?
# Say it out loud every time you type one. It sticks faster that way.


# ---------------------------------------------------------------------------
# 2. IF / ELIF / ELSE
#
# Python decides what belongs inside an if by INDENTATION -- the four spaces at
# the start of the line. Other languages use curly braces; Python uses
# whitespace, which means whitespace is not decoration here, it is grammar.
# ---------------------------------------------------------------------------

score = 78

print(f"\nScore is {score}")

if score >= 90:
    # Everything indented under the if runs only when the condition is True.
    print("  Grade: 7")
elif score >= 80:
    # elif means "else, if". Checked only if the ones above were all False.
    print("  Grade: 6")
elif score >= 70:
    print("  Grade: 5")
elif score >= 60:
    print("  Grade: 4")
else:
    # else is the catch-all. No condition; it runs when nothing above matched.
    print("  Grade: below 4")

# ORDER MATTERS ENORMOUSLY. Python checks top to bottom and stops at the first
# match. Put `if score >= 60` first and a score of 95 would print "Grade: 4",
# because 95 is indeed 60 or more. The code would run perfectly and be wrong.
# This is exactly the sort of bug that tests catch and eyes do not.


# ---------------------------------------------------------------------------
# 3. COMBINING CONDITIONS: and, or, not
# ---------------------------------------------------------------------------

age = 14
has_permission = True

print(f"\nage = {age}, has_permission = {has_permission}")

# and -> both sides must be True
if age >= 13 and has_permission:
    print("  Can join the coding club.")

# or -> at least one side must be True
if age < 13 or not has_permission:
    print("  Needs a parent form.")
else:
    print("  No form needed.")

# not -> flips True to False and back
print(f"  not True is {not True}")

# TRUTH TABLES, worth knowing cold:
#   True  and True  -> True      True  or True  -> True
#   True  and False -> False     True  or False -> True
#   False and True  -> False     False or True  -> True
#   False and False -> False     False or False -> False


# ---------------------------------------------------------------------------
# 4. A COMMON MISTAKE
# ---------------------------------------------------------------------------

day = "Saturday"

# WRONG -- and it does not even crash, which is what makes it dangerous:
#     if day == "Saturday" or "Sunday":
#
# Python reads that as:  (day == "Saturday")  or  ("Sunday")
# A non-empty string counts as True, so the whole thing is ALWAYS True. The
# code runs, reports a weekend every day of the week, and never complains.

# RIGHT -- state the full comparison both times:
if day == "Saturday" or day == "Sunday":
    print(f"\n{day} is the weekend.")

# ALSO RIGHT, and easier to extend later:
if day in ["Saturday", "Sunday"]:
    print(f"{day} is in the weekend list.")


# ---------------------------------------------------------------------------
# 5. NESTING
# ---------------------------------------------------------------------------

temperature = 22
is_raining = False

print(f"\ntemperature = {temperature}, is_raining = {is_raining}")

if temperature > 18:
    if is_raining:
        print("  Warm but wet. Take a jacket.")
    else:
        print("  Warm and dry. Go outside.")
else:
    print("  Cold. Stay in.")

# Nesting works, but it gets hard to follow fast. Three levels deep is usually
# a sign the logic wants to be split into a function -- see 04_functions.py.


print("\n--- YOUR TURN ---------------------------------------------")
print("Write, IN ENGLISH FIRST as a comment, then in Python:")
print("  A program that decides whether someone can borrow a laptop.")
print("  Rules: they must be in Grade 9 or above, have no unreturned")
print("  equipment, and if it is after 3pm they also need a teacher note.")
print("Test it with at least four different combinations of inputs,")
print("including one that should be refused.")
