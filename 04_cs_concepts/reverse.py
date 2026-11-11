# time: O(n), space: O(1)
def reverse_in_place(items):
    low = 0
    high = len(items) - 1
    while low < high:
        items[low], items[high] = items[high], items[low]
        low += 1
        high -= 1
    return items 

original = [1,2,3,4]
print(f'{reverse_in_place(original) = }')
print(f'{original = }')

# time: O(n), space: O(n)
def reverse_copy(items):
    # return items[::-1]
    # return [items[i] for i in range(len(items) - 1, -1, -1)]
    results = []
    for i in range(len(items) - 1, -1, -1):
        results.append(items[i]) # O(1)
    return results

original = [1,2,3,4]
print(f'{reverse_copy(original) = }')
print(f'{original = }')