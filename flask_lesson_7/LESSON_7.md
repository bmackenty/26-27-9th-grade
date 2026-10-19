# Lesson 7: Build your creative command centre

Today you will install a complete dashboard, make it your own, and choose a component you could reuse in your project.

**You will have something working and visually impressive before you begin customising it.**

A **dashboard** brings useful information and controls together on one page. Ours uses **AdminLTE**, a ready-made collection of front-end styles and interface behaviours. You do not need to write the whole design yourself.

**You do not need a GitHub account, Git, Node.js, npm, or a build command.** You will copy files and run Flask as before. The dashboard's CSS and JavaScript are included in this lesson folder, so the page does not load them from the internet.

<br>

## Choose your pace

Allow approximately 60–90 minutes. These are guides, not deadlines.

| Chunk | Your task | Time guide | Checkpoint |
|---|---|---|---|
| 0 | Bring your files up to the completed Lesson 6 baseline | 10 min | Gallery, help, and generator work |
| 1 | Install and explore the complete dashboard | 10 min | Dashboard runs locally |
| 2 | Make three visual changes | 10 min | It looks like your project |
| 3 | Choose and adapt a component | 15 min | One component serves your idea |
| 4 | Trace the front end and back end | 10 min | You can explain a request |
| 5 | Test and record evidence | 10–15 min | Tests and notes completed |
| Extensions | Choose an extra challenge | Remaining time | Tested improvement |

**Minimum target:** chunks 0–2, then the relevant tests in chunk 5. Complete chunks 3–4 next lesson if necessary.

**Full core target:** chunks 0–5.

Continue after each checkpoint without waiting for the class. If you are stuck, record the chunk number, what you expected, and what actually happened. Ask for help before making several more changes.

Save your notes in [lesson7_notes.md](lesson7_notes.md), or copy its headings into your usual class document.

<br>

---

## Chunk 0: Get everyone to the end of Lesson 6

**Goal:** start with a working generator, styled gallery, and expandable help, even if you did not finish last time.

### 0A. Protect your work

1. Stop Flask using **Ctrl+C** in its terminal.
2. Back up your own `app.py` and `static` folder somewhere outside your working project. Name the backup `before-lesson-7`.
3. Keep your own customisations in that backup. The baseline below is a complete example; it will replace the files you copy over.

<br>

### 0B. Get the lesson files without an account

**If your teacher gives you an extracted `flask_lesson_7` folder, use that copy.** This is the quickest route if the internet is unreliable.

Otherwise:

