# create_graph.py
import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    G = nx.Graph()

    streets_kyiv = ['Khreschatyk', 'Hrushevskoho Street', 'Volodymyrska Street', 'Andriivskyi Uzviz',
                    'Mykhailivska Square', 'Sophiivska Square', 'Zoloti Vorota', 'Besarabska Square']
    G.add_nodes_from(streets_kyiv)

    roads_kyiv = [('Khreschatyk', 'Hrushevskoho Street'), ('Khreschatyk', 'Volodymyrska Street'),
                  ('Hrushevskoho Street', 'Volodymyrska Street'), (
                      'Hrushevskoho Street', 'Mykhailivska Square'),
                  ('Volodymyrska Street',
                   'Sophiivska Square'), ('Sophiivska Square', 'Zoloti Vorota'),
                  ('Zoloti Vorota', 'Besarabska Square'), ('Sophiivska Square',
                                                           'Andriivskyi Uzviz'),
                  ('Andriivskyi Uzviz', 'Mykhailivska Square')]

    G.add_edges_from(roads_kyiv)

    return G


def analyze_graph(G):
    num_nodes = len(G.nodes)
    num_edges = len(G.edges)
    degree_centrality = nx.degree_centrality(G)

    print(f"Кількість вершин: {num_nodes}")
    print(f"Кількість ребер: {num_edges}")

    print("\nСтупінь вершин:")
    for node, degree in degree_centrality.items():
        print(f"{node}: {degree * (num_nodes - 1)}")

    # Візуалізація графа
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue',
            font_size=10, font_color='black', edge_color='gray', linewidths=1, alpha=0.7)

    # Показати граф
    plt.show()
