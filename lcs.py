import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, node) pairs
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we've already found a shorter path to this node
        if current_distance > distances[current_node]:
            continue

        for neighbor, cost in graph[current_node]:
            distance = current_distance + cost

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 1)],
    'D': [('B', 4), ('C', 1)]
}

# Example usage
start_node = 'A'
distances = dijkstra(graph, start_node)
print("Minimum distances from", start_node, "to each node:", distances)
