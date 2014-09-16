#! /usr/bin/python2.6
# AI Homework 1
from Queue import Queue
from collections import deque

import heapq
import pdb

global_nodes = []

##class PriorityQueue:
##    """
##      Implements a priority queue data structure. Each inserted item
##      has a priority associated with it and the client is usually interested
##      in quick retrieval of the lowest-priority item in the queue. This
##      data structure allows O(1) access to the lowest-priority item.
##
##      Note that this PriorityQueue does not allow you to change the priority
##      of an item.  However, you may insert the same item multiple times with
##      different priorities.
##    """
##    def  __init__(self):
##        self.heap = []
##        self.count = 0
##
##    def __str__(self):
##        return self.heap
##
##    def push(self, item, priority):
##        # FIXME: restored old behaviour to check against old results better
##        # FIXED: restored to stable behaviour
##        entry = (priority, self.count, item)
##        # entry = (priority, item)
##        heapq.heappush(self.heap, entry)
##        self.count += 1
##
##    def pop(self):
##        (_, _, item) = heapq.heappop(self.heap)
##        #  (_, item) = heapq.heappop(self.heap)
##        return item
##
##    def isEmpty(self):
##        return len(self.heap) == 0

def create_graph(vertices, cost_matrix):
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

class Node:
    
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.path_cost = 0
        self.depth = 0
    
    def __repr__(self):
        ##        node = {}
        ##        node['state'] = self.state
        ##        node['parent'] = self.parent
        ##        node['path_cost'] = self.path_cost
        ##        node['depth'] = self.depth
        ##        return repr(node)
        return repr((self.state, self.parent, self.path_cost, self.depth))
    
    def __str__(self):
        s = "Node("
        s += "state = '" + str(self.state) + "', "
        s += "parent = " + str(self.parent) + ", "
        s += "path_cost = " + str(self.path_cost) + ", "
        s += "depth = " + str(self.depth) + ", "
        s += ")"
        return s
    
    def __lt__(self, other):
        if_lesser = None
        if self.path_cost < other.path_cost:
            if_lesser = True
        elif other.path_cost < self.path_cost:
            is_lesser = False
        else: # case where path costs are same
            if self.state.lower() < other.state.lower():
                if_lesser = True
            elif self.state.lower > other.state.lower():
                if_lesser = False
        return if_lesser
    
    def __gt__(self, other):
        if_greater = False
        if self.path_cost > other.path_cost:
            if_greater = True
        elif self.path_cost < other.path_cost:
            if_greater = False
        else: # case where path_cost is the same
            if self.state.lower() > other.state.lower():
                if_greater = True
            elif self.state.lower < other.state.lower():
                if_greater = False
        return if_greater



def expand(graph, node, explored):
    frontier = []
    for each_child in graph[node.state]:
        if graph[node.state][each_child]:
            child = Node(each_child)
            child.parent = node
            child.path_cost = child.parent.path_cost + graph[node.state][each_child]
            child.depth = child.parent.depth + 1
            
            global_nodes.append(child)
            
            # TODO: Check for repeated states.
            # Refer slides 'session02-04', slide 106, 112
            # Slide 12 has 'Clean Robust Algorithm'
            # if not explored[each_child]:
            
            if not explored[child.state]:
                frontier.append(child)
    
    frontier = sorted(frontier, key=lambda node: node.state)
    return frontier


## Need to check for DFS
## Does the DFS go through the graph in alphabetical order?
## I may have to reverse the frontier list and then add it to stack
def dfs(graph, source, dest):
    # Initialisation
    s = Node(source)
    stack = []
    stack.append(s)
    explored = {}
    for each in graph:
        explored[each] = False
    explored[s.state] = True
    expansion = []
    
    # Main Loop
    while True:
        if not stack:
            return 'DFS Failed!'
        node = stack.pop()
        expansion.append(node.state)
        explored[node.state] = True
        if node.state == dest:
            return [node, expansion]
        frontier = expand(graph, node, explored)
        frontier.reverse() # TODO: Check if this is correct
        for each_node in frontier:
            stack.append(each_node)

