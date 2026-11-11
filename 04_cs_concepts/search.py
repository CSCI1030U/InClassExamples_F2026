# O(n)
def linear_search(items, target):
    comparison_count = 0
    for i in range(len(items)):
        comparison_count += 1
        if items[i] == target:
            print(f'linear_search: {comparison_count = }')
            return i 
    print(f'linear_search: {comparison_count = }')
    return None

print(f'{linear_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 4) = }')
print(f'{linear_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 31) = }')

# O(log n)
def binary_search(items, target):
    low = 0
    high = len(items) - 1
    comparison_count = 0
    while low <= high:
        middle = (low + high) // 2
        comparison_count += 1
        if items[middle] == target:
            # found it!
            print(f'binary_search: {comparison_count = }')
            return middle
        elif items[middle] > target:
            # search the first half of the list
            high = middle - 1
        else: # items[middle] < target
            # search the second half of the list
            low = middle + 1
    print(f'binary_search: {comparison_count = }')
    return None

print(f'{binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 4) = }')
print(f'{binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 31) = }')
