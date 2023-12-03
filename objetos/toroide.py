import numpy as np


def toroide(r_raio, R_raio, circunferencias_intermediarias):
    phi = np.linspace(0, 2 * np.pi, circunferencias_intermediarias + 1)
    theta = np.linspace(0, 2 * np.pi, circunferencias_intermediarias + 1)

    phi, theta = np.meshgrid(phi, theta)
    x = (R_raio + r_raio * np.cos(phi)) * np.cos(theta)
    y = (R_raio + r_raio * np.cos(phi)) * np.sin(theta)
    z = r_raio * np.sin(phi)

    vertices = np.column_stack([x.flatten(), y.flatten(), z.flatten()])

    arestas = []
    for i in range(circunferencias_intermediarias + 1):
        for j in range(circunferencias_intermediarias + 1):
            if j < circunferencias_intermediarias:
                arestas.append([i * (circunferencias_intermediarias + 1) + j,
                                i * (circunferencias_intermediarias + 1) + j + 1])
            if i < circunferencias_intermediarias:
                arestas.append([i * (circunferencias_intermediarias + 1) + j,
                                (i + 1) * (circunferencias_intermediarias + 1) + j])

    return vertices, arestas
