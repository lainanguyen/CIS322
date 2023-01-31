# Name: Laina Nguyen
# Ch 1 Book exercises, odds R-1.1 - R-1.11

# Exercise R-1.1

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


# Exercise R-1.3
# Tuple: A finite ordered list (sequence) of elements.

def minmax(data):
    minimum_data = data[0]
    maximum_data = data[0]
    for i in data:
        if i < minimum_data:
            minimum_data = i
        if i > maximum_data:
            maximum_data = i
    return minimum_data, maximum_data


# Exercise R-1.5
# https://www.geeksforgeeks.org/sum-function-python/
# https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
# To use multiples in python - **

def sum_compute(n):
    return sum([i ** 2 for i in range(1, n)])


# Exercise R-1.7

def sum_compute_odd(n):
    return sum([i ** 2 for i in range(1, n) if i % 2 != 0])


# Exercise R-1.9
# https://www.tutorialsteacher.com/python/range-method#:~:text=The%20range()%20constructor%20method,parameter%2C%20increment%20by%20step%20parameter.
# Python range() Method:
# range(start, stop, step)

num_range = range(50, 90, 10)

# Exercise R-1.11
# https://www.geeksforgeeks.org/python-list-comprehension/
# Pattern is 2^x, x starts with 0 (2^0 = 1), ends with 9 (2^8 = 256)

list_comprehension = [2 ** i for i in range(9)]


# Function Tests

# R-1.1
# print(is_multiple(10, 5)) # Should return True
# print(is_multiple(10, 6)) # Should return False

# R-1.3
# print(minmax([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Should return (1, 9)

# R-1.5
# print(sum_compute(3)) # Should return (1^2 + 2^2) = (1+4) = 5

# R-1.7
# print(sum_compute_odd(5)) # Should return (1^2 + 3^2) = (1+9) = 10

# R-1.9
# print(list(num_range)) # Should return [50, 60, 70, 80]

# R-1.11
# print(list_comprehension) # Should return [1, 2, 4, 8, 16, 32, 64, 128, 256]
