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
