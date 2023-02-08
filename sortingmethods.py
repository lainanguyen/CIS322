# Create random list of nums

# Selection

# Selection sort in Python
# time complexity O(n^2)
# sorting by finding min_index
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j

        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


# Insertion

# Python program for implementation of Insertion Sort
# tiem complexity O(n^2)
# Function to do insertion sort
def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Quicksort

# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# function to perform quicksort


def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


# Mergesort

# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Test all methods
if __name__ == "__main__":
    print("-----Sorting Tests-----")

    print("SELECTION SORT")
    arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
    size = len(arr)
    print(arr)
    selectionSort(arr, size)
    print(arr)

    print("INSERTION SORT")
    # sorting the array [12, 11, 13, 5, 6] using insertionSort
    arr = [12, 11, 13, 5, 6]
    print(arr)
    insertionSort(arr)
    print(arr)

    print("QUICKSORT")
    data = [1, 7, 4, 1, 10, 9, -2]
    print("Unsorted Array")
    print(data)

    size = len(data)

    quickSort(data, 0, size - 1)

    print('Sorted Array in Ascending Order:')
    print(data)

    print("MERGESORT")
    # Driver code to test above
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)

    print(arr)
    mergeSort(arr, 0, n - 1)
    print(arr)
