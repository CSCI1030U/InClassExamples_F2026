# fibonacci sequence:
# 0 1 1 2 3 5 8 13 ...

# O(2^n)
def fib_slow(n):
    if n < 2:
        return n
    
    return fib_slow(n - 1) + fib_slow(n - 2)

# print(f'{fib_slow(100) = }')

# dynamic programming version:
# O(n)
def fib(n, memo=None):
    if memo is None:
        memo = {}
    
    if n < 2:
        return n
    
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]

print(f'{fib(500) = }')

def fib_linear(n):
    solutions = [0, 1]

    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])
    
    return solutions[n]

print(f'{fib_linear(5000) = }')
