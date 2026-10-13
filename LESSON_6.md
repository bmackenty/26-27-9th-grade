# Lesson 6: Send a choice to Python

**Suggested time: 60 minutes. Work at your own pace.**

Last lesson, your nickname and colour choice changed your result card in the browser. Today, you will choose **Sword**, **Shield**, or **Staff** and send that choice to Python. Python will use it to generate the correct type of item.

Example: choose **Shield**, then click **Forge my item**. You might receive **Glowing Shield**. You should never receive a Sword or Staff when Shield is selected.

## How to use this lesson

1. Complete the steps in order. Do not skip a checkpoint.
2. Save the file before testing it.
3. Only copy code inside the code blocks. Do not copy the backticks around them.
4. If a checkpoint fails, use its help before continuing.
5. In lesson6_notes.txt, record the last checkpoint you passed. If time runs out, write the step to resume next lesson.

The times are suggestions. It is better to finish fewer steps with understanding than to rush through a broken application. Extensions are optional.

## Your goal

By the end, you should be able to:
- Add a labelled dropdown to a form.
- Send its value to Flask using a URL query parameter.
- Read that value in Python.
- Use a conditional to choose the correct output.
- Explain why Python checks that the choice is valid.

## Step 1: Check your starting point — about 8 minutes

**File: your existing project. No code changes yet.**

**1.1** Open your my_first_web_app folder in VS Code. 

**1.3** Start Flask:
```bash
python -m flask --app app run --debug
```

Leave this terminal running. If Flask is already running correctly, do not start a second copy. If you use port 5001, add --port 5001 and use 5001 in every address below.

**1.4** Open http://127.0.0.1:5000/static/index.html. Use this address, not Live Server, GitHub Pages, or a file:/// address.

**1.5** Enter the invented nickname StarFox, choose Fire orange, and submit.

**Checkpoint 1 — pass when:** the card becomes orange and displays a nickname and generated item.

**If it fails:** use the [README recovery instructions](README.md) to copy the four completed Lesson 5 files. Keep your existing .venv. Test again. Ask for help if it still fails. Do not continue with a broken starting point.

## Step 2: Understand the new request — about 4 minutes

Today you will send a request such as:

```text
/api/generate?category=shield
```

| Part | Meaning |
|---|---|
| /api/generate | The Flask route we already use |
| ? | Begins the query string |
| category | The name of the value we are sending |
| shield | The selected value |

We call category=shield a **query parameter**. It is information added to the request URL.

The route in Python stays **/api/generate**. Do not put ?category=shield in the @app.route line.

**2.1** In lesson6_notes.txt, predict what /api/generate?category=staff should produce once we finish the Python code.

**Checkpoint 2 — pass when:** you can identify the parameter name and its value.

## Step 3: Teach Python to read the category — about 12 minutes

**File: app.py. Replace the whole file in this step.**

We will use a complete small file so everyone has the same starting behaviour. Keep your earlier personal version in your backup.

**3.1** Open app.py. Select all its code and replace it with the following. Do not paste this underneath your old code.

```python
import random
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "My first Flask application works!", "author": "Your first name"}


@app.route("/api/generate")
def generate():
    category = request.args.get("category", "sword")

    if category == "sword":
        item_type = "Sword"
    elif category == "shield":
        item_type = "Shield"
    elif category == "staff":
        item_type = "Staff"
    else:
        return {"error": "Choose sword, shield, or staff."}, 400

    adjectives = ["Ancient", "Rusty", "Glowing", "Frozen", "Enchanted"]
    adjective = random.choice(adjectives)
    result = f"{adjective} {item_type}"

    return {"item": result, "category": category}

```

The same code is available in [01-replace-app.py](lesson-6-snippets/01-replace-app.py).

**3.2** Save app.py. Check the Flask terminal for errors.

**3.3** Read these explanations:

| Code | What it does |
|---|---|
| from flask import Flask, request | Imports request so we can read information sent by the browser |
| request.args.get("category", "sword") | Reads category from the query string; uses sword if the parameter is missing |
| if / elif | Matches the supplied value to an allowed category |
| else | Handles values that do not match any allowed category |
| return {"error": ...}, 400 | Returns a JSON error with HTTP status 400, meaning a bad request |
| return {"item": result, "category": category} | Sends the generated item and the accepted category back as JSON |

