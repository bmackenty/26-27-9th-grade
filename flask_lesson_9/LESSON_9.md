# Lesson 9: Explore components and choose a pathway

Today you will explore ready-made interface components, learn about five directions for your next project, and plan an interface for a real purpose.

**Success means you can explain what your user needs, which components help, and what programming still needs to be written.** You do not need to build a complete pathway project today.

## Choose your pace

Allow 75–90 minutes. Work in order. After a checkpoint passes, continue independently. Pause for your teacher's pathway presentation when asked; you can return to your current chunk afterwards.

| Chunk | Task | Guide |
|---|---|---|
| 0 | Open your existing project | 5 minutes |
| 1 | Add three example files | 10 minutes |
| 2 | Explore and test components | 15–20 minutes |
| 3 | Understand the five pathways and choose | 15–20 minutes including slides |
| 4 | Build a small interface prototype | 20 minutes |
| 5 | Test, explain and submit | 10–15 minutes |

**Minimum target:** checkpoints 0–3, then submit your notes using chunk 5. Your evidence is a working gallery, three component observations, and a reasoned pathway choice with a sketch.

**Full target:** checkpoints 0–5, including two purposeful components in your new prototype.

**Finished early?** Complete an extension. More components are not automatically a better design.

Use [lesson9_notes.md](lesson9_notes.md): copy its headings into your usual class document. Keep it open beside VS Code. Record your checkpoint and next action before stopping.

<br><br>

---

## Chunk 0: Open your own project

1. Open the Flask project you used in Lesson 8 in VS Code.
2. In the Explorer on the left, find `app.py` and the `static` folder.
3. Open **Terminal → New Terminal**. Use `dir` on Windows or `ls` on Mac to check that the terminal is in the folder containing `app.py`.
4. Activate your existing environment. For an environment named `.venv`, use the appropriate command:

| Terminal | Command |
|---|---|
| macOS/Linux | `source .venv/bin/activate` |

Use your actual environment name if different. If activation is blocked or the environment is missing, ask your teacher for setup help. Do not overwrite your project to solve an environment problem.

5. If this project's server is already running, leave it running. Otherwise run:

```bash
python -m flask --app app run --debug
```

6. Open `http://127.0.0.1:5000/static/dashboard.html` in your browser. If Flask displays another port, use that port throughout this lesson.
7. Try your existing generator with an invented nickname. Confirm that a result appears.

### CHECKPOINT 0 — Existing project works

**Show:** your dashboard loads and its generator produces a result.

**Say:** “Flask serves my files. The browser displays HTML and CSS and runs JavaScript.”

**If not yet:** check the terminal for an error and check the URL. Ask for help before changing existing files. If setup takes longer, you can use a partner's gallery for chunks 2–3 and record that in your notes.

**When passed:** write `0 passed` and continue.

<br><br>

---

## Chunk 1: Add three files — replace none

### 1A. Get the lesson examples

