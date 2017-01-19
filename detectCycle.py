import fileinput


class Edge:
    def __init__(self, end=0, weight=0):
        self.end = end
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = set()       # Set of vertices of the graph
        self.edges = {}             # Graph represented as adjacency list

    def addEdge(self, start, end, weight):
        self.vertices.add(start)
        self.vertices.add(end)
        if start in self.edges.keys():
            self.edges[start].append(Edge(end, weight))
        else:
            self.edges[start] = [Edge(end, weight)]

    def printGraph(self):
        for v in self.edges.keys():
            for u in self.edges[v]:
                print '{} --> {} {}'.format(v, u.end, weight)

    def detectCycle(self, graph):
        dfs_stack = []          # Stack for DFS traversal of graph
        visited = set()         # Set of visited vertices
        stack_set = set()       # Set of vertices on dfs_stack

        for v in graph.vertices:
            if v not in visited:
                stack_set.add(v)
                dfs_stack.append(v)
                while len(dfs_stack) > 0:
                    v = dfs_stack[-1]
                    flag = 0                                        # Flag is set when a new node is added on dfs_stack
                    for u in graph.edges.setdefault(v, []):         # For all neighbours of node v
                        if u.end not in visited:
                            # This condition checks if adding the new node would cause a cycle.
                            # If a previously unvisited neighbour of v is on the same stack as v,
                            # i.e there is a path from v to v, it means that the graph will have a cycle.
                            if u.end in stack_set:
                                print "Cycle Found"
                                return True
                            dfs_stack.append(u.end)
                            stack_set.add(u.end)
                            flag = 1
                            break
                    # If the current v is not left with an unvisited neighbour, thus indicating that it had
                    # served its purpose, it must be popped and marked visited.
                    if flag == 0:
                        s = dfs_stack.pop()
                        visited.add(s)
                        stack_set.remove(s)
        print "No Cycle found"
        return False


if __name__ == '__main__':
    print "Enter edges in the format : <Start> <End> <Weight>"
    graph = Graph()
    for line in fileinput.input():
        start, end, weight = [int(i) for i in line.split()]
        graph.addEdge(start, end, weight)
    graph.printGraph()
    print graph.detectCycle(graph)
