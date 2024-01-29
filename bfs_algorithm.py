#  bfs_algorithm.py
def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in graph[node]:
            if next_node not in path:
                new_path = path + [next_node]
                queue.append((next_node, new_path))
                if next_node == end:
                    return new_path
