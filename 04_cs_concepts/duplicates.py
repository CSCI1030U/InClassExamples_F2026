# O(n^2)
def has_duplicate(items):
    for index in range(len(items)):
        # see if items[index] is in the list again
        for dup_index in range(index + 1, len(items)):
            if index != dup_index and items[index] == items[dup_index]:
                return True
    return False

print(f'{has_duplicate([1,2,3,4,5,6,3]) = }')
print(f'{has_duplicate([1,2,3,4,5,6,7]) = }')

# O(n)
def has_duplicate_fast(items):
    already_checked = set()
    # already_checked = []
    for item in items:
        # how fast does 'in' check for list or set membership?
        # list - O(n)
        # set  - O(1) (https://www.geeksforgeeks.org/python/time-complexity-of-in-operator-in-python/)
        # choosing a data structure has a big impact - we'll discuss later
        if item in already_checked:
            return True 
        already_checked.add(item)
        # already_checked.append(item)
    return False

print(f'{has_duplicate_fast([1,2,3,4,5,6,3]) = }')
print(f'{has_duplicate_fast([1,2,3,4,5,6,7]) = }')

