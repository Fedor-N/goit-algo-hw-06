# main.py
from create_graph import create_graph, analyze_graph
from dfs_algorithm import dfs
from bfs_algorithm import bfs


def main():
    # Створення та аналіз графа
    graph = create_graph()
    analyze_graph(graph)

    # Виклик DFS
    start_node_dfs = 'Khreschatyk'
    end_node_dfs = 'Besarabska Square'
    dfs_paths = dfs(graph, start_node_dfs, end_node_dfs)
    print(f"\nDFS Paths from {start_node_dfs} to {end_node_dfs}: {dfs_paths}")

    # Виклик BFS
    start_node_bfs = 'Khreschatyk'
    end_node_bfs = 'Besarabska Square'
    bfs_path = bfs(graph, start_node_bfs, end_node_bfs)
    print(f"BFS Path from {start_node_bfs} to {end_node_bfs}: {bfs_path}")


if __name__ == "__main__":
    main()
