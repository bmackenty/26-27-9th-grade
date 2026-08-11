"""
app.py  --  a very small web application.

Unit 1: run it and look at it. You are not expected to build this yet.
Unit 3: you will edit it.

WHAT A WEB APPLICATION ACTUALLY IS
When you type an address into a browser, the browser sends a REQUEST across the
network. Something at the other end receives it and sends back a RESPONSE,
usually HTML, which the browser draws on the screen.

Flask is the "something at the other end". You give Flask a rule -- "when
somebody asks for /students, run this function" -- and Flask handles all the
networking.

HOW TO RUN IT
    python app.py

Then open http://localhost:5000 in a browser.
  localhost  means "this computer"
  :5000      means "door number 5000"

Stop the server with Control + C. The terminal stays busy while the server runs;
that is not a freeze, it is the server waiting for requests. Open a second
terminal tab if you need to type other commands.
"""

from flask import Flask, render_template

import config
from models import Project, Student, create_all_tables, get_session

# ---------------------------------------------------------------------------
# CREATE THE APPLICATION
#
# __name__ is a built-in variable holding the name of the current module. Flask
# uses it to work out where this file lives, so it can find the templates/ and
# static/ folders. You do not need to understand it deeply yet -- just know
# every Flask app starts with this line.
# ---------------------------------------------------------------------------
app = Flask(__name__)


# ---------------------------------------------------------------------------
# ROUTES
#
# A route connects a WEB ADDRESS to a PYTHON FUNCTION.
#
# The line starting with @ is a DECORATOR. It sits directly above a function
# and changes what happens to it. Here it tells Flask: "register the function
# below as the handler for this address."
#
# The decorator must be immediately above the function. A blank line is fine;
# anything else is not.
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """The home page. "/" is the address with nothing after it."""

    # render_template() finds the file in templates/, fills in any placeholders
    # with the values we pass, and returns the finished HTML as a string.
    # Whatever a route function RETURNS is what the browser receives.
    return render_template(
        "index.html",
        # Everything after this point is data being handed to the template.
        # On the left is the name the template will use; on the right is the
        # Python value. They are allowed to differ, but keeping them the same
        # saves confusion.
        title="DSTP Starter",
        message="Your starter repository is running.",
    )


@app.route("/students")
def student_list():
    """A page listing every student in the database.

    This is the route you will extend in Unit 3.
    """
    # Open a workspace onto the database.
    session = get_session()

    try:
        # THE ORM QUERY.
        #   query(Student)   which table
        #   .order_by(...)   sort by name, A to Z
        #   .all()           actually run it, give me a list
        #
        # Nothing happens until .all() is called. Up to that point you are only
        # describing a question. Forgetting .all() is a common bug: you get back
        # a query object instead of your data.
        #
        # The SQL SQLAlchemy writes for this is:
        #   SELECT * FROM students ORDER BY name;
        students = session.query(Student).order_by(Student.name).all()

        return render_template(
            "students.html",
            title="Students",
            students=students,
        )
    finally:
        # A "finally" block runs whether or not something went wrong above.
        # Closing the session releases the connection. Leave enough of them
        # open and the database eventually refuses to talk to you.
        session.close()


# ---------------------------------------------------------------------------
# TODO (Unit 3): add a route at "/projects" that lists every project.
#
# Steps:
#   1. Copy the student_list function below this comment and rename it.
#   2. Change the decorator address to "/projects".
#   3. Query Project instead of Student.
#   4. Create templates/projects.html, modelled on students.html.
#   5. Run it, open http://localhost:5000/projects, and check it.
#
# There is a test waiting for you in tests/test_app.py that will pass once this
# works. Run it with:  pytest tests/test_app.py
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# STARTING THE SERVER
#
# This strange-looking if statement means: "only run the code below when this
# file is executed directly, not when another file imports it."
#
# Why it matters: the tests import app.py to inspect the routes. Without this
# guard, importing it would launch a web server and the tests would hang
# forever. You will meet this line in almost every Python program you read.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Make sure the tables exist before serving any pages.
    create_all_tables()

    print("Starting the DSTP starter app...")
    print(f"Open http://localhost:{config.PORT} in your browser.")
    print("Press Control + C to stop.")

    app.run(debug=config.DEBUG, port=config.PORT)
