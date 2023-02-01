# Understanding Recursion

# 5! = 5 * 4 * 3 * 2 * 1 =
def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

# RECURSIVE; look, no loops!
def rec_factorial(n):
    # Base Case
    if n == 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n-1)