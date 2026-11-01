# Teacher guide

## Prepare and publish

Upload the entire `flask_lesson_9` folder beside `flask_lesson_8` in the class repository. The student entry point is `flask_lesson_9/LESSON_9.md`. The archive is a lesson folder, not a replacement Flask project.

Before class, add the three files in `add_to_static` to a working Lesson 8 project's `static` folder and open `/static/components.html` through Flask. Have an extracted lesson folder available for offline distribution. No new dependencies are required if Lesson 8 already runs. The official website links are optional.

Do not tell students to replace their dashboard, app.py or vendor folder. Students whose setup is broken can explore with a partner and complete the pathway decision before repairing their own environment with support.

## Slide deck and pathway alignment

The user's pathway slide deck was not available among the supplied project files or identifiable search results. The five names and intellectual emphases come from `DSTP_Grade9_Syllabus (8).docx` and the Unit 2 pathway scope. Check your deck against PATHWAYS.md before class; adjust only if your current slide deck changes the pathway definitions.

The student lesson explicitly pauses for your presentation in chunk 3. Suggested 10-minute talk: one minute introducing choice; roughly one minute per pathway; four minutes comparing two examples and taking questions. Students can read the same concepts before or after the talk.

The syllabus names Tabler in its older technology overview. The delivered lesson follows the actual Lesson 8 AdminLTE stack. It does not import the old syllabus's Git-account requirements or dated calendar. The syllabus describes pathway-specific AI emphases; the Unit 2 scope uses Mode 2. This lesson asks students to follow your announced mode rather than granting automatic Mode 3 access by pathway.

## Pacing and evidence

Minimum is checkpoints 0–3 plus the notes submission. Full outcome adds a two-component prototype and tests. Students can proceed without waiting after each checkpoint, except for your shared slide presentation. Allow the paper trials and choice to take priority over extra interface decoration.

At checkpoint 2, ask “Does the number change because Python calculated it?” At checkpoint 3, ask “What problem does this solve for whom?” At checkpoint 4, ask “What would be missing if we removed this component?” These distinguish understanding from copying.

Suggested 90-minute flow: setup 15; component exploration 20; slides and choice 20; prototype 20; tests and reflection 15. For 60 minutes: setup 10; gallery 15; slides/choice 25; submission 10. Continue the prototype next lesson.

## Gallery scope

The 28 sections cover the installed core AdminLTE dashboard widgets and Bootstrap component families: cards, small boxes, info boxes, chat, timeline, callouts/alerts, buttons/groups, badges, breadcrumbs, lists, tables, forms, accordion, collapse, dropdown, tabs, modal, offcanvas, progress, spinners/placeholders, tooltips/popovers, toast, carousel, pagination, navbar, treeview, scrollspy, and layout utilities. Close buttons are demonstrated inside alerts and dialogs. The existing dashboard remains the full application-shell example.

This is a broad component-family explorer, not a claim to reproduce every variation, third-party plugin or application page in all AdminLTE releases. Charts, maps, editors, calendars and enhanced tables are explicitly marked as additional integrations, not working installed components. Sample data and backend limitations are labelled throughout. Online current-version examples may not match the pinned classroom release.

Every displayed example includes expandable HTML. The prototype supplies the same Bootstrap/AdminLTE script links and initialization helpers. Copy one instance per interactive example unless all IDs and matching references are renamed. For simpler students, start with tables and info boxes. The small-box link requires the explicit URL adjustment documented in chunk 4.

## Technical checks

See VALIDATION.md for checks performed on the delivered files. Test the final copy in your classroom environment before teaching, especially if students have independently changed the vendor bundle.

## Sources

- Lesson 8: https://github.com/bmackenty/26-27-9th-grade/blob/main/flask_lesson_8/LESSON_8.md
- Existing vendor files: https://github.com/bmackenty/26-27-9th-grade/tree/main/flask_lesson_8/completed/static/vendor
- Provided course syllabus and Unit 2 scope (five pathways and AI-mode context).
- AdminLTE component reference: https://adminlte.io/themes/v4/docs/components/card.html
- Bootstrap 5.3 reference: https://getbootstrap.com/docs/5.3/components/accordion/
