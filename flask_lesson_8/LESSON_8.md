# Lesson 8: Style your dashboard and add ready-made components

Today you will turn your Lesson 7 dashboard into a more deliberate design. You will style reusable cards, arrange them for different screen sizes, and add a working popup information window.

**Your goal is to explain your choices, not just make the page look different.**

You will use the AdminLTE and Bootstrap files already supplied in Lesson 7. A **component** is a reusable interface part, such as a card, badge, notice, or modal window. A **utility class** applies a small styling job, such as spacing or a shadow.

## Choose your pace

Time guide: **75–90 minutes**. Work through one chunk at a time. After a checkpoint works, continue without waiting for the class.

| Chunk | Task | Approximate time |
|---|---|---|
| 0 | Open your working Lesson 7 dashboard | 5–10 minutes |
| 1 | Plan your design and add a notice | 10 minutes |
| 2 | Add two responsive showcase cards | 15 minutes |
| 3 | Style both cards with your own CSS | 15 minutes |
| 4 | Add a modal information window | 15 minutes |
| 5 | Personalise, test, and explain | 15 minutes |

**Minimum target:** chunks 0–3, then the applicable tests in chunk 5. Write down your next chunk before stopping.

**Full target:** chunks 0–5. Extensions are optional.

Use [lesson8_notes.md](lesson8_notes.md) for your design choices and test results. You can copy its headings into your usual class document.

<br><br>

---

## Chunk 0: Start with your working dashboard

### 0A. Get the lesson folder

If your teacher gives you an extracted `flask_lesson_8` folder, use it and go to 0B.

Otherwise, once your teacher has uploaded this lesson:

