'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def minimum_cost(start, end, graph, visited_paths, paths, current_cost):
    """Find the minimum cost"""
    if end in graph[start].keys():
        path_time = graph[start][end]
        paths[start] = current_cost + path_time
        visited_paths.append(start)
    
    for i in graph[start].keys():
        if i not in visited_paths:
            cost = graph[start][i] + current_cost
            minimum_cost(i, end, graph, visited_paths, paths, cost)
    
    return paths
# get input nodes
n = int(input())
nodes = {}
for i in range(n):
    nodes[int(input())] = {}

# get node edges
m = int(input())
for i in range(m):
    node_id, node_value, node_cost = input().split()
    if not nodes.get(int(node_id), None):
        nodes[int(node_id)] = {}
    nodes[int(node_id)][int(node_value)] = int(node_cost)

a = int(input())
b = int(input())

if a not in nodes.keys() or b not in nodes.keys():
    print(-1)
else:
    path = sorted(minimum_cost(a, b, nodes, [], {}, 0).values())
    if path:
        print(path[0])
    else:
        print(-1)