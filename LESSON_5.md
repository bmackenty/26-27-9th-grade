# Lesson 5: Build a form and a personalised result card

**Time: 60 minutes**

Today you will give your generator a colourful banner, a badge, and a result card. You will also ask the user for an invented nickname and a colour choice, then use those answers on the page.

By the end, you should be able to:
- Create and personalise a styled HTML element.
- Use a label, text input, dropdown, and submit button.
- Read a user's answers with JavaScript.
- Explain why you ask for each piece of data.
- Test an empty input and a successful submission.

## Step 1: Get everyone to the same starting point — 10 minutes

Follow the [README](README.md) to copy the four complete Lesson 4 files into your existing project. Back up your own files first. Use the **top-level files**, not lesson-5-reference yet. Keep your existing virtual environment.

Activate your environment and run:
```bash
python -m flask --app app run --debug
```
Open http://127.0.0.1:5000/static/index.html. Adjust both command and address if you use port 5001.

Click Generate. You should see a random item in a blue result area inside a white card. A result may repeat.

**Checkpoint:** Your styled Lesson 4 application works. Ask for help now if it does not.

## Step 2: Decide what to ask — 5 minutes

A form collects answers through controls such as text boxes and dropdown lists. First decide why each answer is useful.

| Information | Why ask for it? | Control |
|---|---|---|
| Invented nickname | Address the user in the result | Text input |
| Card colour theme | Let the user choose the result's appearance | Dropdown |

Discuss with a partner: would this generator need a home address or date of birth? Give a reason for your answer.

Sketch a form with these two controls and a submit button. Add a visible label for each control. Use made-up names in today's tests.

**Checkpoint:** Explain what you will do with each answer.

## Step 3: Build your banner and form — 15 minutes

Open static/index.html. Keep the stylesheet link and the script line.

**3.1** Replace the existing main heading and welcome paragraph with this banner (also available in [01-hero.html](lesson-5-snippets/01-hero.html)):

```html
<header class="hero">
    <span class="badge">CREATIVE LAB</span>
    <h1>The Item Forge</h1>
    <p>Choose a look. Give your creation a name to belong to.</p>
</header>
```

**3.2** Replace the old Generate button and the old paragraph with id="result" with this block. Remove the old pair completely so you do not have duplicate IDs. This block stays inside your existing main element.

[Copyable form snippet](lesson-5-snippets/02-form-and-result.html)

```html
<form id="generator-form">
    <h2>Design your result card</h2>

    <label for="nickname">Invented nickname (required)</label>
    <input type="text" id="nickname" name="nickname"
           placeholder="For example, StarFox" required maxlength="20"
           aria-describedby="nickname-help">
    <p id="nickname-help" class="hint">Use a made-up name, up to 20 characters.</p>

    <label for="theme">Card colour theme</label>
    <select id="theme" name="theme">
        <option value="ice">Ice blue</option>
        <option value="fire">Fire orange</option>
        <option value="forest">Forest green</option>
    </select>

    <button type="submit" id="generate-button">Forge my item</button>
</form>

<section id="result-card" class="result-card" data-theme="ice"
         aria-labelledby="result-heading">
    <span id="theme-badge" class="badge">ICE BLUE</span>
    <h2 id="result-heading">Your creation</h2>
    <p id="result" aria-live="polite">Your item will appear here.</p>
</section>
```

Keep the example list and the generator data link below this block. Save. Before testing the new form, complete Step 5: the old script still listens for clicks instead of form submissions.

| New HTML | What it does |
|---|---|
| form | Groups the controls into one form |
| label for="nickname" | Connects the visible label to the input with that ID |
| required | Stops ordinary submission with an empty nickname |
| maxlength="20" | Limits ordinary text entry to 20 characters |
| placeholder | Shows a temporary example; it does not replace a label |
| name="nickname" | Names the field for ordinary form submission; today's script uses its ID |
| select and option | Give a fixed set of choices |
| type="submit" | Makes the button submit the form |
| aria-live="polite" | Helps assistive technology announce an updated result |

**Checkpoint:** Identify both controls and their labels. Explain why a dropdown is useful for a choice with three allowed values.

## Step 4: Make your elements look good — 10 minutes

Open [03-add-to-style.css](lesson-5-snippets/03-add-to-style.css). Copy all its code and **append it to the bottom** of your local static/style.css. Keep the Lesson 4 CSS above it.

Save and refresh. You should see a purple-and-blue banner, a rounded badge, styled inputs, and a result card.

Look at these rules in the new CSS:

```css
.hero {
    background: linear-gradient(135deg, #172554, #6d28d9);
    color: white;
    padding: 28px;
    border-radius: 16px;
    margin-bottom: 24px;
}

.badge {
    display: inline-block;
    background-color: #172554;
    color: white;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 1px;
}
```

