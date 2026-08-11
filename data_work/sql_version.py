"""
sql_version.py  --  answer a question about the data using raw SQL.

Unit 3. Read this file and orm_version.py side by side. They ask the database
exactly the same questions in two different ways and must print identical
answers. Proving that to yourself is the point of the exercise.

RUN IT:
    python data_work/sql_version.py

THE QUESTIONS
  1. How many students are on each pathway?
  2. Which students have finished at least one project?
  3. What is the total number of hours spent per pathway?
"""

import os
import sqlite3   # part of Python. Talks to SQLite directly, with no ORM.
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


def get_connection():
    """Open a direct connection to the SQLite file.

    No SQLAlchemy here on purpose. This is the raw, underneath version: you
    write SQL as a string, hand it over, and get tuples back.
    """
    # config.DATABASE_URL starts with "sqlite:///" which sqlite3 does not
    # understand, so we strip that prefix off to leave a plain file path.
    db_path = config.DATABASE_URL.replace("sqlite:///", "")

    if not os.path.exists(db_path):
        # Fail early with a message a human can act on. Compare that to the
        # unhelpful error sqlite3 would produce on its own.
        raise FileNotFoundError(
            f"No database at {db_path}.\n"
            "Run this first:  python data_work/setup_database.py"
        )

    return sqlite3.connect(db_path)


def question_1_students_per_pathway(cursor):
    """Count students on each pathway.

    A CURSOR is the thing that carries a query to the database and holds the
    results on the way back. You get one from a connection.
    """
    print("\n--- 1. Students per pathway -------------------------------")

    # Triple quotes let a string run across several lines, which keeps SQL
    # readable instead of squashed onto one enormous line.
    #
    # Reading this query in the order the database actually does it:
    #   FROM students        start with the students table
    #   GROUP BY pathway     bundle rows together by pathway
    #   COUNT(*)             count the rows in each bundle
    #   ORDER BY ... DESC    biggest bundle first
    #
    # COALESCE(pathway, 'Not chosen') means "use pathway, unless it is NULL, in
    # which case use 'Not chosen'". Igor has no pathway, and without this his
    # group would appear as a blank.
    sql = """
        SELECT COALESCE(pathway, 'Not chosen') AS pathway_name,
               COUNT(*) AS student_count
        FROM students
        GROUP BY pathway
        ORDER BY student_count DESC, pathway_name;
    """

    cursor.execute(sql)          # send the query
    rows = cursor.fetchall()     # collect every result row

    # Each row is a TUPLE: (pathway_name, student_count). A tuple is like a
    # list that cannot be changed. Unpack it into two names in the for line.
    for pathway_name, student_count in rows:
        # :<25 pads the name to 25 characters so the numbers line up. Small
        # formatting touches make output you can actually check by eye.
        print(f"  {pathway_name:<25} {student_count}")


def question_2_students_with_completed_work(cursor):
    """List students who have completed at least one project."""
    print("\n--- 2. Students with a completed project ------------------")

    # A JOIN combines rows from two tables using the link between them.
    # "ON s.id = p.student_id" is the link: match each student to their own
    # projects. Leave out the ON and the database pairs every student with
    # every project, which produces nonsense confidently.
    #
    # s and p are ALIASES -- short nicknames for the tables, so we can write
    # s.name instead of students.name.
    #
    # WHERE filters individual rows BEFORE grouping.
    # HAVING filters groups AFTER grouping. That distinction is examinable.
    sql = """
        SELECT s.name,
               COUNT(p.id) AS finished
        FROM students AS s
        JOIN projects AS p ON s.id = p.student_id
        WHERE p.completed = 1
        GROUP BY s.id, s.name
        HAVING finished >= 1
        ORDER BY finished DESC, s.name;
    """

    cursor.execute(sql)
    for name, finished in cursor.fetchall():
        print(f"  {name:<20} {finished} completed")


def question_3_hours_per_pathway(cursor):
    """Total hours spent per pathway."""
    print("\n--- 3. Total hours per pathway ----------------------------")

    # SUM() adds up a column across a group, the way COUNT() counts it.
    #
    # LEFT JOIN, not JOIN: a LEFT JOIN keeps every student even when they have
    # no matching project. A plain JOIN would silently drop Igor, and a report
    # that quietly loses people is worse than one that is obviously broken.
    # Their total comes out as 0 thanks to the COALESCE.
    sql = """
        SELECT COALESCE(s.pathway, 'Not chosen') AS pathway_name,
               COALESCE(SUM(p.hours_spent), 0) AS total_hours
        FROM students AS s
        LEFT JOIN projects AS p ON s.id = p.student_id
        GROUP BY s.pathway
        ORDER BY total_hours DESC, pathway_name;
    """

    cursor.execute(sql)
    for pathway_name, total_hours in cursor.fetchall():
        print(f"  {pathway_name:<25} {total_hours} hours")


def main():
    print("=" * 60)
    print("RAW SQL VERSION")
    print("=" * 60)

    connection = get_connection()

    try:
        cursor = connection.cursor()

        question_1_students_per_pathway(cursor)
        question_2_students_with_completed_work(cursor)
        question_3_hours_per_pathway(cursor)

        print("\nNow run:  python data_work/orm_version.py")
        print("The numbers must match exactly. If they do not, one of them is")
        print("wrong, and finding out which is the actual exercise.")

    finally:
        # Close the connection whatever happens.
        connection.close()


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# A WARNING WORTH TAKING SERIOUSLY: NEVER BUILD SQL BY GLUING STRINGS
#
# Suppose you wanted to search by name, and wrote:
#
#     name = input("Name: ")
#     cursor.execute("SELECT * FROM students WHERE name = '" + name + "'")
#
# Someone types:   '; DROP TABLE students; --
# and your whole table is gone. This is called SQL injection, and it is still
# one of the most common ways real systems are broken into.
#
# The fix is easy. Use a placeholder and let the library handle the value:
#
#     cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
#
# The ? is filled in safely: whatever the user typed is treated as a value, not
# as SQL to run. Do it this way every single time, including when you are sure
# the input is safe.
# ---------------------------------------------------------------------------
