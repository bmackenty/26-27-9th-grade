"""
lists_and_dicts.py  --  the two data structures you will use most.

Unit 3, Weeks 1-2.

RUN IT:
    python data_work/lists_and_dicts.py

HOW TO USE THIS FILE
Do not just run it. Read one section, predict what it prints, write the
prediction down, then run it and compare. The sections where you were wrong are
the ones to study. Being wrong here costs nothing, which is the whole reason we
do it here.
"""


def section_1_lists():
    """A LIST is an ordered collection. Things stay in the order you put them."""
    print("\n=== 1. LISTS ==============================================")

    # Square brackets make a list. Items are separated by commas.
    pathways = ["Game Programming", "Computer Science", "Computational Biology"]

    print(f"The list: {pathways}")

    # len() gives the number of items.
    print(f"It holds {len(pathways)} items.")

    # --- Indexing ---------------------------------------------------------
    # COUNTING STARTS AT ZERO. The first item is at index 0. This trips up
    # everyone at the start, so say it out loud a few times.
    print(f"First item  (index 0): {pathways[0]}")
    print(f"Second item (index 1): {pathways[1]}")

    # A negative index counts backwards from the end. -1 is the last item.
    # Useful because it works no matter how long the list is.
    print(f"Last item  (index -1): {pathways[-1]}")

    # pathways[3] would crash with IndexError: there is no index 3. The list
    # has three items at 0, 1, and 2. Try it later, on purpose, so you
    # recognise that error when it arrives by accident.

    # --- Changing a list --------------------------------------------------
    # Lists are MUTABLE: they can be changed after they are created.
    pathways.append("Computing in Business")   # add to the end
    print(f"After append: {pathways}")

    pathways.insert(0, "Practical Computing")  # add at a chosen position
    print(f"After insert at 0: {pathways}")

    removed = pathways.pop()                   # remove and return the last item
    print(f"Popped {removed!r}, leaving {len(pathways)} items.")

    # --- Slicing -----------------------------------------------------------
    # [start:stop] gives a piece of the list. The start is included, the stop
    # is NOT. So [0:2] gives items 0 and 1 -- two items, not three.
    print(f"First two: {pathways[0:2]}")
    print(f"From index 2 onward: {pathways[2:]}")

    # --- Looping -----------------------------------------------------------
    print("Looping through the list:")
    for pathway in pathways:
        print(f"  - {pathway}")

    # enumerate() gives you the position AND the item, which saves you from
    # keeping a counter variable of your own.
    print("Looping with position numbers:")
    for position, pathway in enumerate(pathways, start=1):
        print(f"  {position}. {pathway}")


def section_2_dictionaries():
    """A DICTIONARY stores pairs: a KEY, and the VALUE it points at."""
    print("\n=== 2. DICTIONARIES =======================================")

    # Curly braces make a dictionary. Each entry is  key: value.
    student = {
        "name": "Ana Kowalski",
        "grade": 9,
        "pathway": "Game Programming",
        "hours": 20,
    }

    print(f"The dictionary: {student}")

    # --- Looking things up ------------------------------------------------
    # Use the KEY, not a number. Order is not how you find things here.
    print(f"Name: {student['name']}")
    print(f"Grade: {student['grade']}")

    # student["email"] would crash with KeyError, because there is no such key.
    # .get() returns None instead of crashing, and lets you supply a fallback.
    print(f"Email (missing): {student.get('email')}")
    print(f"Email with fallback: {student.get('email', 'not recorded')}")

    # --- Changing a dictionary --------------------------------------------
    student["hours"] = 26        # change an existing value
    student["email"] = "ana@aswarsaw.org"   # a new key is created on assignment
    print(f"After changes: {student}")

    # --- Looping -----------------------------------------------------------
    # .items() gives back both the key and the value on each pass.
    print("Every key and value:")
    for key, value in student.items():
        print(f"  {key:<10} {value}")

    # WHEN TO USE WHICH
    #   LIST        an ordered sequence, and position matters
    #               e.g. the students in a class, in order
    #   DICTIONARY  labelled facts about one thing, looked up by name
    #               e.g. everything about ONE student
    # Being able to justify that choice out loud is a Unit 3 objective.


def section_3_list_of_dicts():
    """A list of dictionaries: the shape almost all real data arrives in."""
    print("\n=== 3. A LIST OF DICTIONARIES =============================")

    # This is what a CSV file becomes when you read it, and what an API sends
    # you. Get comfortable with it now and a lot of later work gets easier.
    students = [
        {"name": "Ana",   "pathway": "Game Programming", "hours": 20},
        {"name": "Ben",   "pathway": "Computer Science", "hours": 15},
        {"name": "Chidi", "pathway": "Computational Biology", "hours": 9},
        {"name": "Dasha", "pathway": "Computing in Business", "hours": 12},
        {"name": "Elias", "pathway": "Practical Computing", "hours": 7},
    ]

    # Two levels of access: pick a dictionary from the list, then a key from it.
    print(f"First student's name: {students[0]['name']}")

    # --- Filtering ---------------------------------------------------------
    print("Students with more than 10 hours:")
    for student in students:
        if student["hours"] > 10:
            print(f"  {student['name']} ({student['hours']}h)")

    # The same filter written as a LIST COMPREHENSION: build a new list from an
    # old one, in a single line. Read it as: "student, for each student in
    # students, if their hours are over 10."
    busy = [s for s in students if s["hours"] > 10]
    print(f"As a comprehension: {[s['name'] for s in busy]}")

    # Comprehensions are compact, not compulsory. A for loop you understand
    # beats a comprehension you copied. In an oral check you will be asked to
    # rewrite one as the other, so practise both directions.

    # --- Totalling ---------------------------------------------------------
    # sum() adds up a sequence of numbers.
    total_hours = sum(s["hours"] for s in students)
    print(f"Total hours across the class: {total_hours}")

    # round() to one decimal place, so the average is readable.
    average = round(total_hours / len(students), 1)
    print(f"Average hours per student: {average}")

    # --- Sorting -----------------------------------------------------------
    # sorted() returns a NEW list; it leaves the original alone.
    #
    # key=... tells sorted() what to compare. The lambda is a small unnamed
    # function meaning "given a student, hand back their hours".
    # reverse=True sorts largest first.
    by_hours = sorted(students, key=lambda s: s["hours"], reverse=True)
    print("Sorted by hours, most first:")
    for student in by_hours:
        print(f"  {student['name']:<8} {student['hours']}h")

    # --- Grouping ----------------------------------------------------------
    # Counting into a dictionary. This pattern is worth memorising: it is the
    # Python equivalent of GROUP BY in SQL.
    counts = {}
    for student in students:
        pathway = student["pathway"]
        # If we have not seen this pathway before, start it at 0, then add 1.
        counts[pathway] = counts.get(pathway, 0) + 1

    print("Students per pathway:")
    for pathway, count in counts.items():
        print(f"  {pathway:<25} {count}")


def main():
    print("=" * 60)
    print("LISTS AND DICTIONARIES")
    print("=" * 60)

    section_1_lists()
    section_2_dictionaries()
    section_3_list_of_dicts()

    print("\n" + "=" * 60)
    print("Your turn. Add a section_4() to this file that:")
    print("  1. Builds a list of at least 4 dictionaries about something")
    print("     you actually care about -- teams, songs, games, anything.")
    print("  2. Filters it down to a subset.")
    print("  3. Sorts that subset.")
    print("  4. Prints a total or an average.")
    print("Then call it from main() and commit your work.")
    print("=" * 60)


if __name__ == "__main__":
    main()
