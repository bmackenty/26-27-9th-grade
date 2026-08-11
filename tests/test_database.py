"""
test_database.py  --  checks that the database and the models work.

RUN THEM:
    pytest tests/test_database.py -v

WHAT IS DIFFERENT ABOUT THESE TESTS
The tests in test_helpers.py check pure functions: same input, same output,
every time. These tests need a database to exist first.

They build their OWN database in memory and throw it away afterwards, so they
never touch data/dstp.db. A test that modifies your real data is worse than no
test at all -- you would stop trusting your own data, which is a bad place to
end up.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Project, Student


# ---------------------------------------------------------------------------
# A FIXTURE
#
# A fixture is setup that runs before a test and cleans up afterwards. Any test
# that wants it just names it as an argument, and pytest supplies it.
# ---------------------------------------------------------------------------

@pytest.fixture
def session():
    """Give each test a fresh, empty, in-memory database.

    "sqlite:///:memory:" is a real SQLite database that lives in RAM and
    vanishes when the connection closes. Nothing is written to disk. It is also
    extremely fast, which matters once you have hundreds of tests.
    """
    # Setup, before the test runs.
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)     # build the tables from models.py
    TestSession = sessionmaker(bind=engine)
    db = TestSession()

    # `yield` hands the session to the test and pauses here. When the test
    # finishes, execution resumes on the next line.
    yield db

    # Teardown, after the test finishes -- even if it failed.
    db.close()


def test_can_create_a_student(session):
    """A student can be saved and read back."""
    student = Student(name="Test Student", grade_level=9, pathway="Testing")

    session.add(student)
    session.commit()      # without this, nothing is saved

    # Read it back to prove it is really there. Checking the object you just
    # created would prove nothing about the database.
    found = session.query(Student).filter(Student.name == "Test Student").first()

    assert found is not None
    assert found.grade_level == 9

    # The id was empty before the commit and the database filled it in.
    assert found.id is not None


def test_student_starts_with_no_projects(session):
    """A new student's projects list is empty, not None.

    Worth pinning down: templates and loops behave very differently for an
    empty list than for None, and this test stops that changing by accident.
    """
    student = Student(name="Solo", grade_level=9)
    session.add(student)
    session.commit()

    assert student.projects == []
    assert len(student.projects) == 0


def test_relationship_works_both_ways(session):
    """student.projects and project.student should agree."""
    student = Student(name="Linked", grade_level=9)
    project = Project(title="A project", hours_spent=5, student=student)

    session.add(student)
    session.add(project)
    session.commit()

    assert len(student.projects) == 1
    assert student.projects[0].title == "A project"
    assert project.student.name == "Linked"


def test_defaults_are_applied(session):
    """Columns with a default should fill themselves in."""
    student = Student(name="Defaults", grade_level=9)
    # hours_spent and completed are deliberately left out.
    project = Project(title="Untouched project", student=student)

    session.add(project)
    session.commit()

    assert project.hours_spent == 0
    assert project.completed is False


def test_pathway_may_be_empty(session):
    """pathway is nullable, so a student without one is still valid."""
    student = Student(name="Undecided", grade_level=9)
    session.add(student)
    session.commit()

    assert student.pathway is None


def test_deleting_a_student_deletes_their_projects(session):
    """The cascade in models.py should clean up behind itself.

    Without cascade="all, delete-orphan" the projects would survive, pointing
    at a student who no longer exists. Rows like that are called orphans, and
    they are how a database quietly fills up with data nobody can interpret.
    """
    student = Student(name="Leaving", grade_level=9)
    student.projects.append(Project(title="Project A"))
    student.projects.append(Project(title="Project B"))

    session.add(student)
    session.commit()

    assert session.query(Project).count() == 2

    session.delete(student)
    session.commit()

    assert session.query(Student).count() == 0
    assert session.query(Project).count() == 0


def test_query_counts_match(session):
    """A group-by count should agree with counting the rows by hand."""
    session.add(Student(name="A", grade_level=9, pathway="Game"))
    session.add(Student(name="B", grade_level=9, pathway="Game"))
    session.add(Student(name="C", grade_level=9, pathway="CS"))
    session.commit()

    game_count = session.query(Student).filter(Student.pathway == "Game").count()
    total = session.query(Student).count()

    assert game_count == 2
    assert total == 3
