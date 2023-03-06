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

mygraph = {
    'A': ['C'],
    'B': ['A', 'C'],
    'C': ['D'],
    'D': ['C'],
    'E': ['B', 'C', 'D'],
    'F': ['E'],
}

mygraph_matrix = [[0, 0, 1, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 1, 0],
                  ]

mygraph2 = {}


def edges(g):
    # Return a list of all edges, each edge ==> (u, v)
    list_edges = []
    for node, edges in g.items():
        for e in edges:
            list_edges.append((node, e))

    return list_edges


def count_edges(g):
    # Return the edge count (int)
    pass


def count_vertices(g):
    # Return the vertices count (int)
    count = 0
    for key in g:
        count += 1
    return count


# TESTING FUNCTIONS
print(count_vertices(mygraph))
print(count_edges(mygraph))