1. Open the [class repository](https://github.com/bmackenty/26-27-9th-grade).
2. Click the green **Code** button on its main page.
3. Click **Download ZIP**.
4. Extract the downloaded ZIP. On Windows, right-click it and choose **Extract All**. On a Mac, double-click the ZIP.
5. Open the extracted folder, then open `flask_lesson_8`.

The downloaded lesson folder supplies examples. Your existing Flask project is where you work.

### 0B. Choose the correct starting point

**If your Lesson 7 dashboard already works:** keep using your existing project. Do not replace its files. Continue to 0C.

**If your Lesson 7 dashboard is missing or broken:** use the complete [starter](starter/) folder supplied here. It is the finished Lesson 7 reference, not the older Lesson 6 page.

1. Open your existing project folder in VS Code.
2. Copy `app.py` and `requirements.txt` from `starter` into that project folder. Replace the matching files if asked.
3. Open `starter/static` in your file manager.
4. Copy its contents into your project's `static` folder. Create `static` if it does not exist. Replace matching files if asked. This puts the reference design into those files.
5. Copy the whole `vendor` folder, including its licence files. Do not copy the contents by hand from a web page.
6. Check that you have `static/vendor/adminlte.min.css`, not `static/static/vendor/adminlte.min.css`.

### Here's what your files should look like now

| Project location | Purpose |
|---|---|
| `app.py` | Existing Flask server and `/api/generate` route |
| `requirements.txt` | Flask dependency |
| `static/dashboard.html` | Dashboard you will edit |
| `static/dashboard.css` | Custom styles you will edit |
| `static/dashboard.js` | Existing generator behaviour |
| `static/vendor/` | Existing AdminLTE and Bootstrap files and licences |
| `static/index.html`, `style.css`, `script.js` | Earlier Lesson 6 page |
| `.venv/` or your existing environment folder | Python environment on your computer |

### 0C. Run Flask

1. In VS Code, choose **Terminal → New Terminal**.
2. Make sure the terminal is in your project folder containing `app.py`. Use `dir` on Windows or `ls` on macOS/Linux to list files.
3. Activate your existing environment using the matching command below. If its name differs, replace `.venv` with that name.

| Terminal | Command |
|---|---|
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

If you have no environment, run `python -m venv .venv` first; on a Mac you may need `python3 -m venv .venv`. Then activate it. If PowerShell blocks activation, use Command Prompt or ask your teacher.

4. If Flask is missing, run `python -m pip install -r requirements.txt` in the activated environment. Installation needs internet.
5. Run:

```bash
python -m flask --app app run --debug
```

If Flask is already running for this project, keep that server running instead of starting a second one.

6. Open **http://127.0.0.1:5000/static/dashboard.html** in your browser.
7. Enter an invented nickname and click **Forge my item**.

Do not double-click the HTML file or use Live Server. Flask must serve this page.

### Checkpoint 0

You can see the styled dashboard, generate an item, and open the sidebar with **Menu**. Fix this before adding anything.

<br><br>

---

## Chunk 1: Plan the design and add a notice

### 1A. Decide who the page is for

1. Open your notes.
2. Finish: "My dashboard is for ___, who needs to ___."
3. Choose a theme, such as a wildlife centre, music studio, sports club, or space station.
4. Sketch two cards side by side. Label the heading, badge, description, and button on each.
5. Write one reason for showing these cards to your user. Ask your teacher to check your sketch before building.

Example: "My dashboard is for a fictional explorer who needs to compare two research stations."

### 1B. Insert a ready-made notice

A Bootstrap **alert** is a styled message panel. This one is a permanent information notice; it does not need a close button.

1. Open `static/dashboard.html` in VS Code.
2. Press **Ctrl+F** on Windows or **Command+F** on Mac.
3. Search for `<!-- START STATS:`. You should find the comment above the three statistic boxes.
4. Close the search box. Click at the start of that comment line.
5. Press Enter to create a blank line above it. Click the blank line.
6. Paste this entire block above the comment. Do not delete the comment or the statistics.

```html
<!-- START LESSON 8 NOTICE -->
<div class="alert alert-info mb-4">
  <strong>Workshop notice:</strong> These featured projects are fictional examples.
  The generator below still creates a new item when you submit its form.
</div>
<!-- END LESSON 8 NOTICE -->
```

7. Save with **Ctrl+S** or **Command+S**.
8. Refresh the browser. Look between the main banner and the statistic boxes.
9. Change only `alert-info` to `alert-warning`. Save and refresh. Observe the colour change.
10. Change it back to `alert-info`, then save and refresh again.

`alert` supplies the component's basic styling. `alert-info` chooses a colour treatment. `mb-4` adds space below it. Keep all three classes separated by spaces.

### Checkpoint 1

Your notice appears once, above the statistics. The generator still works. Explain which class changed the notice colour.

<br><br>

---

## Chunk 2: Build a responsive showcase

### 2A. Add two complete cards

1. Stay in `static/dashboard.html`.
2. Search for the exact comment `<!-- START COLLECTION -->`.
3. Create a blank line immediately above that comment, as you did in chunk 1.
4. Paste the whole block below into that blank space. Keep the existing collection table below it.

```html
<!-- START LESSON 8 SHOWCASE -->
<section class="mb-4" aria-labelledby="showcase-heading">
  <h2 id="showcase-heading" class="h4 mb-3">Project showcase</h2>
  <div class="row g-4">
  <div class="col-12 col-md-6">
    <article class="card showcase-card shadow-sm h-100">
      <div class="card-body p-4">
        <span class="badge text-bg-success mb-3">FEATURED</span>
        <h3 class="card-title mb-3">Forest Observatory</h3>
        <p>A quiet research station that catalogues imaginary discoveries.</p>
        <ul class="list-group list-group-flush mb-3">
          <li class="list-group-item">Type: fictional project</li>
          <li class="list-group-item">Status: design example</li>
        </ul>
        <a href="#workshop" class="btn btn-outline-success">Try the generator</a>
      </div>
    </article>
  </div>
  <div class="col-12 col-md-6">
    <article class="card showcase-card shadow-sm h-100">
      <div class="card-body p-4">
        <span class="badge text-bg-success mb-3">NEW IDEA</span>
        <h3 class="card-title mb-3">Ocean Laboratory</h3>
        <p>An underwater workshop that studies fictional sea creatures.</p>
        <ul class="list-group list-group-flush mb-3">
          <li class="list-group-item">Type: fictional project</li>
          <li class="list-group-item">Status: design example</li>
        </ul>
        <a href="#workshop" class="btn btn-outline-success">Try the generator</a>
      </div>
    </article>
  </div>
  </div>
</section>
<!-- END LESSON 8 SHOWCASE -->
```

5. Save and refresh.
6. Scroll down past the generator. You should see **Project showcase** above the collection table.
7. Click **Try the generator** on either card. It should move you to the existing generator section.

The cards already have library styling. The extra class `showcase-card` will acquire our own styling in chunk 3.

### 2B. Read the component before changing it

| Part of the HTML | What it does |
|---|---|
| `card` and `card-body` | Provide the ready-made card structure |
| `badge text-bg-success` | Display a compact green label |
| `list-group` and `list-group-item` | Format a small list consistently |
| `btn btn-outline-success` | Style the link as an outlined button |
| `href="#workshop"` | Link to the existing element with `id="workshop"` |
| `shadow-sm` | Add a subtle shadow |
| `p-4` | Apply padding inside the body |
| `mb-3` | Apply a bottom margin |
| `h-100` | Fill the available column height |

**Padding** is space inside an element's border. **Margin** is space outside it. The numbers in Bootstrap spacing classes are scale steps, not pixel counts.

### 2C. Test the responsive layout

1. Make your browser window wide. At a viewport width of at least 768 pixels, the two cards share a row.
2. Narrow the browser below 768 pixels. The cards should stack vertically.
3. Read the wrapper around each card:

```html
<div class="col-12 col-md-6">
```

Bootstrap divides a row into 12 units. `col-12` uses all 12 units by default. `col-md-6` uses 6 units from the medium breakpoint upward. Six plus six fills one row. `row g-4` creates the row and its gaps.

4. Predict what will happen if you change **both** occurrences of `col-md-6` inside the new showcase to `col-md-12`.
5. Make the changes, save, and refresh with a wide browser.
6. Compare the result with your prediction.
7. Change both back to `col-md-6`. Save and refresh.

### Checkpoint 2

Two cards appear side by side on a wide screen and stack on a narrow one. Both links reach the generator. Explain why `6 + 6 = 12` matters here.

<br><br>

---

## Chunk 3: Give your cards a shared style

### 3A. Add one reusable CSS class

1. Open `static/dashboard.css`.
2. Scroll to the very bottom, after the final closing `}`.
3. Make a new blank line. Paste the complete CSS below there. Keep all existing CSS above it.

```css
/* LESSON 8: styles for the new showcase only */
:root {
  --showcase-accent: #047857;
  --showcase-surface: #ecfdf5;
}
.showcase-card {
  border: 2px solid var(--showcase-accent);
  background-color: var(--showcase-surface);
  color: #172554;
}
.showcase-card .card-title {
  float: none;
}

```

4. Save the CSS file.
5. Refresh the dashboard. Both showcase cards should have green borders and pale green backgrounds.

### 3B. Understand the rule

In `.showcase-card`, the dot means "select elements that have this class." Both new cards have `class="card showcase-card shadow-sm h-100"`, so both receive the rule.

| CSS | Meaning |
|---|---|
| `--showcase-accent` | A named colour value, called a custom property |
| `var(--showcase-accent)` | Use that named value here |
| `border: 2px solid ...` | A solid border two pixels thick |
| `background-color` | The card's background colour |
| `color` | Its default text colour; more specific component rules can override it |
| `.showcase-card .card-title` | Select a card title inside a showcase card |
| `float: none` | Remove the library's floating title layout inside these cards |

The new `:root` block adds two custom properties. Keep Lesson 7's existing `--forge-accent` as well.

### 3C. Make a controlled colour change

1. Find `--showcase-accent: #047857;` in the CSS you just added.
2. Replace only `#047857` with `#6d28d9`.
3. Find `--showcase-surface: #ecfdf5;`.
4. Replace only `#ecfdf5` with `#f5f3ff`.
5. Save and refresh. The borders should turn purple and the card surfaces pale purple.
6. Notice that the green badges and outlined links have not changed. Their Bootstrap classes control those colours separately.
7. Choose the green or purple pair for your design. Keep dark text on the pale surface.

### 3D. Compare spacing

1. Return to `dashboard.html`.
2. Inside the first new card only, change `card-body p-4` to `card-body p-2`.
3. Save and refresh. Compare the space around the first card's contents with the second card.
4. Change it back to `p-4` for consistent spacing. Save and refresh.

Bootstrap spacing utilities normally use `!important`. This is why `p-2` can override the older `.card-body` padding rule. In general, loading your CSS last helps only when competing rules have suitable importance and specificity; it does not make every custom rule win.

### Here's what your files should look like now

| File | Changes so far |
|---|---|
| `static/dashboard.html` | Notice above stats; showcase above collection |
| `static/dashboard.css` | New CSS appended at the bottom |
| `static/dashboard.js` and `app.py` | Existing generator code |
| `static/vendor/` | Existing libraries, used as supplied |

### Checkpoint 3

Both cards share your selected border and surface colours. You can point to the CSS selector that affects both. Your notice, cards, and generator still work.

**Stopping here today?** Complete the tests for chunks 0–3 in chunk 5 and record "Next: chunk 4" in your notes.

<br><br>

---

## Chunk 4: Add a modal information window

A **modal** opens over the page and requires the user to close it before returning to the page underneath. It is useful for short supporting information. Keep essential instructions visible on the main page.

This component needs two parts: a button to open it and the window itself. Bootstrap's existing JavaScript supplies the behaviour.

### 4A. Add the opening button

1. Open `static/dashboard.html`.
2. Search for `Enter the workshop` near the top of the page.
3. Find the whole line containing that link:

```html
<a href="#workshop" class="btn btn-light">Enter the workshop</a>
```

If you renamed it last lesson, search for `class="btn btn-light"` inside the main banner instead.

4. Make a new line **after that complete `</a>`**, but **before the banner's `</header>`**.
5. Paste this button on the new line:

```html
<button type="button" class="btn btn-light ms-2"
        data-bs-toggle="modal" data-bs-target="#design-modal">
  About this design
</button>
```

6. Save and refresh. The new button appears in the main banner. It will open its window after you finish 4B.

### 4B. Add the window

1. In the same HTML file, search for this exact line near the bottom:

```html
<script src="/static/vendor/bootstrap.bundle.min.js"></script>
```

2. Create a blank line immediately **above** that script line. This is outside the main dashboard wrapper and before the scripts.
3. Paste the entire block below there. Do not put it inside a card, form, or script tag.

```html
<!-- START LESSON 8 MODAL -->
<div class="modal fade" id="design-modal" tabindex="-1"
     aria-labelledby="design-modal-title" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title fs-5" id="design-modal-title">About this design</h2>
        <button type="button" class="btn-close" data-bs-dismiss="modal"
                aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>This dashboard helps a fictional explorer find project ideas.</p>
        <p>The green borders group the featured cards. The badges describe each example.</p>
        <p>The cards contain sample text. They are not saved generator results.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-success" data-bs-dismiss="modal">Got it</button>
      </div>
    </div>
  </div>
</div>
<!-- END LESSON 8 MODAL -->
```

4. Save and refresh.
5. Click **About this design**. The window should open over a dimmed page.
6. Click **Got it**. The window should close.
7. Open it again. Press **Escape**. It should close again.

### 4C. Find the connections

| Attribute | Connection |
|---|---|
| `data-bs-toggle="modal"` | Tells Bootstrap which component to open |
| `data-bs-target="#design-modal"` | Points to the window's ID |
| `id="design-modal"` | Gives that window its unique identifier |
| `aria-labelledby="design-modal-title"` | Associates the window with its heading for assistive technology |
| `id="design-modal-title"` | Identifies that heading |
| `data-bs-dismiss="modal"` | Tells Bootstrap to close the window |

An **ID** identifies one element on a page. A **class** can be reused on many elements. Keep IDs unique. The `#` in the target points to an ID; the ID value itself has no `#`.

You added HTML instructions that existing library JavaScript understands. You did not add a Flask route. Opening this modal does not call `/api/generate`.

### Checkpoint 4

The modal opens and closes. You can point to the matching button target and window ID. The generator still works.

<br><br>

---

## Chunk 5: Make it yours and test it

### 5A. Personalise the examples

1. In the notice, change the message to explain your dashboard. Keep the statement that the showcase uses fictional examples.
2. In each showcase card, change the title, description, badge text, and the two list items to fit your plan.
3. Keep the cards' generator links functional. If you rename their link text, make it describe where the link goes.
4. If you built the modal, change its paragraphs to explain your intended user and one visual design decision.
5. Keep sample data labelled honestly. These cards do not show saved items and do not update when you generate an item.
6. Save both edited files and refresh.

The new showcase is separate from the existing three-row collection. You have not added collection rows, so its "Featured discoveries: 3" statistic can remain unchanged.

### 5B. Test what you built

Record actual results in your notes. Write "not built yet" for the modal if you stopped after chunk 3.

| Test | Expected result |
|---|---|
| View the page | Notice once; two showcase cards; original dashboard still present |
| Narrow browser below 768 pixels | Showcase cards stack; text stays readable |
| Widen browser above 768 pixels | Showcase cards share a row |
| Click both card links | Each reaches the generator |
| Submit an invented nickname twice | Items appear; live browser counter reaches 2 after a fresh reload |
| Refresh | Live counter resets to 0; sample cards stay the same |
| Open modal; click Got it | Window opens, then closes |
| Open modal; press Escape | Window closes |
| Use Tab, then Enter on the modal opener | Window opens; Tab stays within it while open |
| Close modal with Escape | Keyboard focus returns to the opener |
| Use Tab through the page | Interactive controls have a visible focus outline |

For a precise narrow-screen test in Chrome or Edge: open developer tools with **Ctrl+Shift+I** (Windows) or **Command+Option+I** (Mac), click the phone/tablet icon, select **Responsive**, and set width to `375`. Set browser zoom to 100%. Close developer tools afterwards.

### 5C. Explain your work

Answer in your own words:

1. Which class is yours, and which two classes came from Bootstrap?
2. What is the difference between padding and margin? Point to an example.
3. Why can one CSS rule change both showcase cards?
4. How does the modal button find its window? Answer if you completed chunk 4.
5. How does one visual choice help your intended user?

### Checkpoint 5: Submit

Use the normal class submission method:

- One screenshot of your personalised dashboard showing the showcase.
- Your completed notes and actual test results.
- Your edited `dashboard.html` and `dashboard.css` if requested by your teacher.

No GitHub account or upload is required for students. Do not submit your Python environment folder.

<br><br>

---

## Complete files for comparison

The [completed folder](completed/) contains a runnable example of all core additions. It uses the green palette and fictional station theme. Your personalised version can look different.

- [Complete dashboard HTML](completed/static/dashboard.html)
- [Complete dashboard CSS](completed/static/dashboard.css)
- [Unchanged generator JavaScript](completed/static/dashboard.js)
- [Unchanged Flask application](completed/app.py)
- [Complete local vendor folder](completed/static/vendor/)

To compare: open the matching file on GitHub, click **Raw**, and inspect the code. If you need to replace a broken file, select all the code in that local file and paste the complete reference code. This replaces your edits in that file. Save and test before personalising it again. Do not paste Markdown fences into HTML or CSS.

Each component is also supplied separately in [snippets](snippets/). These are pieces to paste at the named locations, not standalone pages.

<br><br>

---

## Optional extensions

### A. Three cards across

1. Find `<!-- START LESSON 8 SHOWCASE -->`.
2. Copy one whole column, from `<div class="col-12 col-md-6">` through its closing `</div>` after `</article>`.
3. Paste it immediately after the second column, inside the same `row g-4` wrapper.
4. Change all three column classes to `col-12 col-md-6 col-xl-4`.
5. Give the third card a new title and content.
6. Test: one card per row below 768 pixels, two per row from 768 pixels, and three per row from 1200 pixels. The last card wraps when there are two per row.

### B. Add a second modal

1. Duplicate the complete modal block outside the dashboard wrapper.
2. In the copy, change `design-modal` to `rules-modal`, and change both occurrences of `design-modal-title` to `rules-modal-title`.
3. Change the copy's heading to `Project rules` and write suitable rules in its body.
4. Duplicate the opening button beside the first one in the banner.
5. In the new button only, change the target to `#rules-modal` and its visible text to `Project rules`.
6. Test each opener separately. Each must open the correct window. Keep only one modal open at a time.

### C. Inspect a styling rule

1. Right-click a showcase card and choose **Inspect**.
2. In the Styles panel, find `.showcase-card`.
3. Temporarily change the border width from `2px` to `6px` there.
4. Refresh. Notice that the temporary change disappears.
5. To keep the change, edit `dashboard.css`, save, and refresh instead.
6. Explain the difference between an experiment in developer tools and a saved source-code change.

<br><br>

---

## If something goes wrong

| Symptom | Check this first |
|---|---|
| Nothing changes | Save the correct file, then hard-refresh: Ctrl+Shift+R or Command+Shift+R |
| Plain page without styling | Confirm the complete `static/vendor` folder is present |
| Only the new border is missing | CSS pasted after the final `}`? Does HTML include `showcase-card`? |
| Only one card changes colour | Both cards need exactly the same `showcase-card` class |
| Cards never sit side by side | Both columns need `col-md-6` inside the same `row`; browser must be at least 768 pixels wide |
| Modal button does nothing | Target is `#design-modal`; window ID is `design-modal`; Bootstrap bundle script still exists |
| Modal appears inside a card | Move the complete modal block to just above the Bootstrap script, outside the wrapper |
| A card link goes nowhere | Keep the existing `id="workshop"` and the link's `href="#workshop"` |
| Generator stopped working | Check you pasted outside its form; compare with the complete HTML |
| Page returns 404 | Run the correct project and use `/static/dashboard.html` |
| Server cannot start | Stop the previous server with Ctrl+C; activate the correct environment |

Do not edit the minified files in `vendor`. Keep the existing generator IDs and script links. Add each new block only once.

## Sources for further exploration

These online references are optional; the supplied local files are sufficient for the lesson.

- [Bootstrap cards](https://getbootstrap.com/docs/5.3/components/card/)
- [Bootstrap spacing](https://getbootstrap.com/docs/5.3/utilities/spacing/)
- [Bootstrap grid](https://getbootstrap.com/docs/5.3/layout/grid/)
- [Bootstrap modal](https://getbootstrap.com/docs/5.3/components/modal/)
- [AdminLTE documentation](https://docs.adminlte.io/)

Use Bootstrap 5 examples with this bundle. Keep its existing local script and stylesheet links rather than adding another library copy.
