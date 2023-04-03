#Goodrich, Exercises 6.3, 6.5
#WARNING: Remember that you are dealing with a STACK, not a LIST. You only have
#     access to the following methods:
#          L.append(), L.pop(), L[-1], len(L) == 0, len(L)
#     You cannot loop through the list to access each item in order with indices
#          because it is NOT a list, it is a stack.


###
#Exercise 6.3
###

letters = []
numbers = []

#Create the stacks to test
letters.append('a')
letters.append('b')
letters.append('c')
letters.append('d')
numbers.append(4)
numbers.append(3)
numbers.append(2)
numbers.append(1)

print("\n***EXERCISE 6.3***\n")
print("LETTERS:")
print(letters)
print("NUMBERS:")
print(numbers)

def transfer(S, T):
    pass

transfer(numbers, letters)
#Should result in:
#Numbers = empty
#Letters = [a, b, c, d, 1, 2, 3, 4]

print("\nNew LETTERS:")
print(letters)
print("New NUMBERS:")
print(numbers)


###
#Exercise 6.5
###
list65 = ['C','A','I','R','N',' ','U','N','I']

print("\n***EXERCISE 6.5***\n")
print("ORIGINAL LIST")
print(list65)

def rev_list(mylist):
    #Use a stack to reverse the list
    mystack = []
    newlist = []

    #Adds all elements from given LIST to stack
    for item in mylist:
        mystack.append(item)

    #Pops elements from stack and places them in newlist
    #In effect, putting them in REVERSE
    while len(mystack) != 0:
        newlist.append(mystack.pop())

    return newlist

list65 = rev_list(list65)

print("\nNEW LIST")
print(list65)

