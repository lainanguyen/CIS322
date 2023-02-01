# Name: Laina Nguyen
# Ch 1 Book exercises, C-1.14, C1.15, C1.17, C1.19

# Exercise C-1.14
# Write a short Python function that takes a sequence of integer values and  determines if there is a distinct pair
# of numbers in the sequence whose  product is odd.

# Python Bitwise Operator: https://www.geeksforgeeks.org/python-bitwise-operators/

def odd_product(sequence):
    n = len(sequence)
    for i in range(n):
        for j in range(n):
            if i != j:
                total = sequence[i] * sequence[j]
                if total & 1:
                    return True
        return False


# Exercise C-1.15
# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each
# other


def unique_numbers(sequence):
    unique_set = []
    for i in range(len(sequence)):
        if i not in unique_set:
            unique_set.append(i)
            if len(unique_set) != 0:
                print("There are duplicates. The numbers are not all different from each other")
                return False
            elif len(unique_set) == 0:
                print("There are no duplicates. The numbers are all different from each other")
                return True


# Exercise C-1.17
# Had we implemented the scale function (page 25) as follows, does it work properly?
# Scale: Primary purpose is to multiply all entries of a numeric data set by a given factor (p.25)
# Cite: Goodrich, Michael T.. Data Structures and Algorithms in Python (p. 25). Wiley Higher Ed. Kindle Edition.


def scale(data, factor):
    for val in data:
        val *= factor

"""
Example shown in book:

def scale(data, factor):  
    for j in range(len(data)):  
        data[j] = factor

Cite: Goodrich, Michael T.. Data Structures and Algorithms in Python (p. 25). Wiley Higher Ed. Kindle Edition. 

Judging from this, this function (shown in the question) was not used properly because of the line "for val in data"
To use 'data' as the iterable does not work because it cannot modify the structure of 'data'. To modify it, 
you need an index to modify the elements of the structure.
To correct it, I would rewrite this function as:
"""

def scale(data, factor):
    for val in range(len(data)):
        data[val] *= factor


# Exercise C-1.19
# Demonstrate how to use Python's list comprehension syntax to produce the list ['a', 'b', 'c', ..., 'z'] but without
# having to type all 26 characters literally.

"""
The general form for list comprehension syntax is as follows:
[ expression for value in iterable if condition ] 
Cite: Goodrich, Michael T.. Data Structures and Algorithms in Python (p. 43). Wiley Higher Ed. Kindle Edition. 

From this website, https://djangocentral.com/display-char-from-a-z/#:~:text=Using%20chr()%20Function,
97)%20returns%20%22a%22. , we learn about the chr()function that returns a Unicode character for the provided ACSII 
value, where chr(97) returns "a".

Using this format, we can use:
"""
        # expression      value   iterable
alphabet = [chr(97 + i) for i in range(26)]
print(alphabet)



