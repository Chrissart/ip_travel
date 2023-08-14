import networkx as nx
import matplotlib.pyplot as plt


def get_graph(
            transitions: dict,
            ip: str,
            graph=None,
            fig=None,
            ax=None,
            pos=None
        ) -> tuple:
    if graph is None:
        graph = nx.DiGraph()
        plt.ion()  # Activa el modo interactivo de matplotlib

    # Limpiar el grafo existente
    graph.clear()

    # Añadir aristas al grafo con pesos (probabilidades)
    for nivel, next_levels in transitions.items():
        for next_nivel, prob in next_levels.items():
            graph.add_edge(nivel, next_nivel, weight=prob)

    if fig is None or ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    # Si las posiciones no se han definido, calcularlas
    if pos is None:
        pos = nx.spring_layout(graph)

    # Limpiar el canvas para nuevas actualizaciones
    ax.clear()

    edges = graph.edges(data=True)

    # Dibujo los nodos
    nx.draw_networkx_nodes(graph, pos, node_color='skyblue', ax=ax)
    # Dibujo las etiquetas de los nodos
    nx.draw_networkx_labels(graph, pos, ax=ax)
    # Dibujo las aristas con flechas distintivas
    nx.draw_networkx_edges(
            graph,
            pos,
            arrowstyle='-|>',
            # Ver las dos aristas si existen entre dos vertices
            connectionstyle='arc3, rad = 0.1',
            arrowsize=20,
            edge_color='gray',
            ax=ax
        )
    # Dibujo las etiquetas de las aristas
    nx.draw_networkx_edge_labels(
            graph,
            pos,
            edge_labels={(u, v): f"{d['weight']:.2f}" for u, v, d in edges},
            label_pos=0.5,
            ax=ax
        )

    ax.set_title(f"Matriz de Transición como Grafo de la IP {ip}")
    plt.draw()
    plt.pause(0.1)  # Pequeña pausa para permitir que se actualice la visualización

    return graph, fig, ax, pos  # Agregar pos a la tupla de retorno
