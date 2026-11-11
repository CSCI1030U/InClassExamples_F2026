# Divide:  split up the list into two lists (cut it in half)
# Conquer: recursively sort the two lists (merge sort)
# Combine: merge the two sorted lists into one


# [2,6,5,1,3,4]
# => [2,6,5], [1,3,4] (divide)
# => [2,5,6], [1,3,4] (recursive merge sort)
#       ^           ^
# => [1,2,3,4,5,6]
def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else: # left value >= right value
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:] + right[right_index:]
    return result

print(f'{merge([2,5,6], [1,3,4]) = }')

# O(n log n)
def merge_sort(items):
    # base case
    if len(items) <= 1:
        return items

    # divide
    middle = len(items) // 2

    # conquer
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    # combine
    return merge(left, right)

print(f'{merge_sort([2,6,5,1,3,4]) = }')

# for comparison, here is quicksort (for reference only - not covered in class)

def split(items, pivot):
    smaller = []
    larger = []

    for index in range(len(items)):
        if items[index] < pivot:
            smaller.append(items[index])
        else:
            larger.append(items[index])

    return smaller, larger

def quicksort(items):
    # base case
    if len(items) <= 1:
        return items

    # divide
    pivot = items[0]
    smaller, larger = split(items[1:], pivot)

    # conquer
    smaller = quicksort(smaller)
    larger = quicksort(larger)

    # combine
    return smaller + [pivot] + larger

print(f'{quicksort([2,6,5,1,3,4]) = }')
