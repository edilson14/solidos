import numpy as np


def criar_esfera(raio, num_esferas_intermediarias):
    theta = np.linspace(0, np.pi, num_esferas_intermediarias + 2)
    phi = np.linspace(0, 2 * np.pi, num_esferas_intermediarias + 2)

    theta, phi = np.meshgrid(theta, phi)

    # Criação de vértices
    x = raio * np.sin(theta) * np.cos(phi)
    y = raio * np.sin(theta) * np.sin(phi)
    z = raio * np.cos(theta)

    vertices = np.vstack([x.flatten(), y.flatten(), z.flatten()]).T

    # Criação de arestas
    arestas = []
    num_phi = num_esferas_intermediarias + 2

    for i in range(num_esferas_intermediarias + 1):
        for j in range(num_phi - 1):
            arestas.append([i * num_phi + j, i * num_phi + j + 1])
            arestas.append([i * num_phi + j, (i + 1) * num_phi + j])

        arestas.append([(i + 1) * num_phi - 1, i * num_phi])

    return vertices, np.array(arestas)