def ucs(graph, source, dest):
    heap = []
    s = Node(source)
    heapq.heappush(heap, s)
    
    explored = {}
    for each in graph:
        explored[each] = False
    explored[s.state] = True
    expansion = []
    
    while True:
        if not heap:
            return 'UCS Failed'
        node = heapq.heappop(heap)
        expansion.append(node.state)
        explored[node.state] = True
        
        if node.state == dest:
            return [node, expansion]
        
        frontier = expand(graph, node, explored)
        for each_node in frontier:
            heapq.heappush(heap, each_node)


def bfs(graph, source, dest):
    # Initialisation
    # TODO:1 Check why nods are getting added twice to the explored queue
    s = Node(source)
    Q = deque()
    Q.append(s)
    explored = {}
    for each in graph:
        explored[each] = False
    explored[s.state] = True
    expansion = []
    
    # Main Loop
    while True:
        if not Q:
            return 'BFS Failed!'
        node = Q.popleft()
        expansion.append(node.state)
        explored[node.state] = True
        if node.state == dest:
            return [node, expansion]
        frontier = expand(graph, node, explored)
        for each_node in frontier:
            Q.append(each_node)
            ## Maybe this is requried only fro BFS
            ## -- Related to the above TODO:1
            explored[each_node.state] = True

def write_output(result, expansion):
    
    lines = []
    
    i = 0
    out = []
    while i < len(expansion):
        out.append(expansion[i])
        out.append('-')
        i += 1
    
    # Format output string from list
    lines.append(''.join(out[:-1]))
    
    node = result
    path = []
    while node != None:
        path.append(node.state)
        path.append('-')
        node = node.parent
    
    # Format output from path list
    path = path[:-1]
    path.reverse()
    lines.append(''.join(path))
    
    # Format total cost into output
    lines.append(str(result.path_cost))
    
    f = open('output.txt', 'w')
    f.writelines(lines)
    f.close()


v = ['an', 'bi', 'cl', 'da', 'al']
c = [[0,1,1,0,0],[1,0,5,4,0],[1,5,0,0,1],[0,4,0,0,0],[0,0,1,0,0]]
g = create_graph(v,c)
graph1 = {'Daniel': {'Daniel': 0, 'Elaine': 1, 'Claire': 0, 'Bill': 0, 'Andy': 1}, 'Elaine': {'Daniel': 1, 'Elaine': 0, 'Claire': 1, 'Bill': 1, 'Andy': 0}, 'Claire': {'Daniel': 0, 'Elaine': 1, 'Claire': 0, 'Bill': 0, 'Andy': 1}, 'Bill': {'Daniel': 0, 'Elaine': 1, 'Claire': 0, 'Bill': 0, 'Andy': 1}, 'Andy': {'Daniel': 1, 'Elaine': 0, 'Claire': 1, 'Bill': 1, 'Andy': 0}}
graph2 = {'Zoe': {'Zoe': 0, 'Bill': 1, 'Claire': 2, 'Daniel': 2, 'Elaine': 2, 'Andy': 0}, 'Bill': {'Zoe': 1, 'Bill': 0, 'Claire': 0, 'Daniel': 0, 'Elaine': 3, 'Andy': 4}, 'Claire': {'Zoe': 2, 'Bill': 0, 'Claire': 0, 'Daniel': 0, 'Elaine': 4, 'Andy': 3}, 'Daniel': {'Zoe': 2, 'Bill': 0, 'Claire': 0, 'Daniel': 0, 'Elaine': 2, 'Andy': 2}, 'Elaine': {'Zoe': 2, 'Bill': 3,'Claire': 4, 'Daniel': 2, 'Elaine': 0, 'Andy': 0}, 'Andy': {'Zoe': 0, 'Bill': 4, 'Claire': 3, 'Daniel': 2, 'Elaine': 0, 'Andy': 0}}
vertices = ['Andy', 'Bill', 'Claire', 'Daniel', 'Elaine']

# [result, expansion] = bfs(graph2, 'Andy', 'Zoe')

# write_output(result, expansion)
