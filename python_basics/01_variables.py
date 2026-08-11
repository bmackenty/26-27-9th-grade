"""
01_variables.py  --  variables, types, input and output.

Unit 1, Week 2.

RUN IT:
    python python_basics/01_variables.py

BEFORE YOU RUN IT
Read the file top to bottom and write down what you think each print() will
show. Then run it. Every place your prediction was wrong is worth more to you
than five that were right.
"""

# ---------------------------------------------------------------------------
# 1. VARIABLES
#
# A variable is a name pointing at a value. Think of a label stuck on a box,
# not the box itself: the label can be moved to a different box at any time.
# ---------------------------------------------------------------------------

student_name = "Ana"    # the single = means "put this value into this name"
student_age = 14
student_height = 1.62
is_enrolled = True

# NAMING RULES (enforced by Python):
#   - letters, numbers and underscores only
#   - cannot start with a number
#   - case matters: name and Name are two different variables
#
# NAMING CONVENTION (enforced by people, and by your teacher):
#   - lowercase_with_underscores
#   - names that say what the thing IS.  student_age, not x or sa or thing
#
# You will read your own code far more often than you write it. Short names
# feel fast for thirty seconds and cost you an hour a week later.

print(student_name)
print(student_age)


# ---------------------------------------------------------------------------
# 2. TYPES
#
# Every value has a type. The type decides what you are allowed to do with it.
# ---------------------------------------------------------------------------

print(f"\n{student_name} is a {type(student_name)}")   # str    text
print(f"{student_age} is a {type(student_age)}")       # int    whole number
print(f"{student_height} is a {type(student_height)}") # float  decimal number
print(f"{is_enrolled} is a {type(is_enrolled)}")       # bool   True or False

# WHY IT MATTERS: + means different things for different types.
print("\nThe + operator behaves differently depending on the type:")
print(f"  2 + 3 = {2 + 3}")             # numbers: addition -> 5
print(f"  '2' + '3' = {'2' + '3'}")     # strings: joining  -> 23

# And some combinations are simply not allowed:
#   "2" + 3   raises TypeError: can only concatenate str (not "int") to str
# That error message is telling you exactly what is wrong. Read it slowly.


# ---------------------------------------------------------------------------
# 3. CONVERTING BETWEEN TYPES
# ---------------------------------------------------------------------------

age_as_text = "14"
age_as_number = int(age_as_text)     # text -> whole number
print(f"\n'{age_as_text}' converted to a number: {age_as_number + 1} next year")

price = float("2.50")                # text -> decimal number
count_as_text = str(7)               # number -> text

# int("hello") raises ValueError, because there is no sensible number in it.
# int("3.7") ALSO fails -- it wants a whole number. Use float("3.7") instead,
# or int(float("3.7")) which gives 3, throwing the .7 away without rounding.


# ---------------------------------------------------------------------------
# 4. ARITHMETIC
# ---------------------------------------------------------------------------

print("\nArithmetic:")
print(f"  7 + 2  = {7 + 2}")
print(f"  7 - 2  = {7 - 2}")
print(f"  7 * 2  = {7 * 2}")
print(f"  7 / 2  = {7 / 2}")      # / always gives a float: 3.5
print(f"  7 // 2 = {7 // 2}")     # // whole-number division: 3
print(f"  7 % 2  = {7 % 2}")      # % the remainder: 1
print(f"  7 ** 2 = {7 ** 2}")     # ** to the power of: 49

# % (modulo) looks obscure but is everywhere. n % 2 == 0 tests whether n is
# even. It is how you wrap a clock around at 12, or a list index back to zero.


# ---------------------------------------------------------------------------
# 5. STRINGS
# ---------------------------------------------------------------------------

message = "Design, Technology and Programming"

print(f"\nThe string: {message}")
print(f"  Length: {len(message)}")
print(f"  Uppercase: {message.upper()}")
print(f"  First 6 characters: {message[0:6]}")
print(f"  Does it contain 'Tech'? {'Tech' in message}")

# .upper() is a METHOD: a function that belongs to a value, called with a dot.
# Methods do not change the original. message.upper() hands back a NEW string
# and leaves message exactly as it was. Strings are immutable in Python.
print(f"  The original is unchanged: {message}")


# ---------------------------------------------------------------------------
# 6. INPUT
#
# input() stops the program and waits for someone to type something.
#
# IT ALWAYS RETURNS TEXT. Always. Even if they type 14, you get "14". Forget to
# convert and your arithmetic goes strange in ways that are hard to spot.
# ---------------------------------------------------------------------------

# Commented out so the file can run without stopping for you, and so the tests
# can run it automatically. Uncomment these lines to try it.
#
# name = input("What is your name? ")
# age_text = input("How old are you? ")
# age = int(age_text)                 # convert before doing any maths
# print(f"Hello {name}. Next year you will be {age + 1}.")
#
# What happens if the user types "fourteen"? int() raises ValueError and the
# program stops. Handling that properly is 02_conditionals.py and beyond.


print("\n--- YOUR TURN ---------------------------------------------")
print("Below this line, write code that:")
print("  1. Stores your name, your age, and your favourite number.")
print("  2. Prints a sentence using all three, with an f-string.")
print("  3. Prints your age multiplied by your favourite number.")
print("Then commit:  git commit -m 'Complete variables exercise'")
