#!/usr/bin/python                        # Specifies the location of this file
# -*- coding: utf-8 -*-                  # Tells Python program to use unicode character encoding method
import math                              # Imports math module that is used in lines 33 and 62

graph = {                                # Create a dictionary named graph
    'a': {'b': 5, 'c': 2},               # Key 'a' is mapped to 'b' of value 5 and 'c' of value 2
    'b': {'a': 5, 'c': 7, 'd': 8},       # Key 'b' is mapped to 'a' of value 5 and 'c' of value 7 and 'd' of value 8
    'c': {                               # Key 'c' is mapped to:
        'a': 2,                          # 'a' of value 2
        'b': 7,                          # 'b' of value 7
        'd': 4,                          # 'd' of value 4
        'e': 8,                          # 'e' of value 8
    },
    'd': {                               # Key 'd' is mapped to:
        'b': 8,                          # 'b' of value 8
        'c': 4,                          # 'c' of value 4
        'e': 6,                          # 'e' of value 6
        'f': 4,                          # 'f' of value 4
    },
    'e': {'c': 8, 'd': 6, 'f': 3},       # Key 'e' is mapped to 'c' of value 8 and 'd' of value 6 and 'f' of value 3
    'f': {'e': 3, 'd': 4},               # Key 'f' is mapped to 'e' of value 3 and 'd' of value 4
}

source = 'a'                             # Key 'a' is set as the source
destination = 'f'                        # Key 'f' is set as the destination

unvisited = graph                        # Sets the graph dictionary as unvisited upon initialization
shortest_distances = {}                  # Create an empty dictionary called shortest_distances
route = []                               # Create an empty list called route
path_nodes = {}                          # Create an empty dictionary called path_nodes

for nodes in unvisited:                                 # Loops through unvisited dictionary, which loops through the graph dictionary and searches for nodes
    shortest_distances[nodes] = math.inf                # When those nodes are found, they are inserted into shortest_distances dictionary
                                                        # The math.inf constant returns a floating point positive infinity // Source: https://www.w3schools.com/python/ref_math_inf.asp
shortest_distances[source] = 0                          # Sets the source node, which is whatever key 'a' was in the dictionary to 0

while unvisited:                                        # Loops through until the graph dictionary is empty
    min_node = None                                     # Sets the minimum node (min_node) to None
    for current_node in unvisited:                      # Loops through unvisited dictionary, which loops through the graph dictionary and searches for current_node
                                                        # The goal of this loop is to find the node with the shortest distance from the source node
        if min_node is None:                                                    # Searches for min_node that fits the condition: is None, so if the min_node is nothing:
            min_node = current_node                                             # Then set the min_node to whatever is current_node
        elif shortest_distances[min_node] > shortest_distances[current_node]:   # If the previous condition is not met, search for the current_node in shortest_distances and make sure it is
                                                                                # smaller than the min_node is shortest_distances, then
            min_node = current_node                                             # Set it as the min_node
                                                                                # So if the node has a shorter distance than the minimum node, then set that as the new minimum node
    for (node, value) in unvisited[min_node].items():                           # Loops through neighbors of the min_node and searches for the node and value
        if value + shortest_distances[min_node] < shortest_distances[node]:     # Searches for min_node in shortest_distances dictionary, adding value to it that fits the condition that
                                                                                # It is smaller than node in shortest_distances dictionary
                                                                                # Basically if the distance from the source node to the neighbor through the minimum node is shorter than
                                                                                # whatever the current shortest distance to the neighbor is,
            shortest_distances[node] = value + shortest_distances[min_node]     # Then set that to the new shortest distance.
            path_nodes[node] = min_node                                         # Add this path from source node to its neighbor through the minimum node to the path_nodes dictionary
    unvisited.pop(min_node)                             # Removes the minimum node from the unvisited dictionary
node = destination                                      # Set the current node to destination, which was previously defined as key 'f'

while node != source:                                   # Loops through until node equals source
    try:                                                # The try block lets you test a block of code for errors // Source: https://www.w3schools.com/python/python_try_except.asp
        route.insert(0, node)                           # At index 0, insert into the route list the current node
        node = path_nodes[node]                         # Set the current node to the previous node in the path
    except Exception:                                   # The except block lets you handle the error // Source: https://www.w3schools.com/python/python_try_except.asp
        print('Path not reachable')                     # If this error occurs, print out 'Path not reachable' to the console
                                                        # This error would happen if there was no reachable path from the source node to the destination node
        break                                           # Terminates the current loop and resume execution at next statement // Source: https://www.tutorialspoint.com/python/python_break_statement.htm
route.insert(0, source)                                 # At index 0, insert the source node into the route list

if shortest_distances[destination] != math.inf:                                 # Searches for the destination node in shortest_distances dictionary that is not infinity
    print('Shortest distance is ' + str(shortest_distances[destination]))       # Print that out to the console as the shortest distance
    print('And the path is ' + str(route))                                      # Print out the route as a string, two values: the source node, and the destination node
