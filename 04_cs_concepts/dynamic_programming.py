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

# Alternative: pick values so no two picks are neighbours; maximize the total

def max_non_adjacent_slow(values, i=None):
    """The plain recursion: correct, but O(2^n) - it recomputes everything."""
    if i is None:
        i = len(values) - 1
    if i < 0:
        return 0
    return max(values[i] + max_non_adjacent_slow(values, i - 2), max_non_adjacent_slow(values, i - 1))

def max_non_adjacent(values):
    """Bottom-up DP: O(n) time, O(1) space."""
    skip = take = 0
    # best total excluding (skip) or including (take) the current value
    for v in values:
        skip, take = max(skip, take), skip + v
        return max(skip, take)

print(f'{max_non_adjacent([3, 2, 7, 10]) = }')