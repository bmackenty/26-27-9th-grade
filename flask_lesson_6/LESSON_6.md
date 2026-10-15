# Lesson 6 — Make your generator look extraordinary

Today you will turn your working generator into a designed web page: a dramatic banner, a gallery of collectible cards, and an expandable field guide. Choose a theme you enjoy: space exploration, football, music, wildlife, fantasy, cooking, or something else.

**HTML creates the structure and meaning. CSS creates most of the visual effects. JavaScript keeps your form working, and Python generates the random item.**

You will practise adding HTML elements, reusing CSS classes, and testing each small change. You should be able to explain one HTML element and one CSS declaration you changed.

## Choose your pace

Allow approximately 60–90 minutes. The times are guides, not deadlines.

| Chunk | Task | Approximate time | Finish line |
|---|---|---|---|
| 0 | Update and test your files | 10 minutes | Working Lesson 5 form |
| 1 | Create your visual identity | 10 minutes | New banner and working jump link |
| 2 | Build a card gallery | 15 minutes | Three cards that stack on a narrow screen |
| 3 | Make the design yours | 10 minutes | Three explained changes |
| 4 | Add expandable help | 10 minutes | Help works with mouse and keyboard |
| 5 | Test and explain | 10 minutes | Evidence and reflection saved |
| Extensions | Choose a further challenge | Remaining time | Tested improvement |

**Work independently through the chunks.** After each checkpoint, continue without waiting for the class. If you need more time, finish one chunk before opening the next. If you get stuck, write the chunk number and what you expected, then ask for help.

**Minimum target today:** chunks 0–2, personalise one card, then complete the applicable tests in chunk 5. Continue chunks 3–4 next time. **Full core target:** chunks 0–5. Extensions come after the core checkpoints, not instead of them.

## Chunk 0 — Update your project safely

Even if Lesson 5 was unfinished, these steps give you a complete working starting point.



### 0B — Replace the complete files

Open the class repository's `flask_lesson_6` folder. Use its **top-level files**, not `lesson-6-reference` and not the old `flask_lesson_5` folder.

For each file below: open the source link, click **Raw**, select and copy all the code, open the matching local file, select all its old contents, paste, and save. On Windows use Ctrl+A / Ctrl+C / Ctrl+V; on Mac use Command+A / Command+C / Command+V. Do this inside the file editor, not the terminal. Do not paste Markdown backticks into code files.

| Copy from this lesson | Replace this local file | Action |
|---|---|---|
| [app.py](app.py) | app.py | Replace everything |
| [index.html](static/index.html) | static/index.html | Replace everything |
| [style.css](static/style.css) | static/style.css | Replace everything |
| [script.js](static/script.js) | static/script.js | Replace everything |
| [requirements.txt](requirements.txt) | requirements.txt | Replace everything |

Create a missing file or folder using exactly the name shown. `static` must be beside `app.py`, and the three browser files must be inside `static`. Do not create `static/static`. Copy [lesson6_notes.md](lesson6_notes.md) into your project too.

### 0C — Run the right project

run:
```bash
python -m flask --app app run --debug
```

Open **http://127.0.0.1:5000/static/index.html** in your browser. Do not double-click the HTML file and do not use Live Server. If your class uses port 5001, add `--port 5001` to the Flask command and use 5001 in the address.

Hard-refresh: Ctrl+Shift+R on Windows or Command+Shift+R on Mac.

### Checkpoint 0

You should see **The Item Forge**, a nickname field, a colour dropdown, and **Forge my item**. Enter `StarFox`, select **Fire orange**, and submit. The result card should turn orange and include your nickname and an item. An empty nickname should be blocked.

**Stop here if this does not work.** Fix the starting point before changing its design. Record checkpoint 0 in your notes.

## Chunk 1 — Give the page a visual identity

### 1A — Replace the banner

1. Open `static/index.html`.
2. Find `<header class="hero">`.
3. Select that whole block, ending with its matching `</header>`.
4. Replace it with all the code in [01-hero.html](lesson-6-snippets/01-hero.html).
5. Keep the form and everything below the header.

The new link contains `href="#generator-form"`. This jumps to the existing element with `id="generator-form"`. It does not generate an item.

### 1B — Add the visual styling

1. Open [02-foundation.css](lesson-6-snippets/02-foundation.css) and copy all its code.
2. Open your local `static/style.css`.
3. Go to the very bottom, after the final closing brace `}`.
4. Paste the new CSS **once**. Keep all the existing CSS above it.
5. Save both files and refresh.

Later rules can override earlier rules of equal specificity. We intentionally add these lesson rules at the bottom. When personalising them later, edit these new rules rather than repeatedly pasting them.