A gradient blends colours. The badge uses a large border radius to give it a pill shape. The card's box-shadow adds a soft shadow. These effects come from CSS classes you can reuse.

**Make two deliberate changes:**
1. Change the banner title and badge text to fit your own theme.
2. Change one visual property: gradient colours, padding, corner rounding, or shadow.

Edit the existing rule instead of adding another copy. Predict what will happen, save, refresh, and compare. Keep light text on a dark background or dark text on a light background.

**Checkpoint:** Point to the CSS declaration you changed and describe its effect.

## Step 5: Use the user's answers — 10 minutes

Open [04-replace-script.js](lesson-5-snippets/04-replace-script.js). Copy all its code and **replace the entire contents** of your local static/script.js. This removes the old click listener so a submission only makes one request.

Save and hard refresh in Chrome: Command + Shift + R on macOS, Ctrl + Shift + R on Windows.

Read these key lines in the new script:

| Code | Purpose |
|---|---|
| form.addEventListener("submit", generate) | Runs the function when the form is submitted, including with Enter |
| event.preventDefault() | Stops the form's default page navigation |
| nicknameInput.value.trim() | Reads the nickname and removes spaces at its ends |
| themeInput.value | Reads the selected option's value |
| fetch("/api/generate") | Requests an item from Python |
| resultCard.dataset.theme = theme | Changes the card's data-theme attribute so the matching CSS applies |
| result.textContent = ... | Displays the nickname and generated item as text |

The script also shows a waiting message, temporarily disables the button, and reports a failed request. Read its comments; today's focus is on reading the two answers and using them.

Try nickname **StarFox** and theme **Fire orange**. Submit the form. Your orange card should show something like:

> StarFox, your item is: Glowing Staff

Choose **Forest green** and submit again. The card should turn green.

**Where does the data go?** The nickname and theme are used by JavaScript in the browser. The request to Flask still asks only for a random item. This code does not send those two answers to Python or save them. The theme changes the card's appearance, not the Python generation rules.

**Checkpoint:** Point to where JavaScript reads a field, where it contacts Flask, and where it updates the page.

## Step 6: Test and reflect — 10 minutes

Work with a partner. Record actual results in lesson5_notes.txt.

| Test | Expected result |
|---|---|
| Submit an empty nickname | Browser requests a value; no item request is sent |
| Submit spaces only | Page asks for an invented nickname |
| Submit StarFox and Fire orange | Orange card, matching badge, nickname and generated item |
| Submit a second nickname and Forest green | Updated greeting and green card |
| Press Enter while in the nickname input | Form submits without a page reload |
| Try typing more than 20 characters | Input stops at the specified maximum |
| Navigate using Tab | Inputs and button show visible keyboard focus |
| Narrow the window to phone width | Controls and card fit without horizontal scrolling |

Answer in your notes:
1. **Explain** why a visible label is useful when an input also has a placeholder.
2. **Identify** which of today's form answers are sent to Python.
3. **Justify** one piece of information you chose not to ask for.
4. **Describe** one visual change you made and its effect on the user.

**Checkpoint:** Show a working personalised card, one intentional design change, and one invalid-input test.

## If something goes wrong

| Problem | Check |
|---|---|
| Page reloads or form answers appear in the address | Replace the complete script, check its path, hard refresh, and inspect the console. preventDefault must run. |
| Clicking submits twice | Remove the old click listener; use only the supplied form submit listener. |
| JavaScript mentions null | Check IDs match the script and each is present exactly once. |
| Card does not change colour | Submit after changing the dropdown. Check data-theme, dataset.theme, and the appended CSS. |
| Card changes but an old blue rectangle remains | Check the final #result rule sets background-color: transparent. |
| CSS seems missing | Visit /static/style.css to check it loads, then hard refresh the page. |
| Result is undefined | Python must return the item key and JavaScript must read data.item. |
| Generator cannot be reached | Check Flask is running and use its /static/index.html address. |

Compare with [the complete Lesson 5 reference](lesson-5-reference) if you need to locate a mistake.

## Finished early?

Choose one:
- Create a second badge explaining what your generator does. Reuse class="badge".
- Add an optional tagline input with a label and a 40-character maximum. Read its value and display it using textContent. Keep it in the browser.
- Sketch a form for a different project. Specify three fields, their controls, and the purpose of each answer. Do not add unused fields to this application.

**Next lesson:** You will choose an item category and send that choice to Python so the input changes what the generator produces.

Sources: [MDN: Your first form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form); [MDN: submit event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit_event).
