import numpy as np


def cubo(tamanho_aresta):
    # vertices do cubo
    vertices = np.array([
        [0, 0, 0],
        [tamanho_aresta, 0, 0],
        [0, tamanho_aresta, 0],
        [tamanho_aresta, tamanho_aresta, 0],
        [0, 0, tamanho_aresta],
        [tamanho_aresta, 0, tamanho_aresta],
        [0, tamanho_aresta, tamanho_aresta],
        [tamanho_aresta, tamanho_aresta, tamanho_aresta],
    ])

    # arestas do cubo
    # definir quais vertices estao ligados entre si na lista de vertices
    arestas = [
        [0, 1], [1, 3], [3, 2], [2, 0],
        [4, 5], [5, 7], [7, 6], [6, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    return vertices, arestas
