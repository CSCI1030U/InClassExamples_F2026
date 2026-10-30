"""
Exercise 1 - "Review the AI's answer".

The prompt that produced this:

    "Write a Python function that returns the median of a list of numbers."

The code below is what an assistant actually tends to produce for that prompt.
It is clean, well-named, documented, and looks completely reasonable.
It is also wrong in two ways and rude in a third.

Don't run it yet. Read it first and decide what you think it does.
"""


def median(numbers):
    """Return the median value of a list of numbers."""
    numbers.sort()
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle] + numbers[middle + 1]) / 2
    return numbers[middle]


# ---------------------------------------------------------------------------
# Three test cases. Predict each answer before running.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("odd-length :", median([7, 1, 3]))            # expect 3

    scores = [4, 1, 3, 2]
    print("even-length:", median(scores))               # expect 2.5
    print("scores now :", scores)                       # was it left alone?

    print("empty      :", median([]))                   # expect... what?
