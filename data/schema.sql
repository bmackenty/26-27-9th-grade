-- ===========================================================================
-- schema.sql  --  the shape of our database, written in plain SQL.
-- ===========================================================================
--
-- In SQL, a comment starts with two dashes. Not #, not //. Two dashes.
--
-- WHY THIS FILE EXISTS WHEN models.py ALREADY DEFINES THE TABLES
-- models.py describes these same tables in Python, and SQLAlchemy generates
-- SQL very much like this from it. This file is what that generated SQL looks
-- like. Read both. Being able to move between them in either direction is a
-- Unit 3 objective and it will be checked out loud.
--
-- HOW TO RUN IT BY HAND (optional -- setup_database.py does this for you)
--     sqlite3 data/dstp.db < data/schema.sql
--
-- SQL keywords are conventionally written in capitals. The database does not
-- care, but it makes queries far easier to skim.
-- ===========================================================================


-- Delete the tables if they already exist, so this file can be run repeatedly
-- without errors. Order matters: projects points at students, so projects must
-- go first. The database will refuse to delete a table another one depends on.
--
-- DROP TABLE destroys the table AND everything in it, with no confirmation and
-- no undo. Harmless here on practice data. Treat it with real fear elsewhere.
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS students;


-- --- The students table -----------------------------------------------------
CREATE TABLE students (
    -- Each line describes one column: name, type, then any rules.
    id           INTEGER PRIMARY KEY AUTOINCREMENT,

    -- NOT NULL means this may never be empty.
    name         VARCHAR(100) NOT NULL,
    grade_level  INTEGER NOT NULL,

    -- No NOT NULL here, so this column is allowed to be empty. A student who
    -- has not chosen a pathway yet is still a real student.
    pathway      VARCHAR(50)
);


-- --- The projects table -----------------------------------------------------
CREATE TABLE projects (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,

    -- This column holds the id of a row in the students table.
    student_id   INTEGER NOT NULL,

    title        VARCHAR(200) NOT NULL,

    -- DEFAULT fills in a value when nobody supplies one.
    hours_spent  INTEGER DEFAULT 0,

    -- SQLite has no true boolean type. It stores 0 for false and 1 for true.
    -- Other databases, MySQL included, handle this differently. Small
    -- differences like this are exactly why an ORM is useful.
    completed    INTEGER DEFAULT 0,

    -- THE FOREIGN KEY.
    -- This tells the database that student_id must match some students.id.
    -- Try to insert a project for student 999 when no student 999 exists and
    -- the database refuses. That refusal is a feature: it makes impossible
    -- data actually impossible, rather than merely unlikely.
    FOREIGN KEY (student_id) REFERENCES students(id)
);


-- --- An index ---------------------------------------------------------------
-- An index is like the index at the back of a textbook: instead of reading
-- every page to find a word, you look it up. Here it makes "find all projects
-- belonging to student 4" fast.
--
-- Indexes cost disk space and slow down writing slightly, so you add them for
-- lookups you do often -- not for every column out of habit.
CREATE INDEX idx_projects_student_id ON projects(student_id);
