import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "My first Flask application works!", "author": "Your first name"}


@app.route("/api/generate")
def generate():
    adjectives = ["Ancient", "Rusty", "Glowing", "Frozen", "Enchanted"]
    items = ["Sword", "Shield", "Staff", "Bow", "Hammer"]
    adjective = random.choice(adjectives)
    item = random.choice(items)
    result = f"{adjective} {item}"
    return {"item": result}
