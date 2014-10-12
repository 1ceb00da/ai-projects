#! /usr/bin/python2.6
# AI Homework 1
from collections import deque
from heapq import heappush
from heapq import heappop

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

def read_input():
    # Read input
    # Assign only until last 2 chars
    # to ignore \r\n - carriage return, new line
    # Use -1 if running on Unix like environment;
    # i.e. ignore only last '\n'
    
    file = open('input.txt', 'rU')
    
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
            return 'NoPathAvailable'
        node = stack.pop()
        expansion.append(node.state)
        explored[node.state] = True
        if node.state == dest:
            return [node, expansion]
        frontier = expand(graph, node, explored)
        frontier.reverse()
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
            return 'NoPathAvailable'
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
            return 'NoPathAvailable'
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
    lines.append('')
    
    with open('output.txt', 'w') as f:
        f.write('\n'.join(lines))

#################################
## Robust asearch algorithms conforming to
## "alphabetical pop" special contraint
def popleft(q):
    # use depth instead of path_cost for bfs and dfs
    candidates = [node for node in q if node.depth == q[0].depth]
    candidates = sorted(candidates, key=lambda node: node.state)
    popped = candidates[0]
    q.remove(popped)
    return popped

def pop(stack):
    candidates = [node for node in stack if stack[-1].depth == node.depth]
    candidates = sorted(candidates, key=lambda node: node.state)
    popped = candidates[0]
    stack.remove(popped)
    return popped

def expand(graph, node, explored):
    frontier = []
    for each_child in graph[node.state]:
        if graph[node.state][each_child]:
            child = Node(each_child)
            child.parent = node
            child.path_cost = child.parent.path_cost + graph[node.state][each_child]
            child.depth = child.parent.depth + 1
            if not explored[child.state]:
                frontier.append(child)
    frontier = sorted(frontier, key=lambda node: node.state)
    return frontier

## Robust bfs
def getChildren(graph, node):
    children = []
    for each_child in graph[node.state]:
        if graph[each_child][node.state]:
            child = Node(each_child)
            child.parent = node
            child.path_cost = child.parent.path_cost + graph[node.state][each_child]
            child.depth = child.parent.depth + 1
            children.append(child)
    return children

def robust_bfs(graph, source, dest):
    openq = deque()
    closedq = deque()
    s = Node(source)
    openq.append(s)
    log = []
    
    while True:
        #import pdb; pdb.set_trace()
        if not openq:
            return 'NoPathAvailable'
        current = popleft(openq)
        log.append(current.state)
        if current.state == dest:
            return [current, log]
        children = getChildren(graph, current)
        closedq.append(current)
        while children:
            child = children.pop()
            open_ = [node.state for node in openq]
            closed_ = [node.state for node in closedq]
            
            if child.state not in open_ and child.state not in closed_:
                openq.append(child)
            elif child.state in open_:
                node = [node for node in openq if node.state == child.state].pop()
                if node.path_cost > child.path_cost:
                    openq.remove(node)
                    openq.append(child)
            elif child.state in closed_:
                node = [node for node in closedq if node.state == child.state].pop()
                if node.path_cost > child.path_cost:
                    closedq.remove(node)
                    openq.append(child)
## End robust_bfs
##
## Begin robust_dfs

def robust_dfs(graph, source, dest):
    openq = deque()
    closedq = deque()
    s = Node(source)
    openq.append(s)
    log = []
    
    while True:
        if not openq:
            return 'NoPathAvailable'
        current = pop(openq)
        log.append(current.state)
        if current.state == dest:
            return [current, log]
        children = getChildren(graph, current)
        closedq.append(current)
        while children:
            child = children.pop()
            open_ = [node.state for node in openq]
            closed_ = [node.state for node in closedq]
            
            if child.state not in open_ and child.state not in closed_:
                openq.append(child)
            elif child.state in open_:
                node = [node for node in openq if node.state == child.state].pop()
                if node.path_cost > child.path_cost:
                    openq.remove(node)
                    openq.append(child)
            elif child.state in closed_:
                node = [node for node in closedq if node.state == child.state].pop()
                if node.path_cost > child.path_cost:
                    closedq.remove(node)
                    openq.append(child)


## End robust_dfs

## Begin robust_ucs

def robust_ucs(graph, source, dest):
    openq = list()
    closedq = deque()
    s = Node(source)
    heappush(openq, s)
    log = []
    
    while True:
        if not openq:
            return 'NoPathAvailable'
        current = heappop(openq)
        log.append(current.state)
        if current.state == dest:
            return [current, log]
        children = getChildren(graph, current)
        closedq.append(current)
        while children:
            child = children.pop()
            open_ = [node.state for node in openq]
            closed_ = [node.state for node in closedq]
            
            if child.state not in open_ and child.state not in closed_:
                heappush(openq, child)
            elif child.state in open_:
                node = [node for node in openq if node.state == child.state].pop()
                if node.path_cost > child.path_cost:
                    openq.remove(node)
                    heappush(openq, child)
            elif child.state in closed_:
                node = [node for node in closedq if node.state == child.state].pop()
                if node.path_cost > child.path_cost:
                    closedq.remove(node)
                    heappush(openq, child)

## End robust_ucs
#################################

input_ = [task, source, dest, num_nodes, vertices, cost_matrix] = read_input()
graph = create_graph(vertices, cost_matrix)

if task == '1':
    [result, expansion] = robust_bfs(graph, source, dest)

elif task == '2':
    [result, expansion] = robust_dfs(graph, source, dest)

elif task == '3':
    [result, expansion] = robust_ucs(graph, source, dest)

write_output(result, expansion)


## g = {'al': {'al': 0, 'da': 0, 'cl': 1, 'bi': 0, 'an': 0}, 'da': {'al': 0, 'da': 0, 'cl': 0, 'bi': 4, 'an': 0}, 'cl': {'al': 1, 'da': 0, 'cl': 0, 'bi': 5, 'an': 1}, 'bi': {'al': 0, 'da': 4, 'cl': 5, 'bi': 0, 'an': 1}, 'an': {'al': 0, 'da': 0, 'cl': 1, 'bi': 1, 'an': 0}}
##
## print "BFS -- s-'an', d-'al' for g in handout", robust_bfs(g, 'an', 'al')
## print "DFS -- s-'an', d-'al' for g in handout", robust_dfs(g, 'an', 'al')
## print "UCS -- s-'an', d-'al' for g in handout", robust_ucs(g, 'an', 'al')
