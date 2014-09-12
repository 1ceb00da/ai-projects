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

def expand(graph, node):
    frontier = []
    for each in graph[node]:
        if graph[node][each]:
            frontier.append(each)
    frontier.sort()
    return frontier

def bfs(graph, source, dest):
    # Initialisation
    Q = Queue()
    explored = {}
    for each in graph:
        explored[each] = False
    
    explored[source] = True
    Q.put(source)
    
    while True:
        if Q.empty():
            return 'BFS Failed!'
        node = Q.get()
        if node == dest:
            return 'BFS success!'
        frontier = expand(graph, node)
        for each in frontier:
            if not explored[each]:
                explored[each] = True
                Q.put(each)
    

input = [task, source, dest, num_nodes, vertices, cost_matrix] = read_input()
graph = create_graph(vertices, cost_matrix)

print bfs(graph, source, dest)
print graph