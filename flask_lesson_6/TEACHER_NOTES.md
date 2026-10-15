# Teaching Lesson 6

## Purpose and continuity

This is a visual HTML/CSS lesson built directly on the completed Lesson 5 reference from the class repository, retrieved 15 October 2026. Top-level application files are exact copies of that reference; the completed Lesson 6 example changes HTML and CSS only. Flask remains a JSON API, with vanilla JavaScript updating the browser. No Jinja, database, external images, CDN, or new framework is introduced.

The supplied syllabus names Tabler as the eventual component library. This lesson continues Lesson 5's existing local CSS to keep the changes inspectable and avoid a framework migration during a design lesson. Cards, reusable classes, and semantic structure prepare students to read component-library markup later.

Lesson 5 previewed category input being sent to Python. Explicitly tell students that this has been postponed to prioritise the requested visual work; the category feature is not included here.

## Before class

1. Upload the complete extracted `flask_lesson_6` folder to the root of the class repository. Keep the existing Lesson 5 folder.
2. Give students the link to `flask_lesson_6/LESSON_6.md`.
3. Run the completed example from `lesson-6-reference` and demonstrate the wide and narrow layouts. Explain that the gallery cards are static examples.
4. Demonstrate one replace operation and one append operation. Emphasise that snippets are not full files.
5. Students keep their existing virtual environments; they manually replace the five listed files after backing up. Avoid starting with the completed Lesson 6 reference.

## Pacing

For 60 minutes, keep whole-class explanation to about five minutes. Aim for a working reset, banner, gallery, one personal change, and a five-minute test/reflection finish. Students who do not reach expandable help resume it next lesson. For 90 minutes, aim for all six core chunks and one extension. The chunk estimates total approximately 65 minutes before extensions or extra debugging; do not present them as a universal 60-minute completion promise.

Students move on immediately after each checkpoint. Avoid stopping everyone for demonstrations already described in the instructions. At the final five minutes, everyone records their actual stopping point and a test result.

## Support

For students needing support, cover the unused chunks and focus on one file at a time. Have them locate the start and end tags before selecting code. Ask them to point to the visible change after saving. A working three-card gallery with one original card description and one explained style change is meaningful progress.

For confident students, require the same checkpoints and explanations, but allow quick independent completion. Extensions add layout reasoning, image handling, reusable selectors, and accessibility investigation. Speed alone is not evidence of understanding.

Use a brief oral check: Where is this card's HTML? Which selector gives it a gradient? Why does the gallery stay unchanged when the generator runs? What would break if you renamed `result` only in HTML?

## Evidence

Collect a screenshot, lesson6_notes.md, and updated source through the normal class workflow. Look for deliberate design choices, an intact form, responsive layout, and an explanation of one HTML and one CSS change. Do not grade decorative sophistication as a proxy for programming understanding. This is formative practice, not a complete MYP criterion assessment.

Follow the class's current AI mode. If Mode 2 is allowed, retain the course's before/after AI log: intention, attempt, best guess, answer in the student's words, verification, and change made. Supplied scaffolding is teacher-provided; students still explain their modifications.

## Source

Baseline: https://github.com/bmackenty/26-27-9th-grade/tree/main/flask_lesson_5/lesson-5-reference
