# Teacher notes

Allow 60 minutes: recovery 10, form design 5, HTML 15, CSS 10, JavaScript 10, testing 10. If recovery exceeds 10 minutes, supply the baseline and prioritise the form working; treat visual personalisation as extension work. Students should read and change supplied JavaScript, not memorise its async error-handling structure.

This lesson deliberately consolidates Lesson 4 before introducing AdminLTE. It teaches classes, reusable visual elements, labels, two controls, and a submit event. AdminLTE can follow when these are secure.

## Learning evidence

Each student should show one intentional CSS modification, one correct explanation of a label/control relationship, and a test of an invalid nickname. They should be able to state where the data is used.

## Expected explanations

- The browser reads nickname and theme locally using `.value`.
- `event.preventDefault()` stops the form's default navigation/submission; `fetch` still makes its own GET request to Flask.
- Python receives no nickname or theme in that request. It still returns a random item. Nothing is saved in a database or localStorage by this application. Browsers may separately retain form values.
- Theme changes presentation, not the Python random choices. Both nickname and theme are read at submission time.
- `required` blocks a genuinely empty input; whitespace needs the JavaScript trim check. `maxlength` limits ordinary input to 20 characters. Client checks help usability but would not replace server-side validation if data were sent to Python.
- A placeholder disappears during typing; a visible label remains and is connected by `for`/`id`.
- `name` identifies the field in an ordinary form submission; this script reads fields by ID and does not serialise or submit their names/values.
- Use invented nicknames. Date of birth, address, and email do not help this generator and should not be requested.
- The CSS theme selectors match `data-theme` on the result card; `dataset.theme` updates that attribute.

## Lesson 3 correction worth reinforcing

Each click requests a result but may produce the same random item. Repetition alone is not evidence of a broken request.

## Extensions

Optional tagline should be used locally and displayed with textContent. Do not request additional identifying data. A future lesson can send an item category to Python, validate it on the server, and change the generated item.

## Validation of this handout

Both Flask projects were run and their routes/assets checked. JavaScript was exercised against live Flask with a simulated DOM for whitespace rejection, personalisation, theme changes, one request per submission, and failed-request recovery. Python syntax, unique HTML IDs, and local Markdown links were checked. A browser renderer could not be installed, so visual layout and native browser validation were not automatically verified.
