#! /usr/bin/python2.6
# AI Homework 1

from Queue import Queue

def create_graph(vertices, costs):
    graph = {}
    for each in vertices:
        graph[each] = {}
    
    for i in range(len(cost_matrix)):
	c = {}
	vertex1 = vertices[i]
	cost_list = cost_matrix[i]
	for j in range(len(cost_list)):
		vertex2 = vertices[j]
		c[vertex2] = cost_list[j]
	graph[vertex1] = c

    return graph

def read_input():
    # Read input
    # Assign only until last 2 chars
    # to ignore \r\n - carriage return, new line
    # Use -1 if running on Unix like environment;
    # i.e. ignore only last '\n'
    
    file = open('input.txt', 'r')
    
    task = file.readline()[:-1]
    source = file.readline()[:-1]
    dest = file.readline()[:-1]
    num_nodes = int(file.readline()[:-1])

    # Read node list
    nodes = []
    index = num_nodes
    while index > 0:
        nodes.append(file.readline()[:-1])
        index -= 1

    # Read cost matrix
    cost_matrix = []
    index = num_nodes
    while index > 0:
        cost_list = file.readline()[:-1].split()
        cost_list = [int(each) for each in cost_list]
        cost_matrix.append(cost_list)
        index -= 1

    return [task, source, dest, num_nodes, nodes, cost_matrix]

class Node:

    def __init__(self, state):
        self.state = state
        self.parent = None
        self.path_cost = 0
        self.depth = 0

    def __repr__(self):
        return repr((self.state, self.parent, self.path_cost, self.depth))
    
    def __str__(self):
        s = "Node("
        s += "state = '" + str(self.state) + "', "
        s += "parent = " + str(self.parent) + ", "
        s += "path_cost = " + str(self.path_cost) + ", "
        s += "depth = " + str(self.depth) + ", "
        s += ")"
        return s

def expand(graph, node, explored):
    frontier = []
    for each_child in graph[node.state]:
        if graph[node.state][each_child]:
            child = Node(each_child)
            child.parent = node
            child.path_cost = child.parent.path_cost + graph[node.state][each_child]
            child.depth = child.parent.depth + 1
            # TODO: Check for repeated states.
            # Refer slides 'session02-04', slide 106, 112
            # Slide 12 has 'Clean Robust Algorithm'
            # if not explored[each_child]:

            if not explored[child.state]:
                frontier.append(child)

    frontier = sorted(frontier, key=lambda node: node.state)
    return frontier

def bfs(graph, source, dest):
    # Initialisation    
    s = Node(source)
    Q = Queue()
    Q.put(s)
    explored = {}
    for each in graph:
        explored[each] = False
    explored[s.state] = True
    expansion = []

    # Main Loop
    while True:
        if Q.empty():
            return 'BFS Failed!'
        node = Q.get()
        expansion.append(node.state)
        if node.state == dest:
            return [node, expansion]
        frontier = expand(graph, node, explored)
        for each_node in frontier:
            Q.put(each_node)
            explored[each_node] = True

input = [task, source, dest, num_nodes, vertices, cost_matrix] = read_input()
graph = create_graph(vertices, cost_matrix)

[result, expansion] = bfs(graph, source, dest)
print expansion
print result