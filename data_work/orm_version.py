"""
orm_version.py  --  the SAME three questions, asked through SQLAlchemy.

Unit 3. This is the twin of sql_version.py. Run both. The output must be
identical. If you can hold both files in your head at once and see how each
line corresponds, you understand what an ORM is doing -- which is exactly what
the oral check asks about.

RUN IT:
    python data_work/orm_version.py
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# func gives access to SQL functions like COUNT and SUM from Python.
from sqlalchemy import desc, func

from models import Project, Student, get_session


def question_1_students_per_pathway(session):
    """Count students on each pathway.

    THE SQL THIS REPLACES:
        SELECT COALESCE(pathway,'Not chosen'), COUNT(*)
        FROM students GROUP BY pathway ORDER BY COUNT(*) DESC;
    """
    print("\n--- 1. Students per pathway -------------------------------")

    # Build the query one step at a time. Each method returns a new query, so
    # they chain together. Still nothing has run at this point: you are writing
    # the question, not asking it.
    #
    #   .query(a, b)   the columns you want back
    #   .group_by()    bundle rows together
    #   .order_by()    sort the results
    #   .all()         NOW run it
    results = (
        session.query(
            Student.pathway,
            func.count(Student.id).label("student_count"),
        )
        .group_by(Student.pathway)
        .order_by(desc("student_count"), Student.pathway)
        .all()
    )

    # The SQL version used COALESCE to turn NULL into 'Not chosen'. SQLAlchemy
    # can do that too, but here we handle it in plain Python instead, because
    # it reads more clearly. Choosing where a job belongs -- in the database or
    # in your code -- is a real decision, and both answers are defensible.
    for pathway, student_count in results:
        display_name = pathway if pathway else "Not chosen"
        print(f"  {display_name:<25} {student_count}")


def question_2_students_with_completed_work(session):
    """List students who have completed at least one project.

    THE SQL THIS REPLACES:
        SELECT s.name, COUNT(p.id) FROM students s
        JOIN projects p ON s.id = p.student_id
        WHERE p.completed = 1 GROUP BY s.id HAVING COUNT(p.id) >= 1;
    """
    print("\n--- 2. Students with a completed project ------------------")

    results = (
        session.query(
            Student.name,
            func.count(Project.id).label("finished"),
        )
        # .join() is the ORM's JOIN. It needs no ON clause here: SQLAlchemy
        # already knows how the tables connect, because you told it once in the
        # relationship in models.py. That is the ORM earning its keep.
        .join(Project, Student.id == Project.student_id)
        # .filter() is WHERE. Note the double == for comparison; a single = is
        # assignment, and mixing them up is a classic first-year bug.
        .filter(Project.completed == True)  # noqa: E712
        .group_by(Student.id, Student.name)
        # .having() is HAVING: a filter applied AFTER grouping.
        .having(func.count(Project.id) >= 1)
        .order_by(desc("finished"), Student.name)
        .all()
    )

    for name, finished in results:
        print(f"  {name:<20} {finished} completed")


def question_3_hours_per_pathway(session):
    """Total hours spent per pathway.

    THE SQL THIS REPLACES:
        SELECT s.pathway, SUM(p.hours_spent) FROM students s
        LEFT JOIN projects p ON s.id = p.student_id GROUP BY s.pathway;
    """
    print("\n--- 3. Total hours per pathway ----------------------------")

    results = (
        session.query(
            Student.pathway,
            func.sum(Project.hours_spent).label("total_hours"),
        )
        # isouter=True turns this into a LEFT JOIN, keeping students who have
        # no projects. Drop it and Igor vanishes from the report without any
        # error at all -- which is the dangerous kind of wrong.
        .join(Project, Student.id == Project.student_id, isouter=True)
        .group_by(Student.pathway)
        .order_by(desc("total_hours"), Student.pathway)
        .all()
    )

    for pathway, total_hours in results:
        display_name = pathway if pathway else "Not chosen"
        # SUM over no rows gives None, not 0. `or 0` converts it, exactly as
        # COALESCE did in the SQL version.
        hours = total_hours or 0
        print(f"  {display_name:<25} {hours} hours")


def bonus_objects_not_rows(session):
    """Something the raw SQL version cannot do nearly as neatly.

    Raw SQL hands back tuples of values. The ORM hands back OBJECTS, with all
    their relationships attached. This is the real advantage, and it is worth
    seeing rather than being told.
    """
    print("\n--- Bonus: working with objects ---------------------------")

    # .first() returns one object, or None if there are no matches.
    student = session.query(Student).filter(Student.name == "Ana Kowalski").first()

    if student is None:
        print("  Ana is not in the database. Run setup_database.py.")
        return   # leave the function early

    print(f"  {student.name} is on the {student.pathway} pathway.")

    # student.projects: no second query written by us, no JOIN, no ids. The
    # relationship in models.py fetches them on demand.
    for project in student.projects:
        status = "done" if project.completed else "in progress"
        print(f"    - {project.title} ({project.hours_spent}h, {status})")


def main():
    print("=" * 60)
    print("SQLALCHEMY ORM VERSION")
    print("=" * 60)

    session = get_session()

    try:
        question_1_students_per_pathway(session)
        question_2_students_with_completed_work(session)
        question_3_hours_per_pathway(session)
        bonus_objects_not_rows(session)

        print("\nCompare this output with:  python data_work/sql_version.py")
        print("Questions 1-3 must match line for line.")

    finally:
        session.close()


if __name__ == "__main__":
    main()
