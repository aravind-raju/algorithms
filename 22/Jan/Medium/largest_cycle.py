#question:
#1
#23
#4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21
from collections import defaultdict
 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.cycle = 0
        self.cycle_totals = []
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                self.cycle = sum([sum(self.graph[i]) for i, x in enumerate(recStack) if x])
                return True
 
        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False

    def cyclictotal(self, v, visited, total, visited_total, old_visited):
        visited.append(v)
        for neighbour in self.graph[v]:
            if neighbour in old_visited:
                return visited
            if neighbour not in visited:
                visited_total[neighbour] = total
                total += neighbour
                visited = self.cyclictotal(neighbour, visited, total, visited_total, old_visited)
            else:
                self.cycle_totals.append(total - visited_total[neighbour])
        return visited
 
    def LargestCyclicWeight(self):
        visited = []
        for node in range(self.V):
            if node not in visited:
                visited += self.cyclictotal(node, [], node, {node : 0}, visited)
        if self.cyclictotal:
            return max(self.cycle_totals)
        else:
            return -1

 
n = int(input())
for i in range(n):
    m = int(input())
    edges = list(map(int, input().split()))
    g = Graph(m)
    for i, j in enumerate(edges):
        g.addEdge(i, j)

    print(g.LargestCyclicWeight())