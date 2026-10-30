"""
Exercise 2 - "Does this function exist?"

The prompt that produced this:

    "Read a CSV file in Python and give me the average of the 'score' column,
     without using pandas."

Everything below is syntactically perfect Python. Two of these three snippets
call something that does not exist. The assistant invented them because they
*sound* like they should exist - which is exactly why they are easy to miss.

Run this file. Read the errors. Then look each name up in the real docs:
    https://docs.python.org/3/library/csv.html
    https://docs.python.org/3/library/statistics.html
"""
import csv
import statistics


def attempt_1(path):
    """Looks plausible. csv has reader() and DictReader - does it have this?"""
    with open(path, newline="") as f:
        rows = csv.read_dict(f)                 # <-- real, or invented?
    return statistics.mean(float(r["score"]) for r in rows)


def attempt_2(path):
    """statistics has mean, median, mode... surely it has this too?"""
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    return statistics.average(r["score"] for r in rows)   # <-- real?


def attempt_3(path):
    """The one that actually works."""
    with open(path, newline="") as f:
        scores = [float(row["score"]) for row in csv.DictReader(f)]
    return statistics.mean(scores)


if __name__ == "__main__":
    # Build a small CSV to test against.
    with open("scores.csv", "w", newline="") as f:
        f.write("name,score\nada,90\ngrace,80\nalan,70\n")

    for n, fn in enumerate([attempt_1, attempt_2, attempt_3], start=1):
        try:
            print(f"attempt_{n}: {fn('scores.csv')}")
        except AttributeError as e:
            print(f"attempt_{n}: FAILED -> AttributeError: {e}")
