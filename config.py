"""
config.py  --  settings that the rest of the program reads.

Unit 3.

WHY A SEPARATE SETTINGS FILE?
Things like "where is the database" and "what port do we run on" change
depending on WHERE the program runs: your laptop, a classmate's laptop, the
school server. The interesting logic of the program does not change. Keeping
settings in one small file means you edit one place instead of hunting through
every file when something moves.

This is a habit worth learning early. Professionals call it "separating
configuration from code".
"""

import os  # os lets Python ask the operating system questions, like "where am I?"


# ---------------------------------------------------------------------------
# WHERE IS THIS PROJECT ON DISK?
#
# Hard-coding a path like "/Users/ana/Documents/dstp-starter" would break on
# every other computer. Instead we ask Python to work it out.
#
#   __file__            the path of THIS file (config.py)
#   os.path.abspath()   turn it into a full path from the root of the disk
#   os.path.dirname()   chop off the filename, leaving the folder
#
# Read that from the inside out. Nested function calls always evaluate inward
# first: the innermost brackets finish before the outer ones start.
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# os.path.join() glues path pieces together using the right separator for your
# operating system (/ on macOS and Linux, \ on Windows). Never build paths by
# gluing strings together yourself -- it breaks across machines.
DATA_DIR = os.path.join(BASE_DIR, "data")


# ---------------------------------------------------------------------------
# WHICH DATABASE?
#
# We start with SQLite: a whole database stored in a single file. No server, no
# username, no password, nothing to break. Perfect for learning.
#
# Later in Unit 3 we move to the school MySQL server. When we do, the ONLY line
# that changes is this one. Every query you wrote keeps working, because
# SQLAlchemy speaks both dialects. That is the point of an ORM, and you will be
# asked to explain it out loud.
# ---------------------------------------------------------------------------

# The "sqlite:///" prefix tells SQLAlchemy which kind of database this is.
DATABASE_URL = "sqlite:///" + os.path.join(DATA_DIR, "dstp.db")

# --- The MySQL version, for later in Unit 3 --------------------------------
# Uncomment this and comment out the line above when Mr. MacKenty gives you the
# school database credentials. The shape of the address is:
#
#   mysql+pymysql://USERNAME:PASSWORD@SERVER/DATABASE_NAME
#
# WARNING: never type a real password directly into a file you will commit.
# Passwords go in a .env file, which .gitignore already excludes. Ask in class
# when you get to this point -- do not guess.
#
# DATABASE_URL = "mysql+pymysql://student:CHANGEME@db.school.local/dstp"


# ---------------------------------------------------------------------------
# FLASK SETTINGS
# ---------------------------------------------------------------------------

# DEBUG mode does two helpful things while you are learning:
#   1. It restarts the server automatically when you save a file.
#   2. It shows the full error in the browser instead of a blank page.
# Real websites turn this OFF, because those detailed errors would tell an
# attacker far too much about how the site works.
DEBUG = True

# The port is the numbered "door" on your computer that the web server listens
# at. 5000 is Flask's usual choice. If you ever see "Address already in use",
# something else is at this door -- change the number to 5001 and try again.
PORT = 5000

# SQLAlchemy prints a warning if we do not set this. It switches off an old
# tracking feature we do not need and which uses extra memory.
SQLALCHEMY_TRACK_MODIFICATIONS = False
