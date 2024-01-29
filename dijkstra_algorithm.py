# dijkstra_algorithm.py
import networkx as nx


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        current_node = min(
            (node for node in graph.nodes if node not in visited),
            key=lambda node: distances[node]
        )

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph.get_edge_data(
                current_node, neighbor).get('weight', 1)
            new_distance = distances[current_node] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances
