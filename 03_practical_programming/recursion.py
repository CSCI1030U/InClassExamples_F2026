# infinite recursion

def a():
    a()
    print('a() called')

# a()

'''
a()
    -> a()
        -> a()
            -> a()
                -> a()
'''

# formula
# 1. base case - eventually it will be true, then exit
# 2. recursive case - recursive call, but simpler

def print_n_times(message: str, n: int) -> None:
    # base case
    if n == 0:
        return

    print(message)

    # recursive case
    print_n_times(message, n - 1)

print_n_times('Hello', 5)

'''
print_n_times('Hello', 5)
    -> print('Hello')
    -> print_n_times('Hello', 4)
        -> print('Hello')
        -> print_n_times('Hello', 3)
'''

'''
factorial(1) = 1
factorial(n) = n * factorial(n - 1)
'''
def factorial(n: int) -> int:
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'{factorial(3) = }')

'''
factorial(3)
    - factorial(2) * 3
        - factorial(1) * 2
        - 1 * 2 = 2
    - 2 * 3 = 6
'''


'''
- this is an example of a problem fit for recursion:
                6
        3               11
    -1      4       10      30
'''

def list_sum(values: list[int]) -> int:
    # base case (when to quit)
    if len(values) == 0:
        return 0

    # recursive case (call itself, simpler problem)
    return values[0] + list_sum(values[1:])

'''
list_sum([1,2,3])
    - 1 + list_sum([2,3])
        - 2 + list_sum([3])
            - 3 + list_sum([])
                0
            - 3 + 0 = 3
        - 2 + 3 = 5
    - 1 + 5 = 6
'''
print(f'{list_sum([1,2,3]) = }')

def power(base: int, expo: int) -> int:
    # base case (when to exit)
    if expo == 1:
        return base
    # alternative base case:
    # if expo == 0:
    #     return 1
    
    # recursive call, but with simpler arguments
    return base * power(base, expo - 1)

print(f'{power(2,8) = }')