### 1C — Make two small changes

Change the heading `Build something legendary.` and the sentence below it to match your interests. Keep the HTML tags. Change the badge text too, but keep `LESSON 6` so you can identify this version.

**Predict, then try:** in the new `.hero` rule, change the last gradient colour from `#9d174d` to `#065f46`. Save and refresh. Which end changed?

### Checkpoint 1

You have a dark page background, a colourful banner, and a rounded white link. Click **Enter the workshop**: the browser targets the form. On a tall screen it may already be visible, so little scrolling occurs. Confirm the address ends in `#generator-form`.

In your notes, explain what `href="#generator-form"` connects to. Test the form again.

## Chunk 2 — Build a collectible card gallery

### 2A — Replace the old example list

1. Open `static/index.html`.
2. Find `<h2>Example results</h2>` near the bottom.
3. Select that heading and the entire `<ul> ... </ul>` immediately below it.
4. Replace that selection with [03-gallery.html](lesson-6-snippets/03-gallery.html).
5. Keep the **Open the generator data** link, the closing `</main>`, and the script line below your new section.

This gives you three example cards. They are **static examples**; pressing Forge changes the live result above, not these cards.

### 2B — Style the gallery

Append [04-gallery.css](lesson-6-snippets/04-gallery.css) **once** to the bottom of `static/style.css`. Save and refresh.

| HTML or CSS | What to look for |
|---|---|
| `<section>` | Groups the whole gallery under a heading |
| `<article>` | Contains one self-contained example card |
| `<h3>` | Gives a card a heading beneath the section's h2 |
| `<dl>`, `<dt>`, `<dd>` | Represent a label and its value, such as Origin and Ancient Grove |
| `class="showcase-card fire"` | Applies two classes to one element |
| `display: grid` | Arranges the cards into a grid |
| `gap: 18px` | Adds space between grid items |
| `border-radius: 18px` | Rounds the card corners |
| `box-shadow` | Adds depth with a shadow |
| `:hover` and `transform` | Lift the card when the pointer is over it |
| `@media (max-width: 760px)` | Changes to one column when the viewport is narrow |

The large numbers in `.card-art` are decorative and hidden from assistive technology with `aria-hidden="true"`. The card names and descriptions remain readable. The cards are not buttons, so you do not need to click them.

### Checkpoint 2

At a wide browser width, you should see three cards in a row. Narrow the browser below approximately 760 pixels: they should stack. Hover over a card: it should lift slightly unless your device requests reduced motion.

Change **Frozen Compass** to your own item name and change its description. Keep its tags and classes. Explain why the gallery does not update when you submit the form.

## Chunk 3 — Turn the examples into your own design

Make the following changes **one at a time**. Save and refresh after each.

1. **Content:** change all three card titles, descriptions, badge labels, and Origin values. Use a consistent idea, such as three planets, three albums, or three fictional inventions. These are invented examples; label fictional claims clearly if needed.
2. **Spacing:** in the newly added `.gallery` rule, change `gap: 18px` to `gap: 28px`. Predict which space will grow before refreshing.
3. **Shape:** in `.showcase-card`, change `border-radius: 18px` to `border-radius: 6px`. Decide which appearance suits your theme and keep your preferred value.
4. **Colour:** change the two colours in `.fire .card-art`. Keep the decorative number readable against its background.

You can rename visible labels freely. Keep the existing `ice`, `fire`, and `forest` classes unless you also update their CSS selectors. Do not rename the form's IDs: JavaScript uses them to find its elements.

**Protect these IDs:** `generator-form`, `generate-button`, `nickname`, `theme`, `result-card`, `theme-badge`, `result`, `result-heading`, and `nickname-help`. Each ID must appear only once as an `id` attribute.

### Checkpoint 3

In your notes, record three changes using: **I changed ___ in ___ because ___. The visible effect was ___.** At least one must concern HTML and one CSS. Your generator must still work.

## Chunk 4 — Add help that opens and closes

### 4A — Insert the help section

1. Open `static/index.html`.
2. Find the paragraph containing **Open the generator data**.
3. Put your cursor at the start of that paragraph and insert a blank line above it.
4. Paste [05-help.html](lesson-6-snippets/05-help.html) into that space. This puts the help after the gallery but inside `<main>`.
5. Append [06-help.css](lesson-6-snippets/06-help.css) once to `static/style.css`.
6. Save and refresh.

`<details>` is an expandable HTML element. Its `<summary>` is the visible label. The browser handles opening and closing it; you do not need to write JavaScript for this feature.

### 4B — Add your own question

