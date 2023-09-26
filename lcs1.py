import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}

        for vertex in vertices:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))

def dijkstra(graph, start, goal):
    min_heap = [(0, start, [])]
    visited = set()

    while min_heap:
        cost, current_vertex, path = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue

        path = path + [current_vertex]

        if current_vertex == goal:
            return path

        visited.add(current_vertex)

        for neighbor, weight in graph.adj_list[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (cost + weight, neighbor, path))

    return None

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 4)
graph.add_edge('C', 'D', 1)

start_node = 'A'
goal_node = 'D'

path = dijkstra(graph, start_node, goal_node)
if path:
    print(f"The lowest-cost path from {start_node} to {goal_node} is: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
