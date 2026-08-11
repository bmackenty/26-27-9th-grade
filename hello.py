"""
hello.py  --  your first program in this course.

Unit 1, Week 1.

WHAT IS THIS TEXT YOU ARE READING RIGHT NOW?
It is a docstring: a block of text wrapped in three quote marks. Python ignores
it when the program runs. It exists for humans. Every file you write this year
should start with one explaining what the file is for.

HOW TO RUN THIS FILE
  1. Open Terminal.
  2. Make sure your virtual environment is active (your prompt shows "(venv)").
  3. Type:   python hello.py
  4. Press Enter.

WHAT SHOULD HAPPEN
Three lines of text appear in the terminal. That is it. It is not impressive.
It is proof that the whole chain works: your editor saved the file, Python
found it, and your machine ran it. Everything else this year is built on top of
this working.
"""

# ---------------------------------------------------------------------------
# A line starting with # is a COMMENT. Python ignores it completely.
# Comments explain WHY the code does something. The code already says WHAT.
# ---------------------------------------------------------------------------

# print() is a FUNCTION. A function is a named piece of work you can ask for.
# The round brackets () mean "do it now". Whatever is inside the brackets is
# what you are handing to the function -- that is called an ARGUMENT.
#
# The quotation marks matter. "Hello, world!" with quotes is a STRING: text.
# Without quotes, Python would think Hello was the name of something and would
# stop with an error because nothing by that name exists.
print("Hello, world!")


# ---------------------------------------------------------------------------
# A VARIABLE is a name attached to a value, so you can use the value later
# without retyping it. The single = sign means "put this value into this name".
# It does NOT mean "is equal to" the way it does in maths class.
# ---------------------------------------------------------------------------

# TODO (Week 1): change the text between the quotes to your own name.
my_name = "Change this to your name"

# An f-string is a string with an f in front of it. Inside an f-string, anything
# in curly braces {} is replaced by the value of that variable.
# So if my_name holds "Ana", the line below prints: My name is Ana.
print(f"My name is {my_name}.")


# TODO (Week 1): replace this with something that is actually true about you.
# It can be anything: a place, a number that means something, a thing you want
# to build this year. One line. Make it yours.
something_personal = "I want to build something this year."
print(something_personal)


# ---------------------------------------------------------------------------
# WHEN THIS RUNS CORRECTLY
#
#   git add hello.py
#   git commit -m "Add personal details to hello.py"
#   git push
#
# Then open your repository on GitHub in a browser and check your change is
# there. Do not skip that last check. "I pushed it" and "it is on GitHub" are
# different claims, and only one of them can be verified.
# ---------------------------------------------------------------------------