The adjective is still random. The item type now comes from the user's choice. Use the lowercase values sword, shield, and staff exactly as shown.

**3.4** Open a **second browser tab** and visit:

http://127.0.0.1:5000/api/generate?category=shield

You should see JSON like:
```json
{"item": "Glowing Shield", "category": "shield"}
```

The adjective and the order of the keys can differ.

**3.5** Change shield to staff in the address. Press Enter. Repeat with sword.

**Checkpoint 3 — pass when:** each address returns its requested item type. Refreshing can change the adjective, but not the chosen type.

**If it fails:** if you see SyntaxError or IndentationError, compare your entire app.py with the supplied file. If the response still ignores category, check that you saved the correct app.py and that Flask restarted. Changing the URL alone cannot update old Python code.

## Step 4: Check invalid input — about 6 minutes

**File: none. Test using the address bar.**

**4.1** Predict the result of this request, then visit it:

http://127.0.0.1:5000/api/generate?category=banana

Expected JSON:
```json
{"error": "Choose sword, shield, or staff."}
```

The browser may simply display this JSON. It does not have to display the number 400 on the page.

**4.2** Visit the address without a category:

http://127.0.0.1:5000/api/generate

You should receive a Sword. The default only applies when the parameter is missing. An explicitly empty value, ?category=, is invalid.

**4.3** Answer in your notes: Why must Python check the category even though our dropdown will only offer three choices?

Hint: you just sent banana without using a dropdown.

**Checkpoint 4 — pass when:** banana returns an error and a missing category uses sword. This is **server-side validation**: checking the input in Python before using it.

## Step 5: Add the dropdown — about 8 minutes

**File: static/index.html. Add one block; do not replace the whole file.**

**5.1** Find your existing submit button:
```html
<button type="submit" id="generate-button">Forge my item</button>
```

Your button text may be personalised. Look for id="generate-button".

**5.2** Immediately **above that button**, inside <form id="generator-form">, add:

```html
    <label for="category">Item category</label>
    <select id="category" name="category">
        <option value="sword">Sword</option>
        <option value="shield">Shield</option>
        <option value="staff">Staff</option>
    </select>

```

The same block is in [02-category-control.html](lesson-6-snippets/02-category-control.html).

**5.3** Save index.html. Return to your application tab at /static/index.html and refresh.

**5.4** Check that you can choose Sword, Shield, and Staff. Click the Item category label; it should focus the dropdown.

The visible word Shield is for the user. The value "shield" is what we will send to Python. The label's for attribute matches the select element's id.

**Checkpoint 5 — pass when:** your existing form contains one new labelled dropdown. It should use your existing styling automatically.

**Expected at this point:** submitting still requests the default Sword, even if you choose Shield. We have not connected the new dropdown to JavaScript yet.

**If the dropdown is missing:** check that you saved static/index.html, placed the block inside the form, and refreshed the application tab rather than the JSON tab.

## Step 6: Send the selected value — about 12 minutes

**File: static/script.js. Make exactly three edits.**

### Edit A: Find the new control

**6.1** Near the top, find:
```javascript
const themeInput = document.getElementById("theme");
```

Immediately below it, add:
```javascript
const categoryInput = document.getElementById("category");
```

### Edit B: Read the current selection

**6.2** Inside async function generate(event), find:
```javascript
    const theme = themeInput.value;
```

Immediately below it, add:
```javascript
    const category = categoryInput.value;
```

This belongs **inside the function**, so each submission reads the current choice.

### Edit C: Include the choice in the request

**6.3** Inside the try block, find this exact block:
```javascript
        const response = await fetch("/api/generate");
        if (!response.ok) {
            throw new Error("The server could not generate an item.");
        }
        const data = await response.json();
```

Replace only those lines with:
```javascript
        const parameters = new URLSearchParams({ category: category });
        const response = await fetch(`/api/generate?${parameters}`);
        const data = await response.json();

        if (!response.ok) {
            result.textContent = data.error;
            return;
        }
```

Copyable version: [03-request-block.js](lesson-6-snippets/03-request-block.js).

Keep the remaining lines that update the card and result, the catch/finally blocks, and the submit listener. Do not add another click or submit listener.

The new URL uses **backticks** around `/api/generate?${parameters}`, not ordinary quotation marks. Backticks allow JavaScript to insert the value inside ${...}.

