# Name: Laina Nguyen
# Ch 6 Book exercises, R-7.2, R-7.6

"""
Exercise R-7.2
# Question:
  Describe an algorithm to concatenate 2 singly linked lists L and M,
  given only references to first node of each list
  into single list L' that contains all nodes of L followed by all nodes of M
# concatenate - link together
  So if L has 1 -> 2 -> None and M has 3 -> 4 -> None
  Then the concatenated list would be L': 1 -> 2 -> 3 -> 4 -> None

To create an algorithm that links lists L and M together, first I would loop through each list to make sure that neither of those
list are empty, because if one of them are, then the concatenated list would just be the content of whichever list is not empty.
I would do this by using an if loop, checking if the only value of list L or M is 'None'.
If both lists L and M are not empty, and since we are only given references to the first node of each list,
then I would start by setting the first node of L to a 'temp' pointer
then loop through list L, and as it goes through the nodes it will set the next node to the 'temp' pointer
this loop will end when the last node is reached, then set the 'temp.next' to the first node of M which inserts contents of M into L
It would look something like this:
while temp.next is not None:
    temp = temp.next
temp.next = M
And then once we return L, it will contain the concatenation of L and M

Exercise R-7.6
# Question:
  Suppose x and y are references to nodes of CIRCULARLY linked lists
  not necessarily the same list
  Desribe a FAST algorithm for telling if x and y belong to the same list

# Tortoise and Hare algorithm with Python example
# https://towardsdatascience.com/detecting-cycles-in-linked-lists-an-analogy-559c3639ef43

# Time complexity
#https://medium.com/swlh/floyds-cycle-detection-algorithm-32881d8eaee1#:~:text=Its%20Time%20complexity%20is%20O(n)%2C%20n%20is%20the,optimized%20algorithm%20for%20this%20problem.

To check if x and y belong to the same list, I would create a function that traverses through each linked list and
checks if x and y are the same node, which would confirm that they are in the same circularly linked list.
Because we are checking circularly linked lists, I would use a slow pointer (x) and a fast pointer (y),
where x moves 1 step ahead, and y moves 2 steps ahead
This makes sure that if this cycle does contain both of these nodes, then they would eventually catch up to each other.
This would look something like:
while slow_pointer != fast_pointer:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next
I would also add an if statement that returns False if either of these pointers (x or y) is None,
in this case x and y are not in the same list
If it cycles through and there is a point where slow_pointer = fast_pointer, then it will return True which means
that x and y belong to the same list
This is a fast algorithm because the time complexity of the tortoise and hare algorithm is O(n).
"""

# Codingame Challenge: Stock Exchange: Losses

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Time complexity of assigning values: O(1)
n = int(input())                # Number of stock values available
input = input().split()         # Splits each number of input into a list of substrings and assign this to variable
p = int(input[0])               # Since the .split() function turns the input into a string type, convert it to an integer type
                                # Only the first element is needed because it is the initial stock value
loss = 0                        # Create loss variable to store the loss calculated
# Time complexity of if loop: O(n)
for i in input:
    t = int(i)                  # Convert each substring to an integer
    loss = max(loss, p - t)     # Find the maximum loss out of the current loss or a calculation of p - t
                                # p - t represents the difference of max loss and current loss
    p = max(p, t)               # Assign the maximum loss found to p
# Time complexity of printing: O(1)
print(-loss)                    # Return a negative value since it is a loss

# Time complexity: O(1) + O(n) + O(1) = O(n)

