# Troubleshooting

Work down this list before asking. Not because asking is discouraged — it is
not — but because you will diagnose most of these yourself in under a minute
once you know where to look, and that skill is worth more than the answer.

---

## First, always

**Read the error message. All of it.** The last line names the problem. The
lines above it show the path the program took to get there. Most beginners
scroll past the error to look for someone to ask; the error was the answer.

---

## `command not found: python`

Try `python3` instead. On macOS, plain `python` often does not exist.

## `ModuleNotFoundError: No module named 'flask'`

Almost always the virtual environment is not active. Check your prompt for
`(venv)`. If it is missing:

```bash
source venv/bin/activate
```

If it is there and the error persists, install the packages:

```bash
pip install -r requirements.txt
```

## `Address already in use` when running `app.py`

Something is already using port 5000 — usually a copy of the app you forgot to
stop. Either press `Control + C` in the other terminal tab, or change `PORT` in
`config.py` to 5001.

## The web page does not update when I edit the file

- Did you save? (`Command + S`)
- Did you refresh the browser? (`Command + R`)
- Is `DEBUG = True` in `config.py`? Without it the server does not restart.
- For CSS specifically, try a hard refresh: `Command + Shift + R`.

## `sqlite3.OperationalError: no such table`

The database has not been built yet:

```bash
python data_work/setup_database.py
```

## The database has wrong or duplicated data

Delete it and rebuild. It is practice data; nothing of yours is lost.

```bash
rm data/dstp.db
python data_work/setup_database.py
```

## `IndentationError` or `TabError`

Python uses indentation as grammar. Mixing tabs and spaces breaks it, even when
the two look identical on screen. In VS Code, click "Spaces: 4" in the bottom
bar and choose **Convert Indentation to Spaces**.

## `TypeError: can only concatenate str (not "int") to str`

You are adding text to a number. Convert first: `int(value)` or `str(value)`.
Anything read from a CSV file or from `input()` is text, always.

## My changes are not on GitHub

Run the three commands in order, and check for errors after each:

```bash
git status      # what has changed
git add .
git commit -m "A message that describes what changed"
git push
```

Then open the repository in a browser and look. "I pushed it" and "it is on
GitHub" are different claims.

## `pytest` says it cannot import my module

Run pytest from the **project folder**, not from inside `tests/`:

```bash
cd ~/Documents/grade9-design/dstp-starter
pytest
```

## Everything is broken and I do not know what I changed

```bash
git diff        # every change since your last commit
git stash       # put those changes aside temporarily
git stash pop   # bring them back
```

This is exactly why we commit often. A commit you can return to is worth more
than an hour of careful work you cannot undo.

---

## Still stuck?

Before asking, be ready to say:

1. What you expected to happen.
2. What actually happened, including the **exact** error text.
3. What you have already tried.

Working that out is usually where the answer turns up anyway.

---

## `TypeError: Can't replace canonical symbol for '__firstlineno__'`

This appears the moment SQLAlchemy is imported, and the traceback is long and
alarming. It is not your code.

Python 3.13 added a hidden attribute called `__firstlineno__` to every class.
Older versions of SQLAlchemy did not expect it and crash on import. Your Python
is newer than your library.

**Fix — upgrade the packages:**

```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
python app.py
```

**If it still fails — rebuild on Python 3.11:**

```bash
deactivate
rm -rf venv
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Check which Python your environment is actually using at any time with:

```bash
python --version
```

**Worth noticing:** the traceback names every file it passed through on the way
to the error, ending with the one that actually failed —
`sqlalchemy/util/langhelpers.py`. None of those paths are in your project
folder. When every file in a traceback lives inside `venv/`, the problem is the
environment, not your code. That single observation will save you a lot of time
this year.
