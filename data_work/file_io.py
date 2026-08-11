"""
file_io.py  --  reading files and writing files.

Unit 3, Weeks 3-4.

RUN IT:
    python data_work/file_io.py

It reads data/students.csv and writes a new file into output/. The output/
folder is in .gitignore, so what you produce stays on your own machine.

THE IDEA YOU MUST LEAVE THIS FILE WITH
A program's variables disappear the moment it stops. A file survives. That is
the whole difference, and it is why every useful program eventually has to
write something down.
"""

import csv
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

# Where the files we create will go.
OUTPUT_DIR = os.path.join(config.BASE_DIR, "output")


def section_1_plain_text():
    """The simplest possible file work: write some lines, read them back."""
    print("\n=== 1. PLAIN TEXT FILES ===================================")

    # exist_ok=True means "do not complain if the folder is already there".
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    path = os.path.join(OUTPUT_DIR, "notes.txt")

    # --- WRITING -----------------------------------------------------------
    # THE MODE IS THE MOST IMPORTANT ARGUMENT HERE.
    #   "r"   read. Crashes if the file does not exist.
    #   "w"   write. Creates the file -- and ERASES everything already in it.
    #   "a"   append. Adds to the end, keeping what was there.
    #
    # "w" has destroyed more homework than any other two characters in Python.
    # When you want to add to a file, you want "a".
    with open(path, "w", encoding="utf-8") as f:
        f.write("First line\n")     # \n means "new line". Without it, the next
        f.write("Second line\n")    # write would sit on the same line.
        f.write("Third line\n")

    print(f"Wrote three lines to {path}")

    # --- APPENDING ---------------------------------------------------------
    with open(path, "a", encoding="utf-8") as f:
        f.write("Fourth line, added later\n")

    # --- READING -----------------------------------------------------------
    # Looping over an open file gives you one line per pass. For a huge file
    # this matters enormously: .read() would pull the entire thing into memory
    # at once, while the loop handles one line at a time.
    print("Reading it back:")
    with open(path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            # .rstrip() removes trailing whitespace, including the \n that is
            # still attached to each line. Without it, print adds a second
            # newline and the output comes out double-spaced.
            print(f"  {line_number}: {line.rstrip()}")


def section_2_read_csv():
    """CSV: Comma-Separated Values. The workhorse format of real data."""
    print("\n=== 2. READING A CSV ======================================")

    path = os.path.join(config.DATA_DIR, "students.csv")

    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # A list comprehension turns the reader into a real list, so we can go
        # through it more than once. A reader can only be walked through ONCE:
        # loop over it twice and the second loop finds nothing, which is a
        # genuinely confusing bug the first time it happens to you.
        rows = [row for row in reader]

    print(f"Read {len(rows)} rows.")
    print(f"Column names: {list(rows[0].keys())}")
    print(f"First row as a dictionary: {rows[0]}")

    # Remember: everything from a CSV is TEXT. Convert before doing arithmetic.
    total = sum(int(row["grade_level"]) for row in rows)
    print(f"Sum of grade levels (after int conversion): {total}")

    # Proof of why it matters. Without int(), "9" + "9" would be "99".
    print(f"Type of grade_level as read: {type(rows[0]['grade_level'])}")

    return rows


def section_3_write_csv(rows):
    """Change some data and write a new CSV.

    Note that we write to a NEW file. Overwriting your source data during an
    experiment is the sort of mistake you only need to make once.
    """
    print("\n=== 3. WRITING A CSV ======================================")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "students_with_status.csv")

    # Add a new column to each row, worked out from the existing data.
    for row in rows:
        row["has_pathway"] = "yes" if row["pathway"].strip() else "no"

    # fieldnames tells the writer which columns to write, and in what order.
    fieldnames = ["name", "grade_level", "pathway", "has_pathway"]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()    # the first line, holding the column names
        writer.writerows(rows)  # then every data row

    print(f"Wrote {len(rows)} rows to {path}")
    print("Open it in VS Code and check it before you trust it.")


def section_4_json(rows):
    """JSON: the format used to move data between programs and across the web."""
    print("\n=== 4. JSON ===============================================")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "students.json")

    # CSV is flat: rows and columns, nothing nested. JSON can nest, so it can
    # describe a student who has a list of projects, each with its own details.
    # That is why almost every web API speaks JSON.
    data = {
        "course": "DSTP Grade 9",
        "student_count": len(rows),
        "students": rows,   # a list of dictionaries goes straight in
    }

    with open(path, "w", encoding="utf-8") as f:
        # indent=2 formats it across multiple lines so a human can read it.
        # Leave it out and you get one enormous unreadable line -- fine for a
        # machine, miserable for you.
        # ensure_ascii=False keeps accented characters as themselves.
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Wrote JSON to {path}")

    # Reading it back. json.load() turns the file straight into Python
    # dictionaries and lists -- no manual parsing at all.
    with open(path, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print(f"Read it back. Course: {loaded['course']}, "
          f"students: {loaded['student_count']}")


def section_5_bytes_and_encoding():
    """What is actually stored on the disk: bytes."""
    print("\n=== 5. WHAT IS REALLY IN THE FILE =========================")

    # Everything on a disk is bytes: whole numbers from 0 to 255. Text is
    # bytes that we have agreed to interpret as letters. That agreement is
    # called an ENCODING, and UTF-8 is the one almost everybody uses.
    text = "Café"

    # .encode() turns text into raw bytes.
    raw = text.encode("utf-8")

    print(f"The text: {text}")
    print(f"As bytes: {raw}")
    print(f"Characters: {len(text)}, bytes: {len(raw)}")

    # Four characters, five bytes. The é needs two bytes in UTF-8. This is why
    # encoding=... appears on every open() in this course: get it wrong and
    # names come back as mojibake -- CafÃ© -- or the program simply crashes.

    print("Byte by byte:")
    for byte in raw:
        # A byte is a number. Shown here as a number, in binary, and as the
        # character it stands for when there is one.
        # format(byte, "08b") means binary, padded to 8 digits.
        char = chr(byte) if 32 <= byte <= 126 else "?"
        print(f"  {byte:>3}  {format(byte, '08b')}  {char}")


def main():
    print("=" * 60)
    print("FILE INPUT AND OUTPUT")
    print("=" * 60)

    section_1_plain_text()
    rows = section_2_read_csv()
    section_3_write_csv(rows)
    section_4_json(rows)
    section_5_bytes_and_encoding()

    print("\n" + "=" * 60)
    print("FILE OR DATABASE? You will be asked this out loud.")
    print("  File     simple, portable, easy to email. Poor at searching,")
    print("           and dangerous when two programs write at once.")
    print("  Database searching, relationships, and rules about what data is")
    print("           even allowed. Needs setup and more to learn.")
    print("Neither is better. Know which question you are answering.")
    print("=" * 60)


if __name__ == "__main__":
    main()