Copy one whole `<details> ... </details>` block and paste it immediately after the other details blocks, before the help section's closing `</section>`. Change the question and answer. Example: **Are the gallery cards live results?** Answer: **No. They are example designs. My generated result appears above them.**

### Checkpoint 4

Open and close the questions with your mouse. Then use Tab to focus a summary and press Enter or Space to toggle it. Keep a visible focus outline. Explain why this interaction works without an additional JavaScript function.

## Chunk 5 — Test like a developer

Copy this table into your notes, or fill in the supplied notes file. Record what actually happened. If a test fails, write the fix and retest. If you have not reached a feature, record **not built yet**, not **passed**.

| Test | Expected result |
|---|---|
| StarFox + Fire orange, then submit | Nickname and generated item appear; live card turns orange |
| New nickname + Forest green, then submit | Result updates and live card turns green |
| Empty nickname | Browser asks for a value |
| Spaces-only nickname | Page asks for an invented nickname |
| Enter while in nickname field | Form submits without navigating away |
| Click banner link | Address targets #generator-form |
| Narrow viewport to about 375 pixels | Cards stack; no sideways page scrolling |
| Use Tab through the page | Interactive elements have visible focus |
| Toggle a help question with keyboard | Answer opens and closes |
| Generate again | Gallery stays unchanged; live result updates; random item may repeat |

Finish these sentences:

1. **HTML controls ___; CSS controls ___.** Use one example of each from your page.
2. **A class can be reused because ___; an ID should be unique because ___.**
3. **My best design decision was ___ because it helps the user ___.**
4. **The next chunk or improvement I need to work on is ___.**

Save everything. Commit your changed files and notes using your usual GitHub workflow. Use a meaningful message such as `Add responsive gallery and expandable help`. Do not commit your virtual environment or backup folder. Submit a screenshot of your page and your notes using the class's normal submission method. Be ready to point to and explain your own changes.

## Extensions — Choose one after the core checkpoints

### A — Add a fourth card

Duplicate one complete `<article> ... </article>` inside `.gallery`. Give it a new title, description, and decorative number. Do not duplicate the gallery section's ID. Predict where a fourth card goes in a three-column grid, then check. Try `repeat(2, minmax(0, 1fr))` in the main gallery rule and compare; keep the narrow-screen rule at one column.

### B — Use your own illustration or photograph

Create `static/images` and place an image you own or have permission to use there, named `my-item.jpg`. In one card, replace the entire `<div class="card-art" ...>...</div>` with:

```html
<img class="card-image" src="/static/images/my-item.jpg"
     alt="A brass compass resting on a hand-drawn map">
```

Change `alt` to describe your actual image. Add this CSS at the bottom:

```css
.card-image {
    display: block;
    width: 100%;
    height: 180px;
    object-fit: cover;
}
```

Explain what gets cropped by `object-fit: cover`. Test the image path by opening it directly in the browser. Use a suitable image without identifying classmates.

### C — Design a new visual theme

Create a fourth gallery style called `cosmic`. Change one card to `class="showcase-card cosmic"` and add a `.cosmic .card-art` CSS rule with a new gradient. This changes a gallery card, not the form's dropdown. Explain that distinction. Test narrow and wide layouts.

### D — Investigate reduced motion

Read the `prefers-reduced-motion` block in the gallery CSS. Explain which two effects it disables and why a user might prefer that. If your device allows it, enable reduced motion in accessibility settings and test. Restore your preferred setting afterwards. Keep all information available without hovering.

## If you get stuck

| Symptom | First thing to check |
|---|---|
| Old page appears | Correct project terminal, correct URL, saved files, then hard-refresh |
| CSS changes do nothing | Visit /static/style.css; confirm your new rule is present and not inside another rule |
| File contains ``` or GitHub page text | Recopy from Raw; paste code only |
| Cards have no colours or layout | Append the gallery CSS once and check class spelling |
| Form stops working | Check the protected IDs and that /static/script.js still loads |
| Entire bottom of page looks strange | Compare closing tags with the relevant snippet |
| Two copies of a component | Undo the extra paste; replace a block only where instructed |
| Flask reports address already in use | Stop your earlier Flask terminal or use the class-approved alternate port |
| Flask cannot be imported | Activate your environment and install requirements with that Python |

**Recovery:** save your current files first. Compare the affected block with [lesson-6-reference](lesson-6-reference). If you cannot locate the error, replace only the affected file with its complete reference version, then reapply your own changes from your backup. The reference is one finished example, not the only correct design.

**Looking ahead:** Lesson 5 previewed sending a category to Python. We are deliberately saving that for a later lesson so today can focus on HTML and CSS. Nickname and theme still stay in the browser in this supplied application.
