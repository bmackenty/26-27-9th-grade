# Validation

Checked against the actual Lesson 8 HTML and pinned vendor files (AdminLTE header identifies version 4.0.0).

Completed checks:

- All local Markdown navigation targets resolve.
- All three added HTML files have unique IDs.
- Every declared Bootstrap target, aria-controls and aria-labelledby reference resolves in its page.
- Stylesheets and scripts use local vendor paths; no CDN or build step.
- AdminLTE card and treeview data attributes match the supplied JavaScript.
- Pathway names and descriptions checked against the supplied syllabus and Unit 2 scope.
- Three additive HTML files only; no existing application files in the installation folder.

Limitation: automated browser interaction and screenshot checks could not run because this environment had no installed browser and the browser download failed. The browser tests in Lesson 9 are therefore provided as classroom verification steps, not reported as completed tests. Preview the pages with your existing Lesson 8 Flask server before class.
