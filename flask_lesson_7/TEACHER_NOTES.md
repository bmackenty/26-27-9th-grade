# Lesson 7 teacher notes

## Teaching intent

Students get a complete working dashboard quickly, then personalise it and adapt one component. The key conceptual distinction is between a front-end template and a back-end service. This is a component-selection lesson, not a framework-build or authentication lesson.

Use 60–90 minutes. Students who need longer should finish chunks 0–2 and applicable tests, then continue next lesson. Early finishers complete component adaptation, request tracing, and an extension. The student lesson uses horizontal rules, explicit HTML breaks, short tasks, and checkpoints so GitHub does not collapse all spacing.

## Exact continuity with Lesson 6

Source reviewed: https://github.com/bmackenty/26-27-9th-grade/blob/main/flask_lesson_6/LESSON_6.md

The top-level Lesson 6 files are its starting point. This package instead uses the files in `flask_lesson_6/lesson-6-reference` as the completed baseline. `app.py`, `requirements.txt`, and the original three static files are copied unchanged. The dashboard is a new page, using the existing `/api/generate` endpoint. No new Python routes are required.

Lesson 6's personalised gallery, colours, and text will differ from the baseline. Students back up their work before replacement. They can later reapply selected wording and content. Do not promise the supplied baseline preserves their personal changes.

The original lesson's request to commit to GitHub is superseded: students only download or receive files, work locally, and submit through the normal class channel. They do not need GitHub accounts.

## Before class

1. Extract this package. Upload the **extracted `flask_lesson_7` folder**, including `static/vendor`, to the root of the class repository alongside `flask_lesson_6`. Uploading only the ZIP will not make the lesson links browsable.
2. From a signed-out browser, confirm `flask_lesson_7/LESSON_7.md` opens. Keep the repository public for account-free downloads.
3. Also distribute the ZIP or extracted folder through your normal class system or local file transfer. Students can use this if GitHub is slow. The whole package is small; there are no remote fonts, images, icon fonts, or chart libraries.
4. Confirm students have Python and Flask installed in their virtual environments **before an offline lesson**. Local dashboard assets remove CDN dependency, but they do not install Python packages offline. A machine without Flask still needs an installation opportunity or a separately prepared compatible offline Python package bundle.
5. Run the app and check `/static/index.html`, `/static/dashboard.html`, and `/api/generate` on a student-like machine.
6. Keep a projected copy of the dashboard visible to establish the visual target.

The application runs unchanged from the package's top-level folder if a student needs a clean recovery project. They must activate or create a suitable virtual environment and run Flask in that folder. Do not copy virtual environments between machines.

## Why this implementation

AdminLTE **4.0.0** is pinned deliberately for a reproducible lesson. Its compiled CSS includes Bootstrap styling. Bootstrap **5.3.3** bundle and AdminLTE JS are included locally; no jQuery is needed for this version. Students do not run npm or compile anything. This is a fixed teaching bundle, not a claim that these are the newest releases.

Only the required files are included. Optional charts, maps, icon libraries, remote fonts, and other plugins have been omitted. The progress display uses native HTML. See `static/vendor/ASSETS.md` for exact sources, versions, hashes, and licences. Preserve the licence files when distributing.

The dashboard has its own CSS and JavaScript so Lesson 6's `.card` styling does not clash with AdminLTE's `.card`. The old page remains usable. Do not add `style.css` to the dashboard head.

## What students should learn

- A template supplies reusable interface components, not application logic or admin privileges.
- HTML structure and CSS classes can be adapted independently of a Flask endpoint.
- JavaScript can request JSON and update a page without navigating away.
- Data displayed in a dashboard can be static, calculated in the browser, or obtained from the back end. Those are different sources of truth.
- A successful visual design must still function at a narrow width and with keyboard controls.

## Answers and misconceptions

| Prompt | Expected explanation |
|---|---|
| Why do gallery/table rows stay the same? | They are static HTML; the script only updates the live result and counter. |
| Why does the counter reset? | It is a JavaScript variable in the current page, not a database or persistent browser storage. |
| Does changing theme change the generated item? | No; the request contains no theme. JavaScript changes the result card locally. |
| Does Python receive the nickname? | This application code does not send it. It is read and displayed in JavaScript. |
| Why does help still work after stopping Flask? | The already-loaded page uses native browser details/summary behaviour. A new API request needs Flask. |
| Why does refreshing fail after stopping Flask? | Flask also serves the static page and assets. |
| Is the dashboard secure admin software? | No. It has no authentication, authorisation, database, or protected admin operations. |
| Why 25 possible names? | Five distinct adjectives times five distinct items. The label is hand-entered, not linked to Python. |
| Why can a generated result repeat? | Independent random choices do not guarantee uniqueness. |
| Can students reuse only one component? | Yes, with its required styles and behaviour. Core work adapts one in place; extension B creates a reduced second page. |

Do not introduce sending categories or nicknames to Python during the core lesson: Lesson 6 explicitly deferred this, and the current task focuses on dashboard installation and front-end/backend clarity.

## Quick formative assessment

Ask students to point to one changed HTML element, one CSS rule, and the `fetch` call. Ask them which process computes the item and which process applies the nickname. A student who can name the languages but cannot trace the request needs another concrete demonstration.

Expected submission: screenshot, notes, and optionally changed files. No account setup or Git workflow. Extensions are optional, not required to demonstrate the core understanding.

## Scope and classroom operation

Run locally with the Flask development server. This sample does not implement real privileged administration. Do not present its styling as evidence of access control or deploy it as an actual admin service.

The built-in sample values are labelled. The generator is live. The counter measures successful generations in this page only, not unique items, visits, or users.

## Verification performed for this package

- All five Lesson 6 baseline files matched the published completed reference byte-for-byte.
- Flask returned HTTP 200 for both pages, the API, and all dashboard assets.
- All relative Markdown links, HTML local asset paths, anchor targets, and unique IDs passed checks.
- JavaScript syntax and generator logic passed checks using a DOM test harness and the actual Flask response: nickname display, colour selection, successful-only counter, spaces-only validation, request failure, button recovery, and retry.
- No external assets are referenced by either HTML page. Vendor CSS uses embedded data URLs for built-in artwork.
- Browser rendering, keyboard behaviour, sidebar interaction, and narrow-screen appearance were not visually verified because the browser runtime could not be installed in the preparation environment. Perform the pre-class browser check above; the student test list covers these checks explicitly.
