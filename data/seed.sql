-- ===========================================================================
-- seed.sql  --  sample data to put into the empty tables.
-- ===========================================================================
--
-- "Seeding" a database means loading starter data into it. Useful because an
-- empty database makes it very hard to tell a working query from a broken one:
-- both return nothing.
--
-- These names are invented. Any resemblance to actual Grade 9 students is
-- entirely intentional and entirely fictional at the same time.
--
-- RUN THIS AFTER schema.sql:
--     sqlite3 data/dstp.db < data/seed.sql
-- ===========================================================================


-- --- Students ---------------------------------------------------------------
-- INSERT INTO table (columns...) VALUES (row), (row), (row);
--
-- Text goes in single quotes. Numbers do not. NULL, with no quotes, means "no
-- value at all" -- which is different from an empty string '': the first says
-- we do not know, the second says we know it is blank.
--
-- We do not list id, because the database generates it automatically.
INSERT INTO students (name, grade_level, pathway) VALUES
    ('Ana Kowalski',     9, 'Game Programming'),
    ('Ben Nowak',        9, 'Computer Science'),
    ('Chidi Okafor',     9, 'Computational Biology'),
    ('Dasha Volkova',    9, 'Computing in Business'),
    ('Elias Hart',       9, 'Practical Computing'),
    ('Fatima Rahman',    9, 'Game Programming'),
    ('Gustav Lind',      9, 'Computer Science'),
    ('Hana Suzuki',      9, 'Computational Biology'),
    ('Igor Wisniewski',  9, NULL),
    ('Julia Santos',     9, 'Computing in Business');


-- --- Projects ---------------------------------------------------------------
-- student_id numbers refer to the students above, in the order they were
-- inserted: Ana is 1, Ben is 2, and so on.
--
-- Writing ids by hand like this is fine for ten rows of practice data and a
-- terrible idea for anything real -- one row inserted out of order and every
-- link is silently wrong. data_work/setup_database.py does it properly, by
-- looking each student up by name.
INSERT INTO projects (student_id, title, hours_spent, completed) VALUES
    (1,  'Maze escape game',           14, 1),
    (1,  'Score tracker add-on',        6, 0),
    (2,  'Sorting visualiser',         11, 1),
    (2,  'Binary search practice tool',  4, 0),
    (3,  'Plant growth data logger',    9, 1),
    (4,  'Canteen sales analyser',     12, 1),
    (5,  'File renaming automator',     7, 1),
    (6,  'Two-player quiz game',       15, 0),
    (7,  'Password strength checker',   5, 1),
    (8,  'DNA sequence counter',       10, 0),
    (10, 'Budget planner',              8, 1);

-- Note that Igor (id 9) has no projects at all. Sample data should always
-- include the awkward cases -- the empty one, the missing one, the one with
-- too many. Data that is uniformly tidy hides the bugs you most want to find.
