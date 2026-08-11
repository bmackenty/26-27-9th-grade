# DSTP Grade 9 — Course Starter Repository

**Digital Systems, Technology & Programming · American School of Warsaw**
Teacher: Mr. MacKenty · bmackenty@aswarsaw.org

Read this file **before** you read any other documentation. Everything here is
specific to our course. When Python's official docs and this README disagree
about how *our* course works, this README wins.

---

## What this repository is

A skeleton. It runs, but it does not do very much yet. Over the year you will
fill it in, break it, fix it, and make it yours.

Every file in this repository is commented far more heavily than professional
code normally is. That is deliberate. The comments are teaching material. Read
them. When you understand a comment well enough that it feels obvious, you have
learned that thing.

---

## Setup — do this once

You need Python 3.11 or higher, Git, and VS Code. If you do not have those yet,
follow the setup guide handed out in Week 1 before continuing.

### 1. Clone this repository

```bash
cd ~/Documents/grade9-design
git clone https://github.com/bmackenty/dstp-starter.git
cd dstp-starter
```

### 2. Create a virtual environment

A virtual environment is a private box of Python packages that belongs to this
project only. Without it, installing something for this course could break a
different project on your laptop.

```bash
python3 -m venv venv
```

This creates a folder called `venv`. You only do this **once**.

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

Your terminal prompt should now start with `(venv)`. You must do this **every
time** you open a new terminal window. If you forget, packages will appear to be
missing even though you installed them.

To leave the virtual environment later: `deactivate`

### 4. Install the packages this project needs

```bash
pip install -r requirements.txt
```

### 5. Check that it worked

```bash
python app.py
```

Then open http://localhost:5000 in your browser. You should see a page that says
the starter is running. Press `Control + C` in the terminal to stop the server.

---

## Every class — your daily routine

```bash
cd ~/Documents/grade9-design/dstp-starter
source venv/bin/activate      # start of session
code .                        # open VS Code
git pull                      # get any updates from the teacher
```

At the end of the session:

```bash
git add .
git commit -m "Add function that validates student age"
git push
```

Commit messages describe **what changed**. "update", "stuff", and "asdf" are not
commit messages.

---

## What is in here

| Path | What it is | When you use it |
| --- | --- | --- |
| `app.py` | A tiny Flask web application | Unit 1 (look), Unit 3 (edit) |
| `config.py` | Settings — database location, secret key | Unit 3 |
| `models.py` | SQLAlchemy models — Python classes that become database tables | Unit 3 |
| `hello.py` | Your very first program | Unit 1, Week 1 |
| `python_basics/` | Small, heavily commented example programs | Units 1–2 |
| `data_work/` | Lists, dicts, CSV files, SQL, the ORM, binary | Unit 3 |
| `data/` | Sample data and the SQL schema | Unit 3 |
| `templates/` | HTML pages that Flask fills in | Unit 3 |
| `static/` | CSS | Unit 3 |
| `tests/` | Automated tests written with pytest | Units 1–3 |
| `docs/` | AI use log template and the scope statement template | All units |

---

## Running the example programs

Each example is a normal Python file. Run one like this:

```bash
python python_basics/01_variables.py
```

**Before you run any example, predict what it will print.** Write your
prediction down. Then run it. When your prediction is wrong, that gap is the
most valuable thing in the lesson — do not skip past it.

---

## Running the tests

Tests are code that checks other code. If a test fails, something is broken.

```bash
pytest
```

For more detail about what passed and what failed:

```bash
pytest -v
```

Some tests are marked as *expected to fail* until you write the missing code.
That is normal. Your job in several exercises is to make a failing test pass.

---

## The database

By default this project uses **SQLite**, a database that lives in a single file
(`data/dstp.db`). It needs no server and no password, so it always works.

Later in Unit 3 we switch to the **school MySQL server**. Nothing in your code
has to change except one line in `config.py`. That is one of the reasons we use
SQLAlchemy — see the comments in `models.py`.

To create the database and load the sample data:

```bash
python data_work/setup_database.py
```

---

## Getting help

1. Read the error message. All of it. The last line names the problem.
2. Read the comments in the file you are working on.
3. Ask a classmate — explain your problem out loud.
4. Ask Mr. MacKenty.
5. AI, **only in the mode the current unit allows** (see `docs/AI_USE_LOG.md`).

---

## Academic honesty

Code you cannot explain is code you did not write, no matter who typed it. Every
build session in this course ends with someone asking you what your code does.
Write code you can defend.
