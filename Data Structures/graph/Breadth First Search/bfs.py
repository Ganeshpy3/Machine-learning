edges=[(1,2),(1,4),(2,3),(2,5),(2,7),(2,8),(3,4),(3,10),(3,9),(5,6),(5,7),(5,8),(7,8)]
nodes=13


class Graph:
    def __init__(self, num_nodes, edges):
        self.data = [[] for _ in range(num_nodes)]
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

    def print(self):
        
        for i in range(len(self.data)):
            if len(self.data[i])>0:
                print(f"{i}:{self.data[i]}")
        return length




g1=Graph(nodes,edges)
g1.print()


def bfs(graph, source):
    visited = [False] * len(graph.data)
    queue = []

    visited[source] = True
    queue.append(source)
    i = 0

    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        i += 1

    return queue

    return queue

print(bfs(g1,3))
