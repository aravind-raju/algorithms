def connected_nodes(start, end, graph, visited_paths, paths):
    """get list of connected nodes to a"""
    if end in graph[start]:
        paths.append(start)
    
    visited_paths.append(start)
    for i in graph[start]:
        if i not in visited_paths:
            connected_nodes(i, end, graph, visited_paths, paths)
    
    return paths
# get input nodes
n = int(input())
nodes = {}
for i in range(n):
    nodes[int(input())] = []

# get node edges
m = int(input())
for i in range(m):
    node_id, node_value = input().split()
    nodes[int(node_id)].append(int(node_value))

a = int(input())
b = int(input())

if a not in nodes.keys() or b not in nodes.keys():
    print(-1)
else:
    path = sorted(connected_nodes(a, b, nodes, [], []))
    if path:
        print(" ".join(list(map(str, path))))
    else:
        print(-1)