# Name: Laina Nguyen
# Ch 1 Book exercises, evens

# Exercise #2
def is_even(k):
    if k % 2 == 0:
        return True
    else:
        return False


def is_even2(k):
    if k & 1 == 0:
        return True
    else:
        return False


# Exercise #4
def sum_of_squares(n):
    sum = 0
    for num in range(n):
        sum += num ** 2
    return sum



# Function Tests

# print(is_even2(4))  # This should print out True
# print(is_even2(13))  # This should print out False

# print(sum_of_squares(5))  # 1 + 4 + 9 + 16
