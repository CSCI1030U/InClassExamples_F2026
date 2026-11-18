def make_change(amount, bills):
    count = 0
    change = []
    for bill in sorted(bills, reverse=True):
        count += amount // bill # bill count
        change.append((bill, amount // bill))
        amount %= bill          # leftover amount
    if amount == 0:
        return change

print(f'{make_change(105, [1,5,20,50]) = }')

def most_items(weights, budget):
    """Greedy: take the lightest items while they still fit."""
    taken = []
    for w in sorted(weights): # lightest first
        if w > budget:
            break # nothing heavier fits either - stop
        taken.append(w)
        budget -= w
    return taken

print(f'{most_items([4, 2, 7, 1, 3], 8) = }')