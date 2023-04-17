# Name: Laina Nguyen
# Unit 3 Project: Understanding Tree Algorithms
# For this project, I chose DFS and BFS to demonstrate common tree algorithms in Python.

# Using a Python dictionary to act as an adjacency list
# We will be using the same dictionary for both demonstrations
# This graph contains 6 nodes and 5 edges
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

"""
1. Depth-First Search
Code from: https://favtutor.com/blogs/depth-first-search-python
Time complexity of this implementation: O(V+E)
                                        = O(6+5)
                                        = O(11)
"""

visited = set()  # Set to keep track of visited nodes of graph.


def dfs(visited, graph, node):              # function for dfs
    if node not in visited:                 # this if loop goes through each node and checks if it is part of the set that we defined as visited
        print(node)                         # if it doesn't exist in the set, then it gets printed
        visited.add(node)                   # then that node gets added to the set of visited nodes we defined as visited
        for neighbour in graph[node]:       # this loops through the neighbor nodes of the current node we are working with
            dfs(visited, graph, neighbour)  # call the function to traverse the graph, visiting each neighbor node


# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')    # The parameters passed here are visited, graph, and '5'
                            # so it checks out each node, comparing it to its presence in the visited set,
                            # uses the dictionary that we defined as graph above,
                            # and defines 5 as the starting node

"""
2. Breadth-First Search
Code from: https://favtutor.com/blogs/breadth-first-search-python
I changed each 'visited' to 'visited1' so that we can see the output of both functions in the same file
Time complexity of this implementation: O(V+E)
                                        = O(6+5)
                                        = O(11)
"""

visited1 = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited1, graph, node):  # function for BFS
    visited1.append(node)        # starting from the root node, this adds the node to the visited1 list
    queue.append(node)           # starting from the root node, this adds the node to the queue list

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)    # define variable m and assign to it the root node that gets removed
        print(m, end=" ")   # print that current node

        for neighbour in graph[m]:            # this loops through the neighbors of the current node
            if neighbour not in visited1:     # and checks that neighbor is not in the list of visited1 nodes
                visited1.append(neighbour)    # if it is not, then it gets added to the visited1 list
                queue.append(neighbour)       # and it also gets added to the queue list


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited1, graph, '5')   # The parameters passed here are visited1, graph, and '5'
                            # so it checks out each node, comparing it to its presence in the visited1 set,
                            # uses the dictionary that we defined as graph above,
                            # and defines 5 as the starting node

