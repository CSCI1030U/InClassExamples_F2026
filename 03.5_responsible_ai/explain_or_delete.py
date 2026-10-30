"""
Exercise 3 - "Explain it or delete it".

The prompt that produced this:

    "Group a list of (student, mark) pairs by letter grade. Make it concise."

Ask for concise and you get concise. Line 31 packs four or five ideas into one
expression. It also produces exactly the right answer on the five students
below - so a quick spot-check passes it, and it goes in.

It is still wrong.

Your job, in order:
  1. For each numbered line, say out loud what it does and why it is there.
  2. Predict the letter grade line 31 gives a student who scored *exactly* 80.
  3. Run the file and read the last line of output.

The rule this exercise exists to make concrete: if you cannot explain a line you
are about to hand in, it is not yours yet. Rewrite it as code you *can* explain,
or keep asking until you can - because "it worked on my examples" is not a check.
"""
from collections import defaultdict

MARKS = [("ada", 91), ("grace", 78), ("noor", 64), ("katherine", 88), ("alan", 58), ("edgar", 25)]


def grade_groups_clever(marks):
    groups = defaultdict(list)                                           # 1
    for name, mark in marks:                                             # 2
        groups["ABCDF"[min(4, max(0, (100 - mark) // 10 - 1))]].append(name)  # 3
    return dict(sorted(groups.items()))                                  # 4


def grade_groups_plain(marks):
    """The same thing, written so a human can check it against the rubric."""
    groups = {}
    for name, mark in marks:
        if mark >= 80:
            letter = "A"
        elif mark >= 70:
            letter = "B"
        elif mark >= 60:
            letter = "C"
        elif mark >= 50:
            letter = "D"
        else:
            letter = "F"
        groups.setdefault(letter, []).append(name)
    return dict(sorted(groups.items()))


if __name__ == "__main__":
    print("clever:", grade_groups_clever(MARKS))
    print("plain :", grade_groups_plain(MARKS))

    # Do they really agree? Check every mark from 0 to 100, not just the five above.
    everyone = [(f"s{m}", m) for m in range(101)]
    same = grade_groups_clever(everyone) == grade_groups_plain(everyone)
    print("agree on all marks 0-100:", same)

    if not same:
        print("\nThey do NOT agree. Where?")
        print(" mark | clever | plain")
        for m in range(101):
            # c = next(iter(grade_groups_clever([("x", m)])))
            # p = next(iter(grade_groups_plain([("x", m)])))
            c = next(iter(grade_groups_clever([("x", m)])))
            p = next(iter(grade_groups_plain([("x", m)])))
            if c != p:
                print(f" {m:>4} |   {c}    |   {p}")
        print("\nOff by one at every boundary: the student who scored exactly 80 gets a B.")
