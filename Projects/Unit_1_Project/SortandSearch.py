from numpy.random import seed
from numpy.random import randint
import time

# Functions from: https://www.youtube.com/watch?v=hpq9FzSfB7k
# Array of random integer values:
# Syntax: (Min range, Max range, Size of Array)
# https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/#:~:text=An%20array%20of%20random%20integers,the%20size%20of%20the%20array.
seed(1)
array_of_100 = randint(0, 100, 100)
array_of_1000 = randint(0, 100, 1000)
array_of_10000 = randint(0, 100, 10000)
array_of_100000 = randint(0, 100, 100000)
array_of_1000000 = randint(0, 100, 1000000)

# 3 Sorting Algorithms

# 1. SELECTION SORT
print("Selection Sort Execution Times: ")

# Perform on array of 100
start_time = time.time()


def sel_sort(array_of_100):
    for i in range(len(array_of_100)):
        min_elem = i
        for j in range(i + 1, len(array_of_100)):
            if array_of_100[j] < array_of_100[min_elem]:
                min_elem = j

        temp = array_of_100[i]
        array_of_100[i] = array_of_100[min_elem]
        array_of_100[min_elem] = temp
    return array_of_100


end_time = time.time()
sel_sort_final_time_100 = end_time - start_time
print(f"Array of 100: {sel_sort_final_time_100}")

# Perform on array of 1000
start_time = time.time()


def sel_sort2(array_of_1000):
    for i in range(len(array_of_1000)):
        min_elem = i
        for j in range(i + 1, len(array_of_1000)):
            if array_of_1000[j] < array_of_1000[min_elem]:
                min_elem = j

        temp = array_of_1000[i]
        array_of_1000[i] = array_of_1000[min_elem]
        array_of_1000[min_elem] = temp
    return array_of_1000


end_time = time.time()
sel_sort_final_time_1000 = end_time - start_time
print(f"Array of 1000: {sel_sort_final_time_1000}")

# Perform on array of 10000
start_time = time.time()


def sel_sort3(array_of_10000):
    for i in range(len(array_of_10000)):
        min_elem = i
        for j in range(i + 1, len(array_of_10000)):
            if array_of_10000[j] < array_of_10000[min_elem]:
                min_elem = j

        temp = array_of_10000[i]
        array_of_10000[i] = array_of_10000[min_elem]
        array_of_10000[min_elem] = temp
    return array_of_10000


end_time = time.time()
sel_sort_final_time_10000 = end_time - start_time
print(f"Array of 10000: {sel_sort_final_time_10000}")

# Perform on array of 100000
start_time = time.time()


def sel_sort4(array_of_100000):
    for i in range(len(array_of_100000)):
        min_elem = i
        for j in range(i + 1, len(array_of_100000)):
            if array_of_100000[j] < array_of_100000[min_elem]:
                min_elem = j

        temp = array_of_100000[i]
        array_of_100000[i] = array_of_100000[min_elem]
        array_of_100000[min_elem] = temp
    return array_of_100000


end_time = time.time()
sel_sort_final_time_100000 = end_time - start_time
print(f"Array of 100000: {sel_sort_final_time_100000}")

sel_sort_final_times_array = [sel_sort_final_time_100, sel_sort_final_time_1000, sel_sort_final_time_10000,
                              sel_sort_final_time_100000]

# 2. BUBBLE SORT
print("Bubble Sort Execution Times: ")

# Perform on array of 100
start_time = time.time()


def bub_sort(array_of_100):
    for i in range(0, len(array_of_100)):
        for j in range(0, len(array_of_100) - i - 1):
            if array_of_100[j] > array_of_100[j + 1]:
                temp = array_of_100[j]
                array_of_100[j] = array_of_100[j + 1]
                array_of_100[j + 1] = temp
    return array_of_100


end_time = time.time()
bub_sort_final_time_100 = end_time - start_time
print(f"Array of 100: {bub_sort_final_time_100}")

