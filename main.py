#  main.py
import networkx as nx
import matplotlib.pyplot as plt
from create_graph import create_graph, analyze_graph
from dfs_algorithm import dfs
from bfs_algorithm import bfs
from dijkstra_algorithm import dijkstra


def main():
    # Завдання 1: Створення та аналіз графа
    graph = create_graph()
    analyze_graph(graph)

    # Завдання 2: Виклик DFS та BFS
    start_node_dfs = 'Khreschatyk'
    end_node_dfs = 'Besarabska Square'
    dfs_paths = dfs(graph, start_node_dfs, end_node_dfs)
    print(f"\nDFS Paths from {start_node_dfs} to {end_node_dfs}: {dfs_paths}")

    start_node_bfs = 'Khreschatyk'
    end_node_bfs = 'Besarabska Square'
    bfs_path = bfs(graph, start_node_bfs, end_node_bfs)
    print(f"BFS Path from {start_node_bfs} to {end_node_bfs}: {bfs_path}")

    # Завдання 3: Виклик алгоритму Дейкстри
    start_node_dijkstra = 'Khreschatyk'
    dijkstra_distances = dijkstra(graph, start_node_dijkstra)
    print(
        f"\nDijkstra Distances from {start_node_dijkstra}: {dijkstra_distances}")

    # Візуалізація графа
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue',
            font_size=10, font_color='black', edge_color='gray', linewidths=1, alpha=0.7)

    # Показати граф
    plt.show()


if __name__ == "__main__":
    main()
