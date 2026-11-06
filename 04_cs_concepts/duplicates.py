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

def has_duplicate_fast(items):
    already_checked = set()
    for item in items:
        if item in already_checked:
            return True 
        already_checked.add(item)
    return False

print(f'{has_duplicate_fast([1,2,3,4,5,6,3]) = }')
print(f'{has_duplicate_fast([1,2,3,4,5,6,7]) = }')

