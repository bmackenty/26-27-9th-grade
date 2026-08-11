"""
models.py  --  Python classes that describe database tables.

Unit 3.

THE BIG IDEA
A database stores rows in tables. Python works with objects. Something has to
translate between the two, and writing that translation by hand is tedious and
easy to get wrong.

SQLAlchemy is an ORM: an Object-Relational Mapper. You describe your tables as
Python classes, once, here. After that you write Python -- and SQLAlchemy
writes the SQL for you.

You still need to know SQL. An ORM that you cannot see through is a magic box,
and magic boxes are impossible to debug. In this unit you will write the same
query BOTH ways (data_work/sql_version.py and data_work/orm_version.py) and
prove they return identical results.

THE TWO TABLES IN THIS STARTER

    students                      projects
    --------                      --------
    id          <-------------+   id
    name                      |   student_id  ---+ points back at students.id
    grade_level               +---
    pathway                       title
                                  hours_spent
                                  completed

One student has many projects. Each project belongs to exactly one student.
That is called a one-to-many relationship, and it is the most common shape in
all of database design.
"""

# --- Imports ---------------------------------------------------------------
# An import brings code from somewhere else into this file. Nothing here was
# written by us: it all comes from the SQLAlchemy package we installed with pip.
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

import config  # our own settings file, sitting next to this one


# ---------------------------------------------------------------------------
# THE BASE CLASS
#
# Every model class below inherits from Base. Inheriting means "start with
# everything Base can do, then add my own details". Base is what allows
# SQLAlchemy to collect all our table definitions in one place.
# ---------------------------------------------------------------------------
Base = declarative_base()


class Student(Base):
    """One student. One row in the students table.

    A class is a blueprint. This class is not a student -- it describes what
    any student has. Individual students are created from it later:

        ana = Student(name="Ana", grade_level=9, pathway="Game Programming")
    """

    # __tablename__ is the actual name of the table inside the database.
    # By convention it is plural and lowercase. SQLAlchemy requires it.
    __tablename__ = "students"

    # --- Columns -----------------------------------------------------------
    # Each Column() below becomes a column in the table. The first argument is
    # the TYPE of data allowed in it. A database is strict about types in a way
    # Python normally is not: put text in an Integer column and it complains.

    # primary_key=True means this column uniquely identifies the row. No two
    # students can share an id, and the database fills it in automatically
    # (1, 2, 3, ...) so you never have to invent one.
    id = Column(Integer, primary_key=True)

    # String(100) means text, at most 100 characters.
    # nullable=False means this column may never be empty. Deciding what is
    # allowed to be missing is a real design decision, not a technicality: a
    # student without a name is not a student.
    name = Column(String(100), nullable=False)

    grade_level = Column(Integer, nullable=False)

    # nullable=True (the default) means this MAY be empty -- a student who has
    # not chosen a pathway yet is still a valid student.
    pathway = Column(String(50), nullable=True)

    # --- Relationship ------------------------------------------------------
    # This is NOT a column. No "projects" column exists in the students table.
    # It is a convenience SQLAlchemy gives you: ana.projects hands you a list of
    # that student's Project objects, fetching them from the other table for you.
    #
    #   back_populates  keeps both sides in step, so project.student works too.
    #   cascade         if a student is deleted, delete their projects as well,
    #                   instead of leaving orphan rows pointing at nobody.
    projects = relationship(
        "Project",
        back_populates="student",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        """What Python prints when you print() a Student.

        Without this you would see something useless like
        <models.Student object at 0x104f2b9d0>. With it you see the actual data.
        Worth adding to every model you ever write -- it pays for itself the
        first time you debug.
        """
        return f"<Student id={self.id} name={self.name!r} pathway={self.pathway!r}>"


class Project(Base):
    """One project belonging to one student."""

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)

    # --- The foreign key ---------------------------------------------------
    # This is the link between the two tables. It stores the id of a row in the
    # students table. ForeignKey tells the database to REFUSE a project whose
    # student_id does not match a real student. That guarantee is one of the
    # main reasons to use a database instead of a pile of files.
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    title = Column(String(200), nullable=False)

    # default=0 means: if nobody supplies a value, use 0.
    hours_spent = Column(Integer, default=0)

    # Boolean is True or False. Behind the scenes SQLite stores it as 1 or 0.
    completed = Column(Boolean, default=False)

    # The other end of the relationship declared in Student.
    student = relationship("Student", back_populates="projects")

    def __repr__(self):
        return f"<Project id={self.id} title={self.title!r} completed={self.completed}>"


# ---------------------------------------------------------------------------
# ENGINE AND SESSION -- how Python actually reaches the database
#
# ENGINE  the connection to the database. Created once, reused everywhere.
#         It knows the address from config.DATABASE_URL, which is why swapping
#         SQLite for MySQL touches no code in this file.
#
# SESSION your workspace. You add objects to it, change them, then commit.
#         Nothing is written to disk until you call session.commit(). If you
#         forget to commit, your work quietly disappears -- this catches
#         everybody at least once, so remember where to look when data vanishes.
# ---------------------------------------------------------------------------
engine = create_engine(config.DATABASE_URL, echo=False)

# Change echo=False to echo=True above and SQLAlchemy will print every SQL
# statement it generates. Do this at least once. Watching your Python turn into
# SQL in real time is the fastest way to understand what an ORM actually does.

SessionLocal = sessionmaker(bind=engine)


def get_session():
    """Hand back a new session to work with.

    Wrapping this in a function means the rest of the program does not need to
    know how sessions are made. If we change how they work, we change it here,
    once.
    """
    return SessionLocal()


def create_all_tables():
    """Create every table described in this file, if it does not already exist.

    Safe to run repeatedly: existing tables are left alone. It will NOT update
    a table whose columns you have since changed -- for that, delete
    data/dstp.db and rebuild. Losing your data that way is fine here and very
    much not fine in real life, which is a conversation for another day.
    """
    Base.metadata.create_all(engine)
