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

def factorial(n: int) -> int:
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'{factorial(3) = }')
