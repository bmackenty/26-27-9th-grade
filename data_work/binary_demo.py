"""
binary_demo.py  --  how computers store numbers, text, and everything else.

Unit 3, Week 5.

RUN IT:
    python data_work/binary_demo.py

WHY THIS MATTERS AND IS NOT JUST TRIVIA
A computer has no idea what a letter is. It stores numbers, and every number is
stored as a pattern of on-and-off switches. Text, images, sound, and this
program are all the same kind of thing underneath, distinguished only by what
we have agreed those patterns mean.

You will be asked to convert a small number to binary BY HAND, on paper, with
no computer. So do the conversions yourself before you read the answers below.
"""


def section_1_counting_in_binary():
    """Binary is counting with two digits instead of ten."""
    print("\n=== 1. COUNTING IN BINARY =================================")

    # In our usual decimal system, each position is worth ten times the one to
    # its right: 1, 10, 100, 1000.
    #
    # In binary each position is worth TWO times the one to its right:
    #
    #     128   64   32   16    8    4    2    1
    #      |     |    |    |    |    |    |    |
    #      0     0    0    0    1    1    0    1   =  8 + 4 + 1 = 13
    #
    # A digit here is a BIT. Eight bits together are a BYTE.

    print("  Decimal   Binary")
    for number in range(16):
        # format(number, "04b") means: binary, padded with zeros to 4 digits.
        print(f"    {number:>3}     {format(number, '04b')}")

    print("\n  Notice: adding one flips the rightmost bit. When it is already")
    print("  1, it becomes 0 and carries into the next column -- exactly like")
    print("  9 + 1 = 10 in decimal, just happening much more often.")


def section_2_converting_by_hand():
    """The method you will be asked to reproduce on paper."""
    print("\n=== 2. CONVERTING BY HAND =================================")

    number = 37

    print(f"  Converting {number} to binary.")
    print("  Ask each column value, largest first: does it fit?")
    print()

    # These are the place values in a byte.
    place_values = [128, 64, 32, 16, 8, 4, 2, 1]

    remaining = number   # what is still left to account for
    bits = []            # collect the answer here

    for value in place_values:
        if value <= remaining:
            # It fits. Write a 1 and subtract it from what remains.
            bits.append("1")
            remaining = remaining - value
            print(f"    {value:>3} fits.        Write 1. Remaining: {remaining}")
        else:
            # Too big. Write a 0 and change nothing.
            bits.append("0")
            print(f"    {value:>3} is too big.  Write 0. Remaining: {remaining}")

    # "".join(list) glues a list of strings into one string with nothing
    # between them.
    answer = "".join(bits)
    print(f"\n  {number} in binary is {answer}")

    # Check the work with Python's built-in conversion.
    # bin() gives a string starting with "0b" to mark it as binary, so we cut
    # off those two characters with [2:] and pad it back out to 8 digits.
    python_answer = bin(number)[2:].zfill(8)
    print(f"  Python agrees: {python_answer}")
    print(f"  Match: {answer == python_answer}")


def section_3_binary_to_decimal():
    """The conversion in the other direction."""
    print("\n=== 3. BINARY BACK TO DECIMAL =============================")

    binary_string = "10110"

    print(f"  Converting {binary_string} back to decimal.")
    print("  Multiply each bit by its place value and add up the results.")
    print()

    total = 0

    # reversed() walks the string backwards, so we start at the rightmost bit,
    # which is the 1s column.
    for position, bit in enumerate(reversed(binary_string)):
        # ** is "to the power of". 2**0 is 1, 2**1 is 2, 2**2 is 4, and so on.
        place_value = 2 ** position

        if bit == "1":
            total = total + place_value
            print(f"    Bit {bit} in the {place_value}s column: add {place_value}. Total: {total}")
        else:
            print(f"    Bit {bit} in the {place_value}s column: add nothing.")

    print(f"\n  {binary_string} is {total} in decimal.")

    # int(string, 2) converts using base 2. The 2 is doing all the work.
    print(f"  Python agrees: {int(binary_string, 2)}")


def section_4_text_is_numbers():
    """Every character is a number underneath."""
    print("\n=== 4. TEXT IS NUMBERS ====================================")

    word = "Code"

    print(f"  The word: {word}")
    print("  Character   Number   Binary")

    for char in word:
        # ord() gives the number that stands for a character.
        number = ord(char)
        print(f"      {char}        {number:>4}   {format(number, '08b')}")

    # chr() goes the other way: number to character.
    print(f"\n  Number 65 is the character {chr(65)!r}")
    print(f"  Number 97 is the character {chr(97)!r}")

    # Capital A is 65 and lowercase a is 97: a gap of exactly 32. That is not a
    # coincidence. 32 is 00100000 in binary, so the ONLY difference between A
    # and a is a single bit. Whoever designed this made changing case very
    # cheap, and that decision is still with us decades later.
    print(f"\n  'A' is {ord('A')}, 'a' is {ord('a')}. The gap is {ord('a') - ord('A')}.")
    print(f"  In binary: {format(ord('A'), '08b')} and {format(ord('a'), '08b')}")
    print("  One bit apart. That was a design decision, not an accident.")


def section_5_why_files_differ():
    """Why a text file and an image file look different at byte level."""
    print("\n=== 5. WHY FILE TYPES DIFFER ==============================")

    # A file is a sequence of bytes. Nothing in the file says what it means.
    # The MEANING comes from the program that opens it.
    text_bytes = "Hi".encode("utf-8")

    # The first bytes of a real PNG image. The 137, 80, 78, 71 at the start is
    # a "magic number": a signature saying "this is a PNG". That is how an
    # image viewer recognises a file even if you rename it to notes.txt.
    fake_png_header = bytes([137, 80, 78, 71, 13, 10, 26, 10])

    print(f"  Text 'Hi' as bytes:   {list(text_bytes)}")
    print(f"  Start of a PNG file:  {list(fake_png_header)}")
    print()
    print("  Both are just numbers. Nothing inside a file states what it is.")
    print("  Renaming photo.png to photo.txt changes nothing about the bytes;")
    print("  it only changes which program your computer offers to open it.")
    print()
    print("  Text files hold bytes that map to characters. Image files hold")
    print("  bytes that map to pixels, usually compressed. Open an image in a")
    print("  text editor and you get nonsense -- because the editor is reading")
    print("  pixel data as if it were letters.")


def main():
    print("=" * 60)
    print("BINARY: HOW COMPUTERS REALLY STORE THINGS")
    print("=" * 60)

    section_1_counting_in_binary()
    section_2_converting_by_hand()
    section_3_binary_to_decimal()
    section_4_text_is_numbers()
    section_5_why_files_differ()

    print("\n" + "=" * 60)
    print("PRACTICE, ON PAPER, NO COMPUTER:")
    print("  1. Convert 19, 64, and 100 to binary.")
    print("  2. Convert 1001, 11110000, and 101010 to decimal.")
    print("  3. What is the largest number one byte can hold? Why?")
    print("  4. Your first name is how many bytes in UTF-8? Check with code")
    print("     only AFTER you have written down your prediction.")
    print("=" * 60)


if __name__ == "__main__":
    main()
