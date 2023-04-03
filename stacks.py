# Stacks and Queues
# Stack (using a Python List)
letters = []

# ADD to the stack
letters.append('a')
letters.append('b')
letters.append('g')

# REMOVE the last item AND store it in a variable
last_let = letters.pop()
print(last_let)

last_let = letters.pop()
print(last_let)

# VIEW top letter
print(letters[-1])

letters.pop()

if len(letters) == 0:
    print("No more letters!")