1. Open the [class repository](https://github.com/bmackenty/26-27-9th-grade).
2. On the repository's main page, click **Code → Download ZIP**.
3. Extract it: just double-click on Mac.
4. Open the extracted repository, then `flask_lesson_9`, then `add_to_static`.

### 1B. Copy only the new files

1. Select these three files in `add_to_static`: `components.html`, `pathways.html`, `my_pathway.html`.
2. Copy them.
3. In your existing project, open the `static` folder.
4. Paste the three files **inside** `static`, beside `dashboard.html`.
5. If asked to replace a file, stop and check: these may already be installed. Keep your edited `my_pathway.html`.

Do not put the `add_to_static` folder inside `static`. Do not copy a new `app.py`, CSS file, JavaScript file or vendor folder. These pages reuse the libraries you already have. They contain their own small page styles so your dashboard styling does not interfere.

**Copy/paste alternative:** open each of the three files in [add_to_static](add_to_static/) on GitHub and click **Raw**. In VS Code, right-click your local `static` folder, choose **New File**, type the exact matching filename, then paste the entire Raw file and save. Repeat three times. Do not copy the GitHub page or Markdown fences.

### Here's what your files should look like now

| Location | Status |
|---|---|
| `app.py` | Existing, untouched |
| `static/dashboard.html`, `dashboard.css`, `dashboard.js` | Existing, untouched |
| `static/vendor/adminlte.min.css` | Existing, reused |
| `static/vendor/adminlte.min.js` | Existing, reused |
| `static/vendor/bootstrap.bundle.min.js` | Existing, reused |
| `static/components.html` | New: component gallery |
| `static/pathways.html` | New: five-pathway reference |
| `static/my_pathway.html` | New: your editable prototype |

Earlier files and vendor licences remain where they are.

### 1C. Open the gallery

1. In the browser address bar, enter `http://127.0.0.1:5000/static/components.html`.
2. You should see **Component explorer**, a row of component links, and examples below.
3. Click **Five pathways** at the top. You should see all five pathway cards.
4. Click **My prototype**. You should see a blue notice and an undecided pathway.
5. Click **Components** to return.

GitHub displays source code; Flask displays the working page. Do not double-click an HTML file or expect GitHub's file preview to run it.

### CHECKPOINT 1 — Three new pages work

**Show:** all three pages open, have styling, and link to each other.

**Check:** your original dashboard still works. You have replaced **zero** existing files.

**If not yet:** 404 means check filenames and placement; an unstyled page means check `static/vendor`. A URL containing `/static/add_to_static/` means the files are one folder too deep.

**When passed:** write `1 passed` and continue.

<br><br>

---

## Chunk 2: Explore the component toolbox

A **component** is a reusable interface part. AdminLTE adds dashboard components and styling to Bootstrap. Some examples only display content; others use the supplied JavaScript to respond to clicks.

### 2A. Take a guided tour

In the gallery, use the component links near the top:

1. Open **Cards**. Click **Collapse / expand** twice. The card body should hide, then return.
2. Open **Modal**. Click **Open sample modal**, then press **Escape**. It should open, then close.
3. Open **Tabs**. Click **Test**, then **Plan**. The visible text should change.
4. Open **Forms**. Leave the required name empty and click **Validate locally**. The browser should ask for a name. Enter an invented name and try again. Read the message: nothing was sent or saved.
5. Open **Grid and utilities**. Narrow the browser; the two columns should stack. Widen it; they should sit side by side once the window is at least 768 pixels wide.
6. Explore two more components of your choice. Read the description before using them.

The sample numbers are fixed HTML. The table does not automatically sort. The chat is not a real messaging system. Charts and other plugins need extra libraries; see the final gallery section.

### 2B. Look behind one component

1. Find **Small boxes**.
2. Click **Show HTML to copy** below its example.
3. Find `class="small-box text-bg-primary"`. These classes select the ready-made appearance.
4. Find the text `24`. That is why the sample shows 24. It is not reading a database.
5. Find `href="#tables"`. This makes the link jump to the gallery's table section.

Record three components in your notes: name, what you tested or observed, and one useful purpose. At least one must be interactive.

### CHECKPOINT 2 — You can use and explain components

**Show:** a working interactive component and three completed observation rows.

**Say:** explain the difference between displaying a score and calculating a score.

**If not yet:** choose **Modal**, **Tables**, and **Small boxes**. Test the modal, read each description, and write one sentence per component. If buttons do nothing, check that both vendor JavaScript files exist and refresh.

**When passed:** write `2 passed` and continue to the pathway introduction.

<br><br>

---

## Chunk 3: Meet the five pathways

**Teacher presentation:** your teacher will introduce the five pathways using their slides. Keep your notes open. If you reach this section before the presentation, read the pathway page and complete the comparison; revisit your choice after the slides.

1. Click **Five pathways** at the top of the gallery.
2. Read all five cards. The same explanations are in [PATHWAYS.md](PATHWAYS.md).
3. For each pathway, read its question and small starting idea. These are possible directions, not a complete project brief.

| Pathway | Main thinking | Small starting idea |
|---|---|---|
| Computer Science | Algorithms, logic and efficiency | Compare ways of searching a list |
| Computational Biology | Models and evidence about living systems | Model population change over a few days |
| Computing in Business | Data, decisions and risk | Compare costs and income for a school stall |
| Game Programming | Rules, choices and feedback loops | Design a three-turn risk-or-bank game |
| Practical Computing | Useful tools and automation | Organise three homework tasks |

A pathway is **not a difficulty level**. A polished interface alone does not make a successful project. All pathways require investigating a need, designing, building, testing and explaining decisions.

### 3A. Try two possibilities

1. Choose two pathways that interest you.
2. Complete the **Try on paper** task from each pathway card. Spend about three minutes on each. Rough notes are enough.
3. In your notes, name your first preference and backup.
4. Explain what interests you about the first pathway and how it differs from the backup.
5. Identify a user and one small problem. Example: “A school stall organiser needs to compare the profit from two products.”
6. Choose two gallery components that would help that user. Explain each choice. Example: “A table compares costs; an info box highlights calculated profit.”
7. Sketch where the two components would go. Label any sample values.
8. Write one feature that still needs Python or JavaScript. Example: “Calculate profit from the entered income and costs.”

For this lesson, follow your teacher's AI mode. Under Mode 2, explain your own attempt first, ask for guidance, explain the response in your own words, predict and check, and record the use. A pathway's longer-term AI emphasis does not change today's permission.

### CHECKPOINT 3 — Your choice has a reason

**Show:** first preference, backup, two short paper trials, user/problem statement, two component choices and a sketch.

**Say:** “I chose ___ because ___. My user needs ___. The interface can show ___, but I still need to program ___.”

**If not yet:** use one small starting idea from the pathway page. Keep the problem to one sentence. Ask a partner to tell you what they think your program will do; revise if unclear.

**Minimum target reached:** if you need more time, go to chunk 5 and submit your notes. Record `Next: chunk 4`. You are not required to rush through the prototype.

**Ready to build?** Continue now; you do not need to wait for classmates.

<br><br>

---

## Chunk 4: Build your own small prototype

A **prototype** is an early version used to test an idea. Today yours demonstrates the interface; it does not need new Flask routes or saved data.

### 4A. Describe your plan

1. In VS Code, open `static/my_pathway.html`.
2. Press **Ctrl+F** (Windows) or **Command+F** (Mac). Search for `EDIT YOUR PLAN BELOW`.
3. Change `My pathway: undecided` to your chosen pathway.
4. Edit the three paragraphs underneath: intended user, problem, and eventual program action.
5. Keep the notice that says this is an interface prototype with fictional data.
6. Save. Open `http://127.0.0.1:5000/static/my_pathway.html` and refresh. Read your plan on the page.

### 4B. Add your first component

1. Return to the gallery in a second browser tab.
2. For a straightforward first component, choose **Small boxes**, **Tables**, **Lists**, or **Progress**.
3. Open **Show HTML to copy** beneath your chosen component.
4. Select and copy the entire code block, from its first opening tag to its final closing tag.
5. Return to `my_pathway.html` in VS Code. Search for `START MY COMPONENTS`.
6. Paste on the blank line after `<!-- Paste your chosen component HTML on the blank line below. -->`, before `<!-- END MY COMPONENTS -->`.
7. Save and refresh your prototype. The component should appear beneath your plan.
8. Change its visible labels and sample numbers to fit your idea. Keep opening and closing tags intact.
9. If you copied the small box, change `href="#tables"` to `href="components.html#tables"`. Its link now opens the gallery's table example; label it “View table example”. The prototype has no `tables` section of its own.

**Pause and check:** your first component appears, its text fits your plan, and any link has a meaningful destination. Fix this before adding another.

### 4C. Add a second component

1. Choose a second component with a different purpose. A table plus an info box is a useful combination.
2. Copy its complete code block from the gallery.
3. Paste below the first component and above `<!-- END MY COMPONENTS -->`. Do not paste inside the first component.
4. Change the visible content to fit your plan, save, and refresh.
5. If using an interactive component, test its action immediately.

For a modal, copy its **button and window together**. The target `#sample-modal` must match the window ID `sample-modal`. Use each interactive example only once unless you also rename all connected IDs and references. IDs must be unique on a page.

The starter includes initialization for tooltips/popovers, the demonstration toast, and the demonstration form. If copying those examples, keep their complete blocks and IDs. These examples still do not save or send data.

### Here's what your files should look like now

| File | What you changed |
|---|---|
| `static/my_pathway.html` | Your plan and two selected components |
| `static/components.html` | Reference gallery, unchanged |
| `static/pathways.html` | Reference pathway guide, unchanged |
| All pre-existing project files | Unchanged |

### CHECKPOINT 4 — Two components serve a purpose

**Show:** two personalised components beneath your plan, with sample data clearly labelled.

**Say:** explain the purpose of each component and identify one class used to style it.

**If not yet:** complete one component first. Compare its opening and closing tags with the gallery. You can keep the second component as a next step and record exactly where you stopped.

**When passed:** continue to the tests.

<br><br>

---

## Chunk 5: Test, explain and submit

### 5A. Record actual results

Use the table in your notes. Write what actually happened, not just “done”. Mark prototype tests `not built yet` if you stopped at checkpoint 3.

| Test | Expected result |
|---|---|
| Open gallery, pathways and prototype links | Each page opens with styling |
| Use gallery modal; press Escape | Opens, then closes |
| Use existing dashboard generator | A result appears |
| Read pathway choice and explanation | User, problem and reason are clear |
| View your prototype | Personal plan and two purposeful components |
| Narrow prototype to about 375 pixels | Text remains readable; tables scroll if needed |
| Use Tab and Enter | Links/buttons are reachable and have visible focus |
| Test any copied interactive component | Its stated action works |
| Refresh prototype | Saved HTML changes remain; no claim of stored user data |

For a precise width in Chrome/Edge: open developer tools with **Ctrl+Shift+I** or **Command+Option+I**, click the phone/tablet icon, choose **Responsive**, and set width to `375`. Close developer tools afterwards.

### 5B. Explain in your own words

1. Why does your chosen pathway interest you?
2. How does each selected component help your user?
3. What works now, and what is only sample content?
4. What should the program do next that HTML alone does not implement?

### CHECKPOINT 5 — Ready to submit

Submit through the normal class method:

- Your notes, including pathway preference, backup, sketch, checkpoint reached and test results.
- One screenshot: your prototype if built, otherwise the gallery component you tested.
- Your `my_pathway.html` file if your teacher requests code.

No student GitHub account is required. Do not submit your environment folder. If unfinished, write your exact next action, for example: “Next: paste the complete table below my small box.”

<br><br>

---

## Extensions — choose one after your core work

### A. Explain a rule with a modal

Copy the gallery modal into your prototype. Change its heading and text to explain a game rule, scientific assumption or calculation. Test its opener, Close button and Escape key. Explain why the information belongs in a dialog.

### B. Compare two designs

Sketch a second layout for the same user and problem. Ask a partner to locate the most important information in both designs. Record which they preferred and why. Improve your prototype using that evidence.

### C. Plan the program behind the page

Write the input, processing and output for one feature. Work one example by hand. Add a normal input and an edge case to your test plan. Do not add a new API route until you have discussed the plan with your teacher.

## Troubleshooting

| Problem | First check |
|---|---|
| 404 | File is directly in `static`; filename matches exactly; correct Flask project running |
| No styling | Existing `static/vendor/adminlte.min.css` is present |
| Modal/tabs do nothing | Existing Bootstrap bundle is present; copied complete component; target matches ID |
| Card controls do nothing | Existing `adminlte.min.js` is present |
| New content disappears | Save in VS Code, then refresh the correct browser page |
| Old content remains | Hard-refresh with Ctrl+Shift+R or Command+Shift+R |
| Layout breaks after paste | Check complete opening/closing tags and paste before END MY COMPONENTS |
| Second modal opens the first | Duplicate IDs: rename the copy's IDs and every matching reference |
| Flask will not start | Read terminal error; check environment and whether another server is already running |

## Optional references

- [AdminLTE demo](https://adminlte.io/themes/v4/) — internet required; may show a newer version or extra plugins.
- [Bootstrap 5.3 components](https://getbootstrap.com/docs/5.3/components/accordion/) — navigate using its component list.

Use the local examples for this lesson. Do not replace the existing vendor files with a different version.
