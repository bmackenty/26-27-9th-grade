# AI Use Log

Copy this file for each unit and fill it in as you work. One entry per
significant AI interaction. Fill it in **while** you work, not the night
before it is due — a log written from memory is a work of fiction, and it
reads like one.

---

## The three modes

| Mode | Name | What it means |
| --- | --- | --- |
| **1** | AI Off | No AI at all. Not for syntax, not for ideas, not for "just checking". |
| **2** | AI as Tutor | AI may explain and teach. It may not write code you submit. |
| **3** | AI as Collaborator | AI may help produce code, and you log and can defend every line. |

The mode is set per unit and per task. If you are unsure which mode applies
right now, ask. Guessing generously in your own favour is not a defence.

**The log is used in Mode 2 and Mode 3 only.** During Mode 1 weeks there is
nothing to log, and that is deliberate.

---

## Entry template

Copy this block for each entry.

```
### Entry [number] — [date]

**Mode:** 2 or 3
**Task:** what you were working on

BEFORE ASKING
1. What I am trying to do:
2. What I have already tried:
3. My best guess at what is wrong or missing:

**My question to the AI:**

AFTER THE ANSWER
4. The answer in my own words (not pasted):
5. Do I think it is correct, and why:
6. What I changed as a result:
```

---

## Worked example of a good entry

### Entry 3 — 14 October

**Mode:** 2
**Task:** Filtering a list of dictionaries in the mini data project

BEFORE ASKING
1. What I am trying to do: print only the students with more than 10 hours.
2. What I have already tried: a for loop with `if students > 10`, which gave
   `TypeError: '>' not supported between instances of 'dict' and 'int'`.
3. My best guess: I am comparing the whole dictionary instead of one value
   inside it, but I do not know how to reach the value.

**My question to the AI:** In Python, how do I get one value out of a
dictionary inside a list while looping?

AFTER THE ANSWER
4. The answer in my own words: each item in the list is a whole dictionary, so
   I have to name the key I want — `student["hours"]` — instead of comparing
   the dictionary itself.
5. Do I think it is correct: yes. I tested it with my five rows and got three
   students back, which I checked against the CSV by hand.
6. What I changed: `if student["hours"] > 10:`. The AI also suggested a list
   comprehension. I did not use it because I could not yet explain how it
   works, and I would not be able to defend it.

---

## Why entry 6 matters most

Point 6 is where the marks and the honesty both live. "I copied what it said"
is not an answer. If you cannot describe what you changed and why, you have
found the boundary of your own understanding — which is useful information,
and much better found now than during an oral defence.

## What is not acceptable

- Pasting AI code you cannot explain line by line.
- Logging entries after the fact, invented to match code you already have.
- Using AI at all during a Mode 1 task.
- Logging one entry for a session where you asked twenty questions.

Every build session ends with someone asking you what your code does. That is
not a trap. It is the assessment.