# Perform on array of 1000
start_time = time.time()


def bub_sort1(array_of_1000):
    for i in range(0, len(array_of_1000)):
        for j in range(0, len(array_of_1000) - i - 1):
            if array_of_1000[j] > array_of_1000[j + 1]:
                temp = array_of_1000[j]
                array_of_1000[j] = array_of_1000[j + 1]
                array_of_1000[j + 1] = temp
    return array_of_1000


end_time = time.time()
bub_sort_final_time_1000 = end_time - start_time
print(f"Array of 1000: {bub_sort_final_time_1000}")

# Perform on array of 10000
start_time = time.time()


def bub_sort2(array_of_10000):
    for i in range(0, len(array_of_10000)):
        for j in range(0, len(array_of_10000) - i - 1):
            if array_of_10000[j] > array_of_10000[j + 1]:
                temp = array_of_10000[j]
                array_of_10000[j] = array_of_10000[j + 1]
                array_of_10000[j + 1] = temp
    return array_of_10000


end_time = time.time()
bub_sort_final_time_10000 = end_time - start_time
print(f"Array of 10000: {bub_sort_final_time_10000}")

# Perform on array of 100000
start_time = time.time()


def bub_sort3(array_of_100000):
    for i in range(0, len(array_of_100000)):
        for j in range(0, len(array_of_100000) - i - 1):
            if array_of_100000[j] > array_of_100000[j + 1]:
                temp = array_of_100000[j]
                array_of_100000[j] = array_of_100000[j + 1]
                array_of_100000[j + 1] = temp
    return array_of_100000


end_time = time.time()
bub_sort_final_time_100000 = end_time - start_time
print(f"Array of 100000: {bub_sort_final_time_100000}")

bub_sort_final_times_array = [bub_sort_final_time_100, bub_sort_final_time_1000, bub_sort_final_time_10000,
                              bub_sort_final_time_10000]

# INSERTION SORT
print("Insertion Sort Execution Times: ")

# Perform on array of 100
start_time = time.time()


def insertion_sort(array_of_100):
    for i in range(1, len(array_of_100)):
        key = array_of_100[i]
        j = i - 1
        while j >= 0 and array_of_100[j] > key:
            array_of_100[j + 1] = array_of_100[j]
            array_of_100[j] = key
            j -= 1
    return array_of_100


end_time = time.time()
insert_sort_final_time_100 = end_time - start_time
print(f"Array of 100: {insert_sort_final_time_100}")

# Perform on array of 1000
start_time = time.time()


def insertion_sort1(array_of_1000):
    for i in range(1, len(array_of_1000)):
        key = array_of_1000[i]
        j = i - 1
        while j >= 0 and array_of_1000[j] > key:
            array_of_1000[j + 1] = array_of_1000[j]
            array_of_1000[j] = key
            j -= 1
    return array_of_1000


end_time = time.time()
insert_sort_final_time_1000 = end_time - start_time
print(f"Array of 1000: {insert_sort_final_time_1000}")

# Perform on array of 10000
start_time = time.time()


def insertion_sort2(array_of_10000):
    for i in range(1, len(array_of_10000)):
        key = array_of_10000[i]
        j = i - 1
        while j >= 0 and array_of_10000[j] > key:
            array_of_10000[j + 1] = array_of_10000[j]
            array_of_10000[j] = key
            j -= 1
    return array_of_10000


end_time = time.time()
insert_sort_final_time_10000 = end_time - start_time
print(f"Array of 10000: {insert_sort_final_time_10000}")

# Perform on array of 100000
start_time = time.time()


def insertion_sort3(array_of_100000):
    for i in range(1, len(array_of_100000)):
        key = array_of_100000[i]
        j = i - 1
        while j >= 0 and array_of_100000[j] > key:
            array_of_100000[j + 1] = array_of_100000[j]
            array_of_100000[j] = key
            j -= 1
    return array_of_100000


