# Flask Lesson 5 — start here

The files at the top of this folder are the **completed Lesson 4 application**.
Start from those files even if you did not finish Lesson 4. Then follow [Lesson 5](LESSON_5.md).

## Copy the completed Lesson 4 files manually

1. Open your existing `my_first_web_app` folder in VS Code.
2. Back up your own `app.py` and `static` folder first, so you can restore your theme later.
3. On GitHub, open each file below. Use **Raw** or the copy button to copy only the code, not the GitHub page. Select all the old code in the matching local file and paste the complete replacement. Save each file.

| Open on GitHub | Paste into your local file |
|---|---|
| [app.py](app.py) | `my_first_web_app/app.py` |
| [index.html](static/index.html) | `my_first_web_app/static/index.html` |
| [style.css](static/style.css) | `my_first_web_app/static/style.css` |
| [script.js](static/script.js) | `my_first_web_app/static/script.js` |

Create missing files or the `static` folder if needed. Keep your existing `.venv` folder. Do not put project files inside `.venv`. There is no need to clone, pull, or reinstall Flask if your environment already works.

## Run your project

Open a terminal in `my_first_web_app`. Activate the environment:

macOS:
```bash
source .venv/bin/activate
```
Windows **Command Prompt**:
```bat
.venv\Scripts\activate.bat
```
Then:
```bash
python -m flask --app app run --debug
```
Open **http://127.0.0.1:5000/static/index.html**. Use this Flask address, not Live Server, GitHub Pages, or a `file:///` address. If port 5000 is busy, add `--port 5001` and use 5001 in the address.

If starting on a new computer, create the environment first with `python3 -m venv .venv` (macOS) or `py -3 -m venv .venv` (Windows), activate it, then run `python -m pip install Flask`.

## What is in this folder?

- Top-level `app.py` and `static/`: completed Lesson 4 baseline.
- [LESSON_5.md](LESSON_5.md): student instructions, 60 minutes.
- [lesson-5-snippets](lesson-5-snippets): small additions used during the lesson.
- [lesson-5-reference](lesson-5-reference): complete expected code after Lesson 5, before personalisation. Compare files if you get stuck; do not copy this version before starting the activities.
- [TEACHER_NOTES.md](TEACHER_NOTES.md): pacing, answers, and checks.

The JSON key is `item` in both Python and JavaScript. Random results can repeat.

## For the teacher: upload to GitHub

Extract this ZIP and upload the `flask_lesson_5` folder into your repository using Add file → Upload files. Keep its structure intact; students start with this README. Upload the extracted files, not only the ZIP, so each source file is easy to open and copy. This repository is a source-code handout; GitHub Pages does not run Flask.

No virtual environment, student data, or account credentials are included.
