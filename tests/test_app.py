"""
test_app.py  --  checks that the web pages load.

RUN THEM:
    pytest tests/test_app.py -v

WHAT A TEST CLIENT IS
Flask can pretend to be a browser. The test client sends a fake request
straight to your routes and hands back the response. No server runs, no network
is involved, and it takes milliseconds.

STATUS CODES -- the number a web server sends back with every response:
    200  OK, here is your page
    302  moved, go and look over there
    404  not found -- the address does not match any route
    500  the server crashed while producing the page
Recognising these on sight will save you a lot of time.
"""

import pytest

from app import app as flask_app
from models import Base, engine


@pytest.fixture
def client():
    """A fake browser for talking to the app."""
    # Testing mode gives fuller error information when something fails.
    flask_app.config["TESTING"] = True

    # Make sure the tables exist so the /students route has something to query.
    Base.metadata.create_all(engine)

    with flask_app.test_client() as test_client:
        yield test_client


def test_home_page_loads(client):
    """The home page should return 200 and mention the course."""
    response = client.get("/")

    assert response.status_code == 200

    # response.data is the raw HTML as BYTES, not text -- which is why the
    # string we look for is written b"..." rather than "...". Bytes and text
    # cannot be compared directly in Python 3, and this is where most people
    # first meet that rule.
    assert b"DSTP" in response.data


def test_students_page_loads(client):
    """The student list page should load even when the table is empty."""
    response = client.get("/students")

    assert response.status_code == 200
    assert b"Students" in response.data


def test_unknown_page_returns_404(client):
    """An address with no route should give 404, not a crash.

    Testing what happens when something goes WRONG matters as much as testing
    the happy path. Arguably more: the happy path is the bit you already tried
    by hand.
    """
    response = client.get("/this-route-does-not-exist")

    assert response.status_code == 404


def test_navigation_is_present(client):
    """Every page inherits base.html, so the nav links should be there."""
    response = client.get("/")

    assert b'href="/students"' in response.data


# ---------------------------------------------------------------------------
# A TEST WAITING FOR YOU
#
# There is a TODO in app.py asking you to add a /projects route. This test
# checks it. It is expected to fail until you write it.
#
# When your route works, this test will report XPASS -- passing unexpectedly.
# Delete the xfail line below and it becomes an ordinary test.
# ---------------------------------------------------------------------------

@pytest.mark.xfail(reason="the /projects route is not written yet -- Unit 3")
def test_projects_page_loads(client):
    response = client.get("/projects")

    assert response.status_code == 200
    assert b"Projects" in response.data