**6.4** Save script.js. Hard refresh your application page in Chrome:
- macOS: Command + Shift + R
- Windows: Ctrl + Shift + R

**6.5** Enter StarFox, select Shield, and submit. The result must end in Shield. Choose Staff and submit again. It must end in Staff.

| New code | Purpose |
|---|---|
| categoryInput.value | Reads the selected option's value |
| new URLSearchParams({ category: category }) | Builds an encoded query string such as category=shield |
| fetch(`/api/generate?${parameters}`) | Requests an item with the chosen category |
| await response.json() | Reads either the successful JSON or the JSON error |
| if (!response.ok) | Detects an unsuccessful HTTP response |
| result.textContent = data.error | Displays the server's error message |
| return | Leaves the function early; the existing finally block still re-enables the button |

Nickname and card colour remain in the browser. Only the category is sent in this request. The application does not save these answers to a database.

**Checkpoint 6 — pass when:** the dropdown controls the generated item type and the nickname and colour features still work.

**If it fails:** use the troubleshooting table below. Compare with [the complete script](lesson-6-reference/static/script.js) if needed. Preserve your own customisation when comparing.

## Step 7: Test and explain — about 10 minutes

**7.1** Run these tests. Record what actually happened in lesson6_notes.txt; do not just copy the expected outcomes.

| Test | Expected result |
|---|---|
| Select Sword, then submit | Item ends in Sword |
| Select Shield, then submit three times | All three items end in Shield; adjectives may repeat |
| Select Staff, then submit | Item ends in Staff |
| Keep Staff selected; change colour to Forest green; submit | Green card and a Staff |
| Change the nickname; submit | New nickname appears |
| Submit an empty nickname | Browser requests a nickname |
| Type ?category=banana directly into the API URL | JSON error, not a generated item |
| Open /api/generate with no query string | A Sword is generated |

**7.2** Explain one complete request in four sentences:
1. What did the user choose?
2. What URL did JavaScript request?
3. How did Python use the category?
4. How did the returned item appear on the page?

**7.3** Show your teacher one valid choice and one invalid request.

**Checkpoint 7 — finished when:** your tests are recorded and you can explain how the user's choice reaches Python.

If you do not finish today, record: **Last passed checkpoint: __. Next action: __. Current error, if any: __.**

## Troubleshooting

| What you see | What to check first |
|---|---|
| Every result is a Sword | Did you replace the fetch block? Is the category read inside generate()? Save and hard refresh. |
| Cannot read properties of null | The HTML must contain exactly one id="category", and the script must load after the HTML elements. |
| Choose sword, shield, or staff | Check each option's value is lowercase and exactly matches Python. |
| SyntaxError in JavaScript | Check backticks, braces, and that you replaced the entire old request block. Use the browser console's file and line number. |
| SyntaxError or IndentationError in Python | Compare app.py with the supplied file. Keep four-space indentation consistent. |
| undefined appears | Successful Python responses must include item; JavaScript must read data.item. |
| The page reloads | Keep event.preventDefault() and the single form submit listener. Check the console for an earlier error. |
| No connection to the server | Check Flask is running, and your browser port matches it. |

To open the console in Chrome, right-click the page → Inspect → Console. Read the first red error. Include the filename and line number when asking for help.

## Optional extensions — after all checkpoints pass

**Extension A: Add a Bow category.**
1. Add a new HTML option with value="bow" and visible text Bow.
2. Add an elif branch in Python before else that sets item_type to "Bow".
3. Update the Python error message to include bow.
4. Test the dropdown and the direct API address.
5. Explain why JavaScript does not need another branch for this category.

**Extension B: Inspect the real request.**
Open Chrome developer tools → Network. Submit the form. Select the generate request and examine its URL, status, and JSON response. Check that category is present but nickname and theme are absent.

**Extension C: Keep the idea, change the theme.**
Plan three categories for a food, sport, or space generator. Write the visible option labels, values sent to Python, and expected item types before editing code. Update the default and error message too.

## Reference files

- [Complete app.py](lesson-6-reference/app.py)
- [Complete index.html](lesson-6-reference/static/index.html)
- [Complete script.js](lesson-6-reference/static/script.js)
- [Existing style.css](lesson-6-reference/static/style.css)

**Next lesson:** Use what you know about inputs, processing, and outputs to plan a small generator of your own.