1. Open the public [class repository](https://github.com/bmackenty/26-27-9th-grade).
2. On the repository's main page, choose **Code → Download ZIP**. No login is required for this public repository.
3. Extract the ZIP. On Windows, use **Extract All**. Do not work inside the ZIP viewer.
4. Find the `flask_lesson_7` folder inside the extracted repository.
5. Keep this downloaded folder available as your **source**. Your existing Flask project is the **destination**.

You are not uploading, committing, or pushing anything to GitHub today.

<br>

### 0C. Replace these five files with the complete Lesson 6 versions

The top-level application files supplied with Lesson 7 contain the **finished Lesson 6 reference**, including the gallery and help. They are not Lesson 6's earlier starting files.

Copy each entire file from the downloaded lesson folder into the matching place in your working project:

| Source in `flask_lesson_7` | Destination in your project | Action |
|---|---|---|
| [app.py](app.py) | `app.py` | Replace entire file |
| [requirements.txt](requirements.txt) | `requirements.txt` | Replace entire file |
| [static/index.html](static/index.html) | `static/index.html` | Replace entire file |
| [static/style.css](static/style.css) | `static/style.css` | Replace entire file |
| [static/script.js](static/script.js) | `static/script.js` | Replace entire file |

You can copy files in your file manager. If copying code from GitHub, open the file, choose **Raw**, copy all the code, and replace all the contents of the matching local file. Do not copy the GitHub page or Markdown backticks.

**Do not copy a second `static` folder inside your existing `static` folder.**

<br>

### Here's what your files should look like now

| Location | What it contains |
|---|---|
| `app.py` | Flask routes `/` and `/api/generate` |
| `requirements.txt` | Flask dependency |
| `static/index.html` | Completed Lesson 6 page |
| `static/style.css` | Completed Lesson 6 styles |
| `static/script.js` | Completed Lesson 6 form behaviour |
| `.venv/` or your existing environment folder | Your existing Python environment; do not replace it |

Full baseline backup: [lesson-6-complete](lesson-6-complete/). You do not run Flask from this backup folder.

<br>

### 0D. Start Flask

Open your working project in your editor. Open its terminal in the folder containing `app.py`. Activate your existing virtual environment.

If it is called `.venv`, use the command for your terminal:

| Terminal | Activation command |
|---|---|
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

If your environment has a different name, use that name instead. If you have no environment yet, run `python -m venv .venv` first, then activate it. On some Macs use `python3` to create it. If PowerShell blocks activation, ask your teacher or use Command Prompt; do not change computer security settings.

**Only if Flask is not installed in that environment**, install it while internet is available:

```bash
python -m pip install -r requirements.txt
```

Then start the app:

```bash
python -m flask --app app run --debug
```

Open **http://127.0.0.1:5000/static/index.html**.

Do not double-click the HTML file or use Live Server. Flask must serve the page and its API from the same address.

<br>

### Checkpoint 0

- You see the dramatic Lesson 6 banner, three gallery cards, and expandable help.
- Enter `StarFox`, choose **Fire orange**, and click **Forge my item**.
- Your nickname and a generated item appear; the result card turns orange.
- The gallery cards stay unchanged.

**Stop and fix this checkpoint before continuing.** Save your observation in your notes.

<br>

---

## Chunk 1: Install the dashboard and get to the interesting part

**Goal:** run a full dashboard with local assets.

### 1A. Copy four additions

Keep Flask running. Copy these from the lesson folder into your working project:

| Source | Destination | Action |
|---|---|---|
| [static/dashboard.html](static/dashboard.html) | `static/dashboard.html` | Copy whole file |
| [static/dashboard.css](static/dashboard.css) | `static/dashboard.css` | Copy whole file |
| [static/dashboard.js](static/dashboard.js) | `static/dashboard.js` | Copy whole file |
| `static/vendor` folder | `static/vendor` folder | Copy the entire folder, including licences |

**Copy `vendor` using your file manager. Do not type or copy-and-paste the minified libraries.** The downloaded folder already contains them.

No changes to `app.py` are needed. Flask already serves files in `static`.

<br>

### Here's what your files should look like now

| File or folder | Job |
|---|---|
| `app.py` | Same Python back end as Lesson 6 |
| `requirements.txt` | Flask dependency |
| `static/index.html`, `style.css`, `script.js` | Your complete Lesson 6 page |
| `static/dashboard.html` | New dashboard structure and content |
| `static/dashboard.css` | Our dashboard customisations |
| `static/dashboard.js` | Dashboard form and browser counter |
| `static/vendor/adminlte.min.css` | AdminLTE styles, including its compiled Bootstrap styles |
| `static/vendor/adminlte.min.js` | AdminLTE interface behaviour |
| `static/vendor/bootstrap.bundle.min.js` | Bootstrap JavaScript bundle, including Popper |
| Other files in `static/vendor` | Licence and version information; keep these |

The exact complete application files are also in [lesson-7-reference](lesson-7-reference/). That folder is for comparison and recovery, not a second place to run Flask.

<br>

### 1B. Open your dashboard

Open **http://127.0.0.1:5000/static/dashboard.html**.

Hard-refresh if necessary: **Ctrl+Shift+R** on Windows, **Command+Shift+R** on Mac.

Explore these parts:

1. A dark sidebar and a colourful banner.
2. Three statistic boxes.
3. A working generator and result panel.
4. A mission card with an example progress indicator.
5. A collection table.
6. Help questions that open and close.

Try **Menu** to toggle the sidebar. On a narrow screen, open the sidebar with Menu before choosing a section. Use Menu or the outside overlay to close it if it covers the page.

<br>

### 1C. Know which information is live

| Component | Where its value comes from | What changes it? |
|---|---|---|
| Generated item | Python's random choices | A successful request to `/api/generate` |
| Nickname and result colour | Browser form controls | Your input, applied by JavaScript |
| Items forged on this page | JavaScript variable in this page | Each successful generation; refresh resets it |
| Featured discoveries: 3 | Number typed into HTML | Editing HTML; it does not count rows automatically |
| Possible names: 25 | Number typed into HTML, based on 5 × 5 choices | Editing HTML; it is not calculated live |
| Mission progress: 60% | Example value typed into HTML | Editing HTML; it does not measure your progress |
| Collection table | Example rows typed into HTML | Editing HTML; generation does not add rows |

<br>

### Checkpoint 1

Generate twice. **Items forged on this page** should show `2`. Refresh: it should return to `0`.

Your browser is keeping that counter in memory. There is no database or saved history.

**You now have a dashboard installed.** Record your checkpoint and continue at your own pace.

<br>

---

## Chunk 2: Make it your dashboard

**Goal:** make three small changes you understand.

### 2A. Choose a theme

Choose something you enjoy: a space station, football club, music studio, wildlife centre, game inventory, or cooking laboratory.

Open `static/dashboard.html` and change:

1. The `<title>` text, which appears in the browser tab.
2. `FORGE CONTROL`, the sidebar's brand text.
3. `Make extraordinary things.`, the main heading.
4. The sentence under that heading.

Change text between tags. Keep the tags, classes, and IDs.

**Save and refresh.** Check that the tab, sidebar, and banner now match your theme.

<br>

### 2B. Change the banner colour

Open `static/dashboard.css`. Near the top, find:

```css
:root { --forge-accent: #6d28d9; }
```

Replace `#6d28d9` with `#047857`. Save and refresh.

`--forge-accent` is a CSS custom property: a named value that our CSS reuses. Here it changes the middle of the banner gradient and the progress accent where the browser supports it. It does not recolour every AdminLTE component.

Choose your own colour if you wish. Keep the white heading readable.

<br>

### 2C. Change a component's appearance

In `dashboard.html`, find the first statistic box:

```html
<div class="small-box text-bg-primary h-100 mb-0">
```

Change only `text-bg-primary` to `text-bg-danger`.

Save and refresh. The first box changes from blue to red. These reusable Bootstrap colour classes are available through the bundled AdminLTE CSS.

**Do not edit anything in `static/vendor`.** Make your custom CSS changes in `dashboard.css`, which loads after the library stylesheet.

<br>

### Checkpoint 2

Your page has your own title, banner wording, and colour choice. The generator still works.

Record one HTML change and one CSS change:

> I changed ___ in ___ because ___. The visible effect was ___.

<br>

---

## Chunk 3: Choose the component you actually want

**Goal:** understand that a dashboard is a collection of reusable parts. You do not have to use all of them in your future project.

For today, adapt one component inside the working sample. You can leave the others as examples.

| Choose this component | It could become... | Find these markers in `dashboard.html` |
|---|---|---|
| Mission card | Training goal, recipe instructions, quest, album brief | `START MISSION` to `END MISSION` |
| Collection table | Team roster, track list, species catalogue, inventory | `START COLLECTION` to `END COLLECTION` |
| Help panel | Game rules, safety guidance, FAQs | `START HELP` to `END HELP` |
| Statistic boxes | A small overview of useful numbers | `START STATS` to `END STATS` |

The HTML comments are landmarks for your editor. They do not appear on the page.

<br>

### Option A: Adapt the mission card

1. Find `<!-- START MISSION -->`.
2. Change `Today's mission`, the badge, the heading, and the paragraph.
3. Replace the three list items with three useful instructions for your theme.
4. Change `value="60"` to `value="30"` in the `<progress>` element.
5. Change both visible `60%` labels in that component to `30%` so the label and value agree.
6. Keep the explanation that the progress value is an example.

**Example:** a space station's mission is to catalogue three fictional planets. A sports dashboard's mission is to plan three training drills.

<br>

### Option B: Adapt the collection table

1. Find `<!-- START COLLECTION -->`.
2. Rename its heading and introductory sentence.
3. Change the three column headings and the content of all three rows.
4. Update the `<caption>` so it describes your table.
5. Keep `<thead>`, `<tbody>`, `<tr>`, `<th>`, and `<td>` in place.

**Example:** use `Track`, `Artist`, and `Mood` for a fictional music collection. Use invented or public information rather than classmates' personal data.

If you add a fourth row, also change the static `Featured discoveries` statistic to `4` and its label to match your new content. It does not update itself.

<br>

### Option C: Adapt the help panel

1. Find `<!-- START HELP -->`.
2. Keep the existing technical explanations, or rewrite them accurately in your own words.
3. Add one new complete `<details> ... </details>` block inside the card body.
4. Write a question in `<summary>` and its answer in `<p>`.
5. Test it using Tab and Enter or Space.

**Example:** "Are my generated items saved?" Answer: "No. This version shows the current result, and the counter resets when the page reloads."

<br>

### Option D: Adapt the statistic boxes

1. Find `<!-- START STATS -->`.
2. Keep `id="session-count"` and its meaning: successful generations on this page.
3. Reword that box for your theme, such as `Discoveries generated on this page`.
4. Change the second and third boxes to useful example information for your idea.
5. Clearly label invented values `Sample data` or `Example value`.

Do not relabel the counter as "online users" or "saved items": the code does not measure those things.

<br>

### Here's what your files should look like now

The folder structure has not changed. Your own edits are in `static/dashboard.html` and `static/dashboard.css`. You have not needed to edit Python or the vendor files.

Compare complete originals here if something breaks:

- [Complete dashboard HTML](lesson-7-reference/static/dashboard.html)
- [Complete dashboard CSS](lesson-7-reference/static/dashboard.css)
- [Complete dashboard JavaScript](lesson-7-reference/static/dashboard.js)

These are working reference files, not a requirement that everyone's design look identical.

<br>

### Checkpoint 3

Show your adapted component to a partner. Explain:

> I chose the ___ component because my user needs ___.

Point to the HTML responsible for one visible part. Test the generator again.

**Reusing components later:** AdminLTE components need the AdminLTE stylesheet. Some interactive components also need its JavaScript and Bootstrap's bundle. Our custom components need `dashboard.css` too. Do not simply paste them into Lesson 6's page and load all its styles together: both stylesheets use names such as `.card`, so rules can conflict. Start from the dashboard shell when building your own dashboard page.

<br>

---

## Chunk 4: Front end and back end — follow one request

**Goal:** distinguish the interface from the program that supplies its data.

Both run on your laptop today, but they have different jobs.

| Part | Runs where? | Responsibility in this project |
|---|---|---|
| HTML | Browser: front end | Structure, headings, form, table |
| CSS, including AdminLTE styles | Browser: front end | Colour, layout, spacing, responsive appearance |
| JavaScript, including AdminLTE behaviour | Browser: front end | Form handling, requests, page updates, sidebar interaction |
| Python and Flask | Python process started in the terminal: back end | Serve local files and respond to `/api/generate` with an item |

**AdminLTE does not replace Flask.** It does not create a database, logins, or real administrator permissions. The word "admin" describes the style and purpose of the template.

<br>

### 4A. Inspect the response

Open **http://127.0.0.1:5000/api/generate** in a new tab.

You should see JSON similar to:

```json
{"item": "Glowing Shield"}
```

Your item may differ. Refresh the tab: Python makes another random choice. A random result can repeat.

This route returns data, not your dashboard HTML. Opening it directly does not increase the dashboard's browser counter.

<br>

### 4B. Read the connection

Open `static/dashboard.js`. Find:

```javascript
const response = await fetch("/api/generate");
```

Follow the sequence:

1. You submit the form in the browser.
2. JavaScript prevents navigation and checks the nickname.
3. JavaScript sends a **GET request** to `/api/generate`.
4. Flask calls `generate()` in `app.py`.
5. Python chooses an adjective and item, and Flask returns JSON.
6. JavaScript reads that JSON and updates the result text, colour, and counter.

**The request does not send your nickname or colour to Python.** JavaScript uses those values in the browser after receiving the item. Changing the colour does not change Python's random choices.

<br>

### 4C. Prove the difference

1. Generate once and keep the page open.
2. Stop Flask with Ctrl+C in the terminal.
3. Without reloading the page, open and close a help question. It still works because it is browser behaviour.
4. Try generating again. You should see a helpful error message: the back end is unavailable.
5. Restart Flask with the same command and try again. Generation should work.

Do not refresh while Flask is stopped: Flask also serves the HTML, CSS, and JavaScript files when the browser requests them.

<br>

### Checkpoint 4

Complete the request trace in your notes. Explain why the help can work while Flask is stopped but a new generated item cannot.

<br>

---

## Chunk 5: Test your dashboard

**Goal:** collect evidence that your changes work.

Use the test table in [lesson7_notes.md](lesson7_notes.md). Record what actually happened; use **not built yet** for a feature you have not reached.

1. Test both Fire orange and Forest green results.
2. Test a blank nickname, spaces only, and submission with Enter.
3. Check that the live counter increases only after successful generation and resets on refresh.
4. Narrow your browser to around 375 pixels. Cards should stack. A wide table may scroll inside its own container; the whole page should not need sideways scrolling.
5. Navigate with Tab. Check visible focus and keyboard use of the form and help.
6. Use the Menu button to open and close the sidebar.
7. If permitted, disconnect Wi-Fi, keep Flask running, and refresh the page. The dashboard, menu, and generator should still work. Reconnect afterwards. Do not use DevTools' Offline mode for this test: that can also block requests to your local Flask server.
8. Complete the stopped-server test in chunk 4 if you reached it.

**Offline means no external internet is needed after setup. The local Flask server must still be running.** Installing Flask and initially downloading the lesson files may need internet; your teacher can distribute the asset folder offline.

<br>

### Checkpoint 5: Submit your work

Save your files. Submit through the class's normal method:

- One screenshot of your personalised dashboard.
- Your completed notes, including your chosen component and front-end/back-end explanation.
- Your changed files if your teacher requests them. Do not include your virtual environment.

No GitHub account, commit, or push is required.

<br>

---

## Extensions: choose one after the core checkpoints

### Extension A: Make the back end match your theme

In `app.py`, replace the five adjectives and five items with suitable words for your theme. Keep the variable names and route unchanged. Use five distinct values in each list so the `25` combinations label remains accurate.

Save, check the Flask terminal for errors, and generate several times. If the development server has not reloaded, stop and restart it.

**Explain:** how is this different from changing the static collection table?

<br>

### Extension B: Create a focused second dashboard

1. Copy `dashboard.html` to `my-dashboard.html` in `static`.
2. Keep all stylesheet and script links, the page shell, the generator, and the `session-count` element.
3. Remove the block between `START COLLECTION` and `END COLLECTION`, including its section tags.
4. Remove the sidebar list item that links to `#collection`.
5. Change the mission card's `href="#collection"` link to `href="#workshop"` and change its text.
6. Adapt the remaining components for a focused purpose.
7. Open **http://127.0.0.1:5000/static/my-dashboard.html** and test every link and the generator.

This is how you begin selecting parts instead of keeping a whole demo page. A script that expects an element can break if that element is removed; that is why you kept the generator and counter.

<br>

### Extension C: Investigate the network request

Open browser developer tools, choose Network, and generate an item. Inspect the `/api/generate` request.

Record the method, response status, and response JSON. Find evidence that the request does not contain your nickname or selected colour. Compare it with a request for `/static/dashboard.css`: what type of content does each response contain?

<br>

---

## If you get stuck

| Symptom | First thing to check |
|---|---|
| Plain, unstyled dashboard | Copy `static/vendor` completely; visit `/static/vendor/adminlte.min.css` and check it returns CSS |
| Lesson 6 page appears | Dashboard URL ends in `/static/dashboard.html`, not `/static/index.html` |
| Menu does nothing | Check that both vendor JavaScript files load and that script tags remain at the bottom |
| Dashboard returns 404 | Correct project running? Is `dashboard.html` directly inside `static`? |
| Generator fails | Flask running? Open `/api/generate` directly; inspect terminal errors |
| Form or count stops working | Check protected IDs and browser Console errors; use `dashboard.js`, not Lesson 6's `script.js` |
| Styles look strange | Dashboard loads `adminlte.min.css` and `dashboard.css`, not Lesson 6's `style.css` |
| Changes do not appear | Save, check the running project's folder, then hard-refresh |
| Port already in use | Stop your earlier Flask server; or use `--port 5001` and replace 5000 in all browser addresses |
| `No module named flask` | Activate the correct environment; install requirements while online |
| Cannot download files | Ask your teacher for the predownloaded lesson folder; do not install npm |
| Image or font missing in your own extension | Use a local file and local path; external URLs need internet |

**Protected IDs:** `generator-form`, `generate-button`, `nickname`, `theme`, `result-card`, `theme-badge`, `result`, `result-heading`, `nickname-help`, and `session-count`. Keep each ID once per page. Keep link targets too, or update the links that point to them.

**Recovery:** back up your edits, then replace only the broken file using [lesson-7-reference](lesson-7-reference/). Reapply your own changes one at a time.
