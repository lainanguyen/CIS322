import numpy as np
# https://www.youtube.com/watch?v=hpq9FzSfB7k
my_array = np.array([20, 14, 25, 16, 45, 60, 12, 9])

# 3 Sorting Algorithms

"""
1. SELECTION SORT
Time complexity: O(n^2)
"""


def sel_sort(array):
    for i in range(len(array)):
        min_elem = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_elem]:
                min_elem = j

        temp = array[i]
        array[i] = array[min_elem]
        array[min_elem] = temp
    return array


# Test
# print(sel_sort(my_array))


"""
2. BUBBLE SORT

1. Compare the first and second elements
2. If it is greater than the first, swap
3. Repeat until end of list
4. The greatest element is at the last position
5. Start the process again to sort the remaining elements

Time complexity: O(n^2)
"""



def bub_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


# Test
# print(bub_sort(my_array))


"""
INSERTION SORT

1. Assume first element to be sorted, keep second element as key
2. Compare key with elements, if element is greater then keep key at front of element
3. Repeat until the key reaches the end of list, all elements sorted

Time complexity:
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            array[j] = key
            j -= 1
    return array


# Test
# print(insertion_sort(my_list))


# Paste into file as functions

# 1 Linear Search function


"""
LINEAR SEARCH

1. Compare each value in list or array
2. If value is equal to desired value
3. Element is found

Time complexity: 
"""

def search(array, x):
    for i in range(0, len(array)):
        if array[i] == x:
            return True


# Test
# print(search(my_list, 9))


# 1 Binary Search function

"""
BINARY SEARCH

1. Mark the highest, lowest, and mid positions
2. Compare the desired value with the mid value
3. If not found, check in sub arrays
4. Change the low values according to the sub array

Time complexity: 
"""


def binary_search(array, elem):
    low = 0
    high = len(array) - 1
    Temp = False

    while (low <= high and not Temp):
        mid = (low + high) // 2
        if array[mid] == elem:
            Temp = True
        else:
            if elem < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return Temp







"""
Output:
a. How long does it take to perform on an array of 100 random integers?
    - the 3 sorting methods
    - binary search
    - linear search
for this one can use the time built in python fucntion

b. Repeat for arrays of 1 000, 10 000, 100 000, 1 000 000

"""







"""
QUICK SORT

1. Decide the pivot element either at end or beginning
2. Start comparing the elements with pivot to create a left and right sub array
3. Do the same for the sub arrays
4. Repeat until all the elements have been sorted.

Time complexity: 
"""

my_list = [20, 14, 25, 16, 45, 60, 12, 9]


def quick_sort(a):
    if len(a) < 2:
        return a

    pos = 0
    for i in range(1, len(a)):
        if a[i] <= a[0]:
            pos += 1
            temp = a[i]
            a[i] = a[pos]
            a[pos] = temp

    temp = a[0]
    a[0] = a[pos]
    a[pos] = temp

    left = quick_sort(a[0:pos])
    right = quick_sort(a[pos + 1:len(a)])

    sorted_array = left + [a[pos]] + right

    return sorted_array


# Test
# print(quick_sort(my_list))


"""
MERGE SORT

1. Divide and conquer to implement merge sort
2. Keep dividing until one element is left in the sub arrays
3. Re-arrange and combine the elements to get the sorted array

Time complexity: 
"""

my_list2 = [20, 14, 25, 16, 45, 60, 12, 9]


def merge_sort(array):
    if len(array) > 1:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


# Test
# print(merge_sort(my_list2))


# Searching Algorithms


# Test
my_array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_array2, 0))