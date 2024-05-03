from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.parent = defaultdict(int)
        self.distance = defaultdict(lambda: float('inf'))

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def get_path(self, start, goal):
        path, node = [], goal
        while node != start:
            path.append(node)
            node = self.parent[node]
        path.append(start)
        path.reverse()
        return path

    def bfs(self, start, goal):
        self.distance.clear()  # Reset distance dictionary
        self.parent.clear()    # Reset parent dictionary
        self.distance[start] = 0
        frontier = {start}
        while frontier:
            a = frontier.pop()
            for b in self.graph[a]:
                if self.distance[b] == float('inf'):
                    self.distance[b] = self.distance[a] + 1
                    self.parent[b] = a
                    frontier.add(b)
        if self.distance[goal] == float('inf'):
            return None, -1
        else:
            path = self.get_path(start, goal)
            return path, self.distance[goal]

def main():
    print('\nBreadth First Search (BFS)')
    print('\nNOTE:')
    print('1. Each of the following input lines require spaced separated entries.')
    print('2. Nodes are numbered from 1 to N by the program, where N is the total number of nodes.')
    graph = Graph()
    num_nodes, num_edges = map(int, input('\nEnter number of nodes, number of edges: ').split())
    for i in range(1, num_nodes + 1):
        graph.distance[i] = float('inf')
    print('\n')
    for i in range(num_edges):
        a, b = map(int, input('Enter initial node, end node of edge ' + str(i + 1) + ': ').split())
        graph.add_edge(a, b)
    start, goal = map(int, input('\nEnter start node, goal node: ').split())
    path, distance = graph.bfs(start, goal)
    if distance == -1:
        print('\nPath from start node to goal node does not exist.\n')
    else:
        path_route = ' --> '.join(map(str, path))
        print('\nPath from start node to goal node:', path_route)
        print('Total path distance:', distance, '\n')

if __name__ == '__main__':
    main()
