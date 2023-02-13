"""
Graphs: Series of connected vertices (nodes) and edges

Types:
Undirected vs. Directed
Weighted vs. Not Weighted

Store Graph in Memory:
1. Adjacency List (Dictionary)
2. Adjacency Matrix (2D Array)

Graph g1, g2 and g3 from notes
"""

g1 = {
    'a': [['c']],
    'b': ['c', 'e'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['c'],
    'e': ['b', 'c'],
    'f': [],
}

g1_matrix = [[0, 0, 1, 0, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [1, 1, 0, 1, 1, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

g2_adj = {
    # [NODE, WEIGHT]
    1: [[2, 1], [3, 1]],
    2: [[3, 3]],
    3: [[4, 4]],
    4: [[1, 5]]
}

g3_adjlist = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C'],
}

g3_matrix = [[0, 1, 1, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 1],
             [0, 0, 1, 0]]
