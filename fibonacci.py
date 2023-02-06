"""
   n  | 1 | 2 | 3 | 4 | 5 | 6 |  7 |  8
-----------------------------------------
 f(n) | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21

"""

def f(n):
    if n <= 1:
        return n                        # Base Case
    else:
        return f(n - 1) + f(n - 2)      # Recursive Case

