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
array_of_20000 = randint(0, 100, 20000)

# The array of 100000 takes too long, so I will be using 20000 to showcase the last point
array_of_100000 = randint(0, 100, 100000)


# 1. SELECTION SORT

def sel_sort(arr):
    for i in range(len(arr)):
        min_elem = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_elem]:
                min_elem = j

        temp = arr[i]
        arr[i] = arr[min_elem]
        arr[min_elem] = temp
    return arr


print("Selection Sort Execution Times: ")

# Perform on array of 100
start_time = time.time()
sel_sort(array_of_100)
end_time = time.time()
sel_sort_final_time_100 = end_time - start_time
print(f"Array of 100: {sel_sort_final_time_100}")

# Perform on array of 1000
start_time = time.time()
sel_sort(array_of_1000)
end_time = time.time()
sel_sort_final_time_1000 = end_time - start_time
print(f"Array of 1000: {sel_sort_final_time_1000}")

# Perform on array of 10000
start_time = time.time()
sel_sort(array_of_10000)
end_time = time.time()
sel_sort_final_time_10000 = end_time - start_time
print(f"Array of 10000: {sel_sort_final_time_10000}")

# Perform on array of 20000
start_time = time.time()
sel_sort(array_of_20000)
end_time = time.time()
sel_sort_final_time_20000 = end_time - start_time
print(f"Array of 20000: {sel_sort_final_time_20000}")

# # Perform on array of 100000
# start_time = time.time()
# sel_sort(array_of_100000)
# end_time = time.time()
# sel_sort_final_time_100000 = end_time - start_time
# print(f"Array of 100000: {sel_sort_final_time_100000}")
#

sel_sort_final_arr = [sel_sort_final_time_100, sel_sort_final_time_1000, sel_sort_final_time_10000,
                      sel_sort_final_time_20000]


# 2. BUBBLE SORT

def bub_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print("Bubble Sort Execution Times: ")

# Perform on array of 100
start_time = time.time()
bub_sort(array_of_100)
end_time = time.time()
bub_sort_final_time_100 = end_time - start_time
print(f"Array of 100: {bub_sort_final_time_100}")

# Perform on array of 1000
start_time = time.time()
bub_sort(array_of_1000)
end_time = time.time()
bub_sort_final_time_1000 = end_time - start_time
print(f"Array of 1000: {bub_sort_final_time_1000}")

# Perform on array of 10000
start_time = time.time()
bub_sort(array_of_10000)
end_time = time.time()
bub_sort_final_time_10000 = end_time - start_time
print(f"Array of 10000: {bub_sort_final_time_10000}")

# Perform on array of 20000
start_time = time.time()
bub_sort(array_of_20000)
end_time = time.time()
bub_sort_final_time_20000 = end_time - start_time
print(f"Array of 20000: {bub_sort_final_time_20000}")

# # Perform on array of 100000
# start_time = time.time()
# bub_sort(array_of_100000)
# end_time = time.time()
# bub_sort_final_time_100000 = end_time - start_time
# print(f"Array of 100000: {bub_sort_final_time_100000}")

bub_sort_final_arr = [bub_sort_final_time_100, bub_sort_final_time_1000, bub_sort_final_time_10000,
                      bub_sort_final_time_20000]


# INSERTION SORT

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1
    return arr


print("Insertion Sort Execution Times: ")

# Perform on array of 100
start_time = time.time()
insertion_sort(array_of_100)
end_time = time.time()
insert_sort_final_time_100 = end_time - start_time
print(f"Array of 100: {insert_sort_final_time_100}")

# Perform on array of 1000
start_time = time.time()
insertion_sort(array_of_1000)
end_time = time.time()
insert_sort_final_time_1000 = end_time - start_time
print(f"Array of 1000: {insert_sort_final_time_1000}")

# Perform on array of 10000
start_time = time.time()
insertion_sort(array_of_10000)
end_time = time.time()
insert_sort_final_time_10000 = end_time - start_time
print(f"Array of 10000: {insert_sort_final_time_10000}")

# Perform on array of 20000
start_time = time.time()
insertion_sort(array_of_20000)
end_time = time.time()
insert_sort_final_time_20000 = end_time - start_time
print(f"Array of 20000: {insert_sort_final_time_20000}")

# # Perform on array of 100000
# start_time = time.time()
# insertion_sort(array_of_100000)
# end_time = time.time()
# insert_sort_final_time_100000 = end_time - start_time
# print(f"Array of 100000: {insert_sort_final_time_100000}")

insert_sort_final_arr = [insert_sort_final_time_100, insert_sort_final_time_1000, insert_sort_final_time_10000,
                         insert_sort_final_time_20000]


# LINEAR SEARCH

def search(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return True


print("Linear Search Execution Times: ")

# Perform on array of 100
start_time = time.time()
search(array_of_100, 1)
end_time = time.time()
lin_search_final_time_100 = end_time - start_time
print(f"Array of 100: {lin_search_final_time_100}")

# Perform on array of 1000
start_time = time.time()
search(array_of_1000, 1)
end_time = time.time()
lin_search_final_time_1000 = end_time - start_time
print(f"Array of 1000: {lin_search_final_time_1000}")

# Perform on array of 10000
start_time = time.time()
search(array_of_10000, 1)
end_time = time.time()
lin_search_final_time_10000 = end_time - start_time
print(f"Array of 10000: {lin_search_final_time_10000}")

# Perform on array of 20000
start_time = time.time()
search(array_of_20000, 1)
end_time = time.time()
lin_search_final_time_20000 = end_time - start_time
print(f"Array of 20000: {lin_search_final_time_20000}")

# # Perform on array of 100000
# start_time = time.time()
# search(array_of_100000, 1)
# end_time = time.time()
# lin_search_final_time_100000 = end_time - start_time
# print(f"Array of 100000: {lin_search_final_time_100000}")

lin_search_final_arr = [lin_search_final_time_100, lin_search_final_time_1000, lin_search_final_time_10000,
                        lin_search_final_time_20000]


# Binary Search

def binary_search(arr, elem):
    low = 0
    high = len(arr) - 1
    Temp = False

    while low <= high and not Temp:
        mid = (low + high) // 2
        if arr[mid] == elem:
            Temp = True
        else:
            if elem < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return Temp


print("Binary Search Execution Times: ")

# Perform on array of 100
start_time = time.time()
binary_search(array_of_100, 1)
end_time = time.time()
bin_search_final_time_100 = end_time - start_time
print(f"Array of 100: {bin_search_final_time_100}")

# Perform on array of 1000
start_time = time.time()
binary_search(array_of_1000, 1)
end_time = time.time()
bin_search_final_time_1000 = end_time - start_time
print(f"Array of 1000: {bin_search_final_time_1000}")

# Perform on array of 10000
start_time = time.time()
binary_search(array_of_10000, 1)
end_time = time.time()
bin_search_final_time_10000 = end_time - start_time
print(f"Array of 10000: {bin_search_final_time_10000}")

# Perform on array of 20000
start_time = time.time()
binary_search(array_of_20000, 1)
end_time = time.time()
bin_search_final_time_20000 = end_time - start_time
print(f"Array of 20000: {bin_search_final_time_20000}")

# # Perform on array of 100000
# start_time = time.time()
# binary_search(array_of_100000, 1)
# end_time = time.time()
# bin_search_final_time_100000 = end_time - start_time
# print(f"Array of 100000: {bin_search_final_time_100000}")

bin_search_final_arr = [bin_search_final_time_100, bin_search_final_time_1000, bin_search_final_time_10000,
                        bin_search_final_time_20000]