def find_path(start, end, graph, visited_paths):
    """Find the list of available paths"""
    output = False
    if end in graph[start]:
        output = True
        return output
    else:
        visited_paths.append(start)
        for i in graph[start]:
            if i not in visited_paths:
                output = find_path(i, end, graph, visited_paths)
                if output:
                    return output

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
    print(0)
else:
    path = find_path(a, b, nodes, [])
    if path:
        print(1)
    else:
        print(0)
