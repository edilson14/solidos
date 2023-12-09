import numpy as np


def cubo(tamanho_aresta):
    # vertices do cubo
    vertices = np.array([
        [-tamanho_aresta / 2, -tamanho_aresta / 2, 0],
        [tamanho_aresta / 2, -tamanho_aresta / 2, 0],
        [-tamanho_aresta / 2, tamanho_aresta / 2, 0],
        [-tamanho_aresta / 2, -tamanho_aresta / 2, tamanho_aresta],
        [tamanho_aresta / 2, tamanho_aresta / 2, 0],
        [tamanho_aresta / 2, -tamanho_aresta / 2, tamanho_aresta],
        [-tamanho_aresta / 2, tamanho_aresta / 2, tamanho_aresta],
        [tamanho_aresta / 2, tamanho_aresta / 2, tamanho_aresta]
    ])

    # arestas do cubo
    # definir quais vertices estao ligados entre si na lista de vertices
    arestas = [
        [0, 1], [0, 2], [0, 3], [1, 4],
        [1, 5], [2, 4], [2, 6], [3, 5],
        [3, 6], [4, 7], [5, 7], [6, 7]
    ]

    return vertices, arestas
