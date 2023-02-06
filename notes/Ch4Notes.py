# RECURSION

# Factorial Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))  # 3! = 3 * (2!) = 3 * 2 * 1 = 6


# English ruler: Fractal

# Draw one line with given tick length
def draw_line(tick_length, tick_label=''):
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
        print(line)


# Draw tick interval based upon a central tick length
def draw_interval(center_length):
    if center_length > 0:  # stop when length drops to 0
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw botton ticks


# Draw English ruler with given number of inches, major tick length
def draw_ruler(num_inches, major_length):
    draw_line(major_length, "0")  # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line and label


# Binary search

# Return True if target is found in indicated portion of a Python list
# The search only considers the portion from data[low] to data[high] inclusive
def binary_search(data, target, low, high):
    if low > high:
        return False  # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:  # found a match
            return True
        elif target < data[mid]:  # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:  # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


# File Systems

"""
Algorithm DiskUsage(path):
    Input: A string designating a path to a file system-entry
    Output: The cumularitve disk space used by that entry and any nested entries
    total = size(path)      # immediate disk space used by that entry
    if path represents a directory then
        for each child entry stored within directory path do
            total = total + DiskUsage(child)    # recursive call
    return total
"""

import os


# Return the number of bytes used by a file/folder and any descendents
def disk_usage(path):
    total = os.path.getsize(path)  # account for direct usage
    if os.path.isdir(path):  # check if this is a directory
        for filename in os.listdir(path):  # then for each child:
            childpath = os.path.join(path, filename)  # compose full path to child
            total += disk_usage(childpath)  # add child's usage to total

    print('{0:<7}'.format(total), path)  # descriptive output (optional)
    return total  # return the grand total

