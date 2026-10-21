# Lesson 8 teacher notes

## Purpose and continuity

A 75–90 minute practical lesson continuing the actual Lesson 7 dashboard. Focus: deliberate visual choices, reusable CSS selectors, component reuse, responsive layout, and testing. Python remains unchanged. Students edit two files, dashboard.html and dashboard.css.

The attached syllabus supports use of professional components, separation of front-end files from Flask JSON routes, design reasoning, and oral explanation. Use the short sketch review as a formative design gate. This lesson is a focused skills activity, not a replacement for the full pathway project proposal or formal assessment. Use the course's current AI-as-tutor rules and log any AI help; students should explain their own changes.

## Suggested delivery

- 0–10 minutes: verify Lesson 7 baseline; distribute extracted files where useful.
- 10–20: audience, two-card sketch, quick teacher review, notice.
- 20–35: two cards; demonstrate row and column boundaries.
- 35–50: custom CSS; predict and compare colour and spacing changes.
- 50–65: modal button, window, and matching IDs.
- 65–80: personalisation, keyboard/mobile testing, partner feedback.
- Remaining time: explain one rule orally or attempt an extension.

For 60 minutes, use chunks 0–3 plus relevant testing as the minimum outcome. Continue the modal next lesson. Faster students proceed independently after passing checkpoints.

## Preparation

Upload the complete flask_lesson_8 folder to the repository root, including starter and completed vendor directories. Markdown links are relative and work when the structure is retained. Both application folders include the original local AdminLTE 4.0.0 and Bootstrap 5.3.3 assets and licence files; no runtime CDN or npm installation is needed. Original asset provenance remains in each vendor/ASSETS.md.

Students with working Lesson 7 projects retain them. The starter is only a replacement baseline when needed. It is copied from Lesson 7's complete reference rather than its top-level Lesson 6 files. The completed example adds only the lesson snippets to that baseline. Existing Lesson 7 labels remain in the application because it is a continuation of that page.

The completed example uses the default green pair. Purple is an explicitly permitted student experiment. No backup instructions are included.

## Common teaching points

A class is reusable; an ID is unique. Preserve generator IDs. Insert entire blocks at the named comments, not inside existing forms. The modal belongs outside the dashboard wrapper, immediately before the Bootstrap script. Keep existing script order.

The two new cards contain sample content, not persisted data. The old Featured discoveries statistic still describes the old three-row collection. The live browser counter resets on reload. The modal runs in the browser using the bundled JavaScript.

The custom .showcase-card rule affects only the new cards. Bootstrap utility rules may use !important, so a later stylesheet does not universally override them. Avoid a lengthy cascade lecture; use the padding experiment as the concrete example.

## Formative assessment

Ask a student to point to a selector, predict a spacing change, explain col-md-6, or show the modal target-to-ID connection. Look for a justified design choice and actual test evidence. A polished screenshot alone does not establish understanding.

Accept incomplete core work with a recorded next step. Do not make extensions a condition of success. The framework provides keyboard behaviour for the modal; students still test focus, Escape, and readable content.

## Package validation

Checked relative lesson links, unique dashboard IDs, fragment and modal targets, local asset paths, exact agreement between snippets and lesson code blocks, and unchanged Python/generator JavaScript. Flask test clients successfully served the API, dashboard, and all linked stylesheets/scripts for both application folders. Interactive browser and visual checks could not be completed because the browser download failed; perform the supplied student test sequence before classroom delivery.