end_time = time.time()
insert_sort_final_time_100000 = end_time - start_time
print(f"Array of 100000: {insert_sort_final_time_100000}")

insert_sort_final_times_array = [insert_sort_final_time_100, insert_sort_final_time_1000, insert_sort_final_time_10000,
                                 insert_sort_final_time_100000]

# LINEAR SEARCH
print("Linear Search Execution Times: ")

# Perform on array of 100
start_time = time.time()


def search(array_of_100, x):
    for i in range(0, len(array_of_100)):
        if array_of_100[i] == x:
            return True


end_time = time.time()
lin_search_final_time_100 = end_time - start_time
print(f"Array of 100: {lin_search_final_time_100}")

# Perform on array of 1000
start_time = time.time()


def search1(array_of_1000, x):
    for i in range(0, len(array_of_1000)):
        if array_of_1000[i] == x:
            return True


end_time = time.time()
lin_search_final_time_1000 = end_time - start_time
print(f"Array of 1000: {lin_search_final_time_1000}")

# Perform on array of 10000
start_time = time.time()


def search2(array_of_10000, x):
    for i in range(0, len(array_of_10000)):
        if array_of_10000[i] == x:
            return True


end_time = time.time()
lin_search_final_time_10000 = end_time - start_time
print(f"Array of 10000: {lin_search_final_time_10000}")

# Perform on array of 100000
start_time = time.time()


def search3(array_of_100000, x):
    for i in range(0, len(array_of_100000)):
        if array_of_100000[i] == x:
            return True


end_time = time.time()
lin_search_final_time_100000 = end_time - start_time
print(f"Array of 100000: {lin_search_final_time_100000}")

# Binary Search
print("Binary Search Execution Times: ")

# Perform on array of 100
start_time = time.time()

lin_search_final_times_array = [lin_search_final_time_100, lin_search_final_time_1000, lin_search_final_time_10000,
                                lin_search_final_time_100000]


def binary_search(array_of_100, elem):
    low = 0
    high = len(array_of_100) - 1
    Temp = False

    while low <= high and not Temp:
        mid = (low + high) // 2
        if array_of_100[mid] == elem:
            Temp = True
        else:
            if elem < array_of_100[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return Temp


end_time = time.time()
bin_search_final_time_100 = end_time - start_time
print(f"Array of 100: {bin_search_final_time_100}")

# Perform on array of 1000
start_time = time.time()


def binary_search1(array_of_1000, elem):
    low = 0
    high = len(array_of_1000) - 1
    Temp = False

    while low <= high and not Temp:
        mid = (low + high) // 2
        if array_of_1000[mid] == elem:
            Temp = True
        else:
            if elem < array_of_1000[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return Temp


end_time = time.time()
bin_search_final_time_1000 = end_time - start_time
print(f"Array of 1000: {bin_search_final_time_1000}")

# Perform on array of 10000
start_time = time.time()


def binary_search2(array_of_10000, elem):
    low = 0
    high = len(array_of_10000) - 1
    Temp = False

    while low <= high and not Temp:
        mid = (low + high) // 2
        if array_of_10000[mid] == elem:
            Temp = True
        else:
            if elem < array_of_10000[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return Temp


end_time = time.time()
bin_search_final_time_10000 = end_time - start_time
print(f"Array of 10000: {bin_search_final_time_10000}")

# Perform on array of 100000
start_time = time.time()


def binary_search3(array_of_100000, elem):
    low = 0
    high = len(array_of_100000) - 1
    Temp = False

    while low <= high and not Temp:
        mid = (low + high) // 2
        if array_of_100000[mid] == elem:
            Temp = True
        else:
            if elem < array_of_100000[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return Temp


end_time = time.time()
bin_search_final_time_100000 = end_time - start_time
print(f"Array of 100000: {bin_search_final_time_100000}")

bin_search_final_times_array = [bin_search_final_time_100, bin_search_final_time_1000, bin_search_final_time_10000,
                                bin_search_final_time_100000]
