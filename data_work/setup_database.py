"""
setup_database.py  --  build the database and fill it with the sample data.

Unit 3.

RUN IT FROM THE PROJECT FOLDER (not from inside data_work/):
    python data_work/setup_database.py

WHAT IT DOES
  1. Creates data/dstp.db if it does not exist.
  2. Creates the students and projects tables.
  3. Reads data/students.csv and data/projects.csv.
  4. Inserts every row.

SAFE TO RUN AGAIN
It empties the tables first, so running it twice does not give you twenty
students. If you ever mangle your database beyond repair -- and you will, at
least once -- delete data/dstp.db and run this again. That is exactly why
throwaway practice data exists.
"""

import csv       # reads and writes CSV files. Part of Python, no install needed.
import os
import sys

# --- Making imports work from the folder above -----------------------------
# This file lives in data_work/, but models.py lives one level up. Python does
# not look upward by default, so we add the parent folder to its search path.
# You do not need to memorise this. It is here so the file actually runs, and
# because someone always asks what these two lines are.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from models import Project, Student, create_all_tables, get_session


def load_students(session):
    """Read students.csv and insert one Student per row.

    The argument `session` is the database workspace, passed in by main(). A
    function that receives what it needs is far easier to test than one that
    reaches out and grabs things for itself.
    """
    path = os.path.join(config.DATA_DIR, "students.csv")

    # "with open(...) as f" opens the file and guarantees it is closed again,
    # even if something fails partway through. Always open files this way.
    #   "r"                read mode
    #   newline=""         the csv module asks for this; it prevents blank rows
    #   encoding="utf-8"   how the text is stored. Matters for names with
    #                      accents -- Wiśniewski, for instance.
    with open(path, "r", newline="", encoding="utf-8") as f:

        # DictReader treats the first line as column headings and gives each
        # following row back as a dictionary:
        #   {"name": "Ana Kowalski", "grade_level": "9", "pathway": "..."}
        # Much safer than remembering that name is at index 0.
        reader = csv.DictReader(f)

        count = 0
        for row in reader:

            # EVERYTHING FROM A CSV FILE IS TEXT. Always. "9" is a string, not
            # the number 9. int() converts it. Forget this conversion and your
            # sums will do something baffling: "9" + "9" is "99".
            grade = int(row["grade_level"])

            # An empty cell arrives as an empty string "". We want None
            # instead, because the database understands None as "no value".
            # The `or None` trick works because Python treats "" as false.
            pathway = row["pathway"].strip() or None

            # Create the object. This is just a Python object so far -- nothing
            # has touched the database yet.
            student = Student(
                name=row["name"].strip(),
                grade_level=grade,
                pathway=pathway,
            )

            # Put it in the session's to-do list. Still not saved.
            session.add(student)
            count += 1

    print(f"  Prepared {count} students.")


def load_projects(session):
    """Read projects.csv and insert one Project per row.

    Harder than students, because the CSV names each student in words but the
    database links by id number. So we look each student up first.
    """
    path = os.path.join(config.DATA_DIR, "projects.csv")

    # --- Build a lookup table --------------------------------------------
    # A dictionary mapping name -> Student object. Querying the database once
    # per project row would work, but it means one round trip per row. One
    # query and a dictionary is faster and shows you a pattern worth keeping.
    all_students = session.query(Student).all()
    students_by_name = {s.name: s for s in all_students}
    # The line above is a DICTIONARY COMPREHENSION. Long form:
    #   students_by_name = {}
    #   for s in all_students:
    #       students_by_name[s.name] = s

    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        count = 0
        skipped = 0
        for row in reader:
            student_name = row["student_name"].strip()

            # .get() returns None instead of crashing when the key is missing.
            # Real data always contains a typo somewhere. Plan for it.
            student = students_by_name.get(student_name)

            if student is None:
                # Say something. A program that skips bad rows in silence is a
                # program that will lie to you later.
                print(f"  WARNING: no student named {student_name!r}; row skipped.")
                skipped += 1
                continue  # jump to the next row of the loop

            # CSV has no idea what True and False are -- it stores "true" as
            # text. Compare in lowercase so "True", "TRUE", and "true" all work.
            completed = row["completed"].strip().lower() == "true"

            project = Project(
                # Assigning the object, not the id. SQLAlchemy works out the
                # student_id for us. This is the relationship in models.py
                # doing its job.
                student=student,
                title=row["title"].strip(),
                hours_spent=int(row["hours_spent"]),
                completed=completed,
            )
            session.add(project)
            count += 1

    print(f"  Prepared {count} projects ({skipped} skipped).")


def main():
    """Do the whole job, in order."""
    print("Setting up the DSTP database...")
    print(f"  Database location: {config.DATABASE_URL}")

    # Step 1: make sure the tables exist.
    create_all_tables()
    print("  Tables created (or already present).")

    session = get_session()

    try:
        # Step 2: empty the tables so re-running does not duplicate everything.
        # Projects first: they point at students, and the database will not let
        # you delete a row something else depends on.
        session.query(Project).delete()
        session.query(Student).delete()
        session.commit()
        print("  Existing rows cleared.")

        # Step 3: load the data.
        load_students(session)

        # Commit the students BEFORE loading projects, so that each student has
        # a real id for the projects to point at.
        session.commit()

        load_projects(session)

        # THE COMMIT. Everything added above is written to disk here. Without
        # this line the script runs perfectly, prints cheerful messages, and
        # saves absolutely nothing.
        session.commit()

        # Step 4: prove it worked by counting what is actually in there.
        student_count = session.query(Student).count()
        project_count = session.query(Project).count()
        print(f"\nDone. Database now holds {student_count} students "
              f"and {project_count} projects.")
        print("Check it with:  python data_work/orm_version.py")

    except Exception as error:
        # If ANYTHING went wrong, undo every change made in this session.
        # A rollback means you end up with the old data rather than half the
        # new data, and half-loaded data is much worse than none.
        session.rollback()
        print(f"\nSomething went wrong, so no changes were saved:\n  {error}")
        raise   # re-raise so you still see the full error and can debug it

    finally:
        session.close()


# Only run main() when this file is executed directly.
if __name__ == "__main__":
    main()
