import numpy as np


def tronco(altura, tamanho_aresta_base, tamanho_aresta_topo):
    # vertices do cubo
    vertices = np.array([
        [-tamanho_aresta_base / 2, -tamanho_aresta_base / 2, 0],  # Vértice 0
        [tamanho_aresta_base / 2, -tamanho_aresta_base / 2, 0],  # Vértice 1
        [tamanho_aresta_base / 2, tamanho_aresta_base / 2, 0],  # Vértice 2
        [-tamanho_aresta_base / 2, tamanho_aresta_base / 2, 0],  # Vértice 3
        [-tamanho_aresta_topo / 2, -tamanho_aresta_topo / 2, altura],  # Vértice 4
        [tamanho_aresta_topo / 2, -tamanho_aresta_topo / 2, altura],  # Vértice 5
        [tamanho_aresta_topo / 2, tamanho_aresta_topo / 2, altura],  # Vértice 6
        [-tamanho_aresta_topo / 2, tamanho_aresta_topo / 2, altura]  # Vértice 7
    ])

    # arestas do cubo
    # definir quais vertices estao ligados entre si na lista de vertices
    arestas = [
        [0, 1], [0, 3], [3, 2], [2, 1],
        [4, 5], [5, 6], [7, 4], [6, 7],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    return vertices, arestas
