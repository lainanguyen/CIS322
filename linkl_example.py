class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# Creates linked list (empty)
mylist = LinkedList()

# Create starting node and
# set it to the HEAD of the linked list
mylist.head = Node('a')

# Add another node to the end
mylist.head.next = Node('b')