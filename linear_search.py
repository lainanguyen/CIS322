import sys
import random
from time import time

# Helper functions
# Create array/list of random numbers

def make_random(n):
    r_list = []
    for i in range(n):
        r_list.append(random.randint(0, sys.maxsize))
    return r_list


# Linear Search:
# Complexity: , Input:, Output:

def linear_search(A, x):
    for item in A:
        if item == x:
            # This is where the code 'breaks'
            return True
    return False


# Test Function
print(linear_search(["Jason", "Albert", "John"], "John"))
A_length = 10000
A = make_random(A_length)
x = random.randint(0, sys.maxsize)
# from time import time
start_time = time()
print(linear_search(A, x))
end_time = time()
print(f"Time it takes with {A_length} length array (ms): ")
print(end_time - start_time)