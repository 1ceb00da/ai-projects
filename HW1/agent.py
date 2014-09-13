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
    
import pdb

class Node:
    count = -1
    
    def reset():
        count = -1

    def __init__(self, state):
        self.__class__.count = self.count + 1
        self.num = self.count
        self.state = state
        self.parent = None
        self.path_cost = 0
        self.depth = 0
        self.is_explored = False

    def __repr__(self):
        return repr((self.num, self.state, self.parent, self.path_cost, self.depth, self.is_explored))
    
    def __str__(self):
        s = "Node("
        s += "num = " + str(self.num) + ", "
        s += "state = '" + str(self.state) + "', "
        s += "parent = " + str(self.parent) + ", "
        s += "path_cost = " + str(self.path_cost) + ", "
        s += "depth = " + str(self.depth) + ", "
        s += "is_explored = " + str(self.is_explored)
        s += ")"
        return s

def _expand(graph, node):
    frontier = []
    for each_successor in graph[node.state]:
        if graph[node.state][each_successor]:
            successor = Node(each_successor)
            successor.parent = node.num
            successor.path_cost = successor.path_cost + graph[node.state][each_successor]
            successor.depth += 1
            frontier.append(successor)
    # frontier.sort()
    frontier = sorted(frontier, key=lambda node: node.state)
    return frontier

def _bfs(graph, source, dest):
    # Initialisation
##    Q = Queue()
##    explored = {}
##    for each in graph:
##        explored[each] = False
##    
##    explored[source] = True
##    Q.put(source)

    s = Node(source)
    s.is_explored = True
    Q = Queue()
    steps = []
    steps.append(s)
    Q.put(s)
    
    while True:
        if Q.empty():
            return 'BFS Failed!'
        node = Q.get()
        if node.state == dest:
            return [node, steps]
        frontier = expand(graph, node)
        for each_node in frontier:
           # pdb.set_trace()
            if not each_node.is_explored:
                each_node.is_explored = True
                Q.put(each_node)
                steps.append(each_node)
    

graph1 = {'Daniel': {'Daniel': 0, 'Elaine': 1, 'Claire': 0, 'Bill': 0, 'Andy': 1}, 'Elaine': {'Daniel': 1, 'Elaine': 0, 'Claire': 1, 'Bill': 1, 'Andy': 0}, 'Claire': {'Daniel': 0, 'Elaine': 1, 'Claire': 0, 'Bill': 0, 'Andy': 1}, 'Bill': {'Daniel': 0, 'Elaine': 1, 'Claire': 0, 'Bill': 0, 'Andy': 1}, 'Andy': {'Daniel': 1, 'Elaine': 0, 'Claire': 1, 'Bill': 1, 'Andy': 0}}
graph2 = {'Zoe': {'Zoe': 0, 'Bill': 1, 'Claire': 2, 'Daniel': 2, 'Elaine': 2, 'Andy': 0}, 'Bill': {'Zoe': 1, 'Bill': 0, 'Claire': 0, 'Daniel': 0, 'Elaine': 3, 'Andy': 4}, 'Claire': {'Zoe': 2, 'Bill': 0, 'Claire': 0, 'Daniel': 0, 'Elaine': 4, 'Andy': 3}, 'Daniel': {'Zoe': 2, 'Bill': 0, 'Claire': 0, 'Daniel': 0, 'Elaine': 2, 'Andy': 2}, 'Elaine': {'Zoe': 2, 'Bill': 3,'Claire': 4, 'Daniel': 2, 'Elaine': 0, 'Andy': 0}, 'Andy': {'Zoe': 0, 'Bill': 4, 'Claire': 3, 'Daniel': 2, 'Elaine': 0, 'Andy': 0}}
vertices = ['Andy', 'Bill', 'Claire', 'Daniel', 'Elaine']

[node, steps] = bfs(graph1, 'Andy', 'Elaine')
print node
print steps
input = [task, source, dest, num_nodes, vertices, cost_matrix] = read_input()
graph = create_graph(vertices, cost_matrix)

print bfs(graph, source, dest)
print graph