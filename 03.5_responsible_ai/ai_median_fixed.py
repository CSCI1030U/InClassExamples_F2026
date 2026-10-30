"""
Exercise 1 - the version you would actually use.

Same function after a human read it, tested it, and decided what it should do
in the cases the prompt never mentioned.
"""


def median(numbers):
    """
    Return the median of `numbers`. Does not modify the caller's list.

    Raises ValueError on an empty list - a median of nothing is not a number,
    and silently returning 0 or None would hide the caller's bug.
    """
    if not numbers:
        raise ValueError("median() needs at least one number")
    ordered = sorted(numbers)          # a sorted copy - leave the original alone
    middle = len(ordered) // 2
    if len(ordered) % 2 == 0:
        return (ordered[middle - 1] + ordered[middle]) / 2   # the two middles
    return ordered[middle]


if __name__ == "__main__":
    assert median([7, 1, 3]) == 3
    assert median([4, 1, 3, 2]) == 2.5
    assert median([5]) == 5

    scores = [4, 1, 3, 2]
    median(scores)
    assert scores == [4, 1, 3, 2], "the caller's list must be untouched"

    try:
        median([])
    except ValueError as e:
        print("empty list raised ValueError:", e)

    print("all checks passed")
