"""
04_functions.py  --  giving a piece of work a name.

Unit 1, Week 5.

RUN IT:
    python python_basics/04_functions.py

THE SHIFT THIS FILE IS ABOUT
Early programs print things. Real programs RETURN things. A function that only
prints is like a calculator that shows you the answer but will not let you use
it in the next sum. Returning a value means the rest of your program can use
the result -- and it means the function can be tested. That second point is
why every test in tests/ works on functions that return.
"""


# ---------------------------------------------------------------------------
# 1. DEFINING AND CALLING
# ---------------------------------------------------------------------------

def greet():
    """Say hello.

    def          starts a definition
    greet        the name we are giving it
    ()           the inputs it takes -- none here
    :            required, ends the def line
    indentation  everything indented below belongs to the function
    """
    print("Hello from inside a function.")


# Defining a function does NOT run it. It only teaches Python the name.
# Calling it -- with the brackets -- is what makes it happen.
greet()

# Writing greet without brackets does not call it. It just refers to the
# function itself, and Python quietly does nothing at all. If a function
# "isn't running", missing brackets is the first thing to check.


# ---------------------------------------------------------------------------
# 2. PARAMETERS -- giving a function something to work on
# ---------------------------------------------------------------------------

def greet_person(name):
    """Say hello to a particular person.

    `name` is a PARAMETER: a placeholder used inside the function.
    The value handed in when you call it is the ARGUMENT.
    """
    print(f"Hello, {name}.")


greet_person("Ana")     # "Ana" is the argument
greet_person("Ben")     # one definition, any number of uses


def describe_student(name, grade, pathway="not chosen"):
    """Parameters can have DEFAULT values.

    pathway has a default, so it may be left out when calling. Parameters with
    defaults must come after those without -- Python enforces this.
    """
    print(f"{name}, Grade {grade}, pathway: {pathway}")


describe_student("Chidi", 9, "Computational Biology")
describe_student("Igor", 9)                            # default used

# You can also name arguments when calling. Clearer, and order stops mattering.
describe_student(grade=9, name="Dasha", pathway="Computing in Business")


# ---------------------------------------------------------------------------
# 3. RETURN -- handing a value back
# ---------------------------------------------------------------------------

def add(a, b):
    """Add two numbers and hand the result back."""
    return a + b


# The returned value can be stored, printed, or fed into something else.
result = add(3, 4)
print(f"\nadd(3, 4) returned {result}")
print(f"add(add(1, 2), add(3, 4)) is {add(add(1, 2), add(3, 4))}")

# Compare the two versions below. Both look the same when you run them:
def add_and_print(a, b):
    print(a + b)        # shows the answer, then throws it away

def add_and_return(a, b):
    return a + b        # hands the answer back to be used

# But only the second can do this:
doubled = add_and_return(3, 4) * 2
print(f"Because it returns, we can use the result: {doubled}")

# add_and_print(3, 4) * 2 crashes: the function returns None, and you cannot
# multiply None by 2. THIS IS THE MOST IMPORTANT IDEA IN THE FILE.

# A function with no return statement returns None. Not zero, not an empty
# string -- None, meaning "nothing here".
print(f"add_and_print returns: {add_and_print(1, 1)}")

# return also ENDS the function immediately. Anything after it never runs.


# ---------------------------------------------------------------------------
# 4. WHY FUNCTIONS ARE WORTH THE EFFORT
# ---------------------------------------------------------------------------

def calculate_grade(score):
    """Turn a percentage into an IB 1-7 grade.

    All the grade logic lives in exactly one place. Change the boundaries here
    and every part of the program that grades anything updates at once.
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


print("\nGrades:")
for score in [95, 83, 71, 45]:
    print(f"  {score}% -> grade {calculate_grade(score)}")

# Because this RETURNS, it can be tested automatically. Look at
# tests/test_functions.py to see calculate_grade being checked against known
# answers. A function that printed instead would be far harder to test.


def average(numbers):
    """Average of a list. Returns 0.0 for an empty list rather than crashing."""
    # GUARD CLAUSE: deal with the awkward case first and leave early. The rest
    # of the function can then assume things are normal, which keeps it flat
    # and readable instead of wrapping everything in a giant if.
    if len(numbers) == 0:
        return 0.0

    return sum(numbers) / len(numbers)


print(f"\naverage([10, 20, 30]) = {average([10, 20, 30])}")
print(f"average([]) = {average([])}   (no crash)")

# Dividing by zero raises ZeroDivisionError. The guard clause is what stops it.
# Deciding what an empty input SHOULD produce is a design decision -- 0.0 is
# one defensible answer, and returning None is another. Be able to justify it.


# ---------------------------------------------------------------------------
# 5. SCOPE -- where a variable can be seen
# ---------------------------------------------------------------------------

message = "I am outside the function"


def show_scope():
    inside = "I am inside the function"
    print(f"\n  Inside, I can see: {message}")   # outer variables are visible
    print(f"  Inside, I can see: {inside}")


show_scope()
print(f"  Outside, I can see: {message}")
# print(inside) here would raise NameError. `inside` was created inside the
# function and stops existing the moment the function ends. That is a feature:
# it means two functions can both use a variable called `total` without ever
# interfering with each other.


print("\n--- YOUR TURN ---------------------------------------------")
print("Write functions that RETURN (do not print) values:")
print("  1. is_even(number) -> True or False")
print("  2. longest_word(sentence) -> the longest word in it")
print("  3. count_vowels(text) -> how many vowels it contains")
print("Then add a test for each in tests/test_functions.py and run pytest.")
