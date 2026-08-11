"""
03_loops.py  --  doing something many times.

Unit 1, Week 4.

RUN IT:
    python python_basics/03_loops.py

THE IDEA
A loop is how you write "do this for every item" once instead of copying the
same three lines twenty times. Anywhere you find yourself copy-pasting code and
changing one number, a loop is what you actually wanted.
"""

# ---------------------------------------------------------------------------
# 1. FOR LOOPS OVER A LIST
#
# A for loop takes each item in turn and puts it into a variable you name.
# ---------------------------------------------------------------------------

pathways = ["Game Programming", "Computer Science", "Practical Computing"]

print("The pathways:")
for pathway in pathways:
    # "pathway" is a name we invented. It could be anything, but a good name
    # makes the loop read like a sentence: for pathway in pathways.
    print(f"  - {pathway}")

# After the loop finishes, pathway still holds the last item. Relying on that
# is a habit worth avoiding: it works, but it surprises the next reader.


# ---------------------------------------------------------------------------
# 2. FOR LOOPS OVER A RANGE OF NUMBERS
# ---------------------------------------------------------------------------

print("\nrange(5) gives 0, 1, 2, 3, 4:")
for i in range(5):
    print(f"  i is {i}")

# THE STOP VALUE IS NOT INCLUDED. range(5) stops before 5, giving five numbers
# starting at 0. This matches list indexing, where the first item is 0, so the
# two fit together neatly once you are used to it.

print("\nrange(1, 6) gives 1 to 5:")
for i in range(1, 6):
    print(f"  {i} squared is {i ** 2}")

print("\nrange(0, 21, 5) counts in fives:")
for i in range(0, 21, 5):
    print(f"  {i}")
# The third number is the STEP: how much to add each time.


# ---------------------------------------------------------------------------
# 3. BUILDING UP AN ANSWER -- the accumulator pattern
# ---------------------------------------------------------------------------

hours = [14, 6, 11, 4, 9]

# Start with an empty answer, then add to it on each pass.
total = 0
for hour in hours:
    total = total + hour       # or the shorthand:  total += hour

print(f"\nHours: {hours}")
print(f"Total: {total}")
print(f"Average: {round(total / len(hours), 1)}")

# THE CLASSIC BUG: putting total = 0 INSIDE the loop. Then it resets to zero on
# every pass and the answer is always just the last item. If a total comes out
# suspiciously small, check where it is initialised first.


# ---------------------------------------------------------------------------
# 4. COUNTING AND FILTERING
# ---------------------------------------------------------------------------

long_projects = 0
for hour in hours:
    if hour > 10:
        long_projects += 1

print(f"Projects over 10 hours: {long_projects}")

# Finding the largest, by hand. Python has max(), but writing it out yourself
# once shows you what max() is actually doing.
biggest = hours[0]              # assume the first is the winner
for hour in hours:
    if hour > biggest:
        biggest = hour          # found a better one; remember it instead

print(f"Longest project: {biggest} hours (max() agrees: {max(hours)})")


# ---------------------------------------------------------------------------
# 5. WHILE LOOPS
#
# A for loop runs a known number of times. A while loop runs until a condition
# stops being true -- which might be never, if you are not careful.
# ---------------------------------------------------------------------------

countdown = 5
print("\nA while loop:")
while countdown > 0:
    print(f"  {countdown}")
    countdown = countdown - 1   # THE LINE THAT MATTERS MOST
print("  Liftoff.")

# Delete that last line inside the loop and countdown stays at 5 forever. The
# program prints 5 endlessly and never stops. That is an INFINITE LOOP, and
# Control + C is how you escape one. Every while loop needs something inside it
# that eventually makes the condition false -- check for it before you run.


# ---------------------------------------------------------------------------
# 6. BREAK AND CONTINUE
# ---------------------------------------------------------------------------

print("\nbreak leaves the loop early:")
for number in range(10):
    if number == 4:
        break                   # stop the loop entirely
    print(f"  {number}")

print("continue skips the rest of this pass:")
for number in range(6):
    if number % 2 == 0:
        continue                # jump straight to the next number
    print(f"  {number} is odd")

# Both are useful and both make a loop harder to follow. Use them when they
# genuinely simplify, not to avoid thinking about the condition.


# ---------------------------------------------------------------------------
# 7. NESTED LOOPS
# ---------------------------------------------------------------------------

print("\nA times table with a loop inside a loop:")
for row in range(1, 4):
    line = ""
    for column in range(1, 4):
        # :>4 pads each number to 4 characters so the columns line up.
        line += f"{row * column:>4}"
    print(f"  {line}")

# The inner loop runs completely for EACH pass of the outer loop. 3 x 3 = 9
# multiplications here. Nest three loops over a thousand items each and you
# have a billion passes -- which is where "why is my program so slow" begins.


print("\n--- YOUR TURN ---------------------------------------------")
print("  1. Print every even number from 2 to 20 using a for loop.")
print("  2. Given [3, 17, 8, 22, 5], find the smallest WITHOUT using min().")
print("  3. Write a while loop that doubles a number starting at 1 and")
print("     stops as soon as it passes 1000. How many doublings?")
print("  4. Predict the answer to 3 before you run it. Write it down.")
