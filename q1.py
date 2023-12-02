import numpy as np
import matplotlib.pyplot as plt


def cilindro(raio, quantidade_pontos_circulo=20):
    altura = 2 * raio
    centro = (0, 0, 0)
    coordenada_z = np.linspace(centro[2], centro[2] + altura, quantidade_pontos_circulo + 1)
    pontos_cilindro = []

    for i in range(quantidade_pontos_circulo):
        theta = np.linspace(0, 2 * np.pi, quantidade_pontos_circulo)
        x = centro[0] + raio * np.cos(theta)
        y = centro[1] + raio * np.sin(theta)
        z = np.full_like(theta, coordenada_z[i])
        pontos_cilindro.append((x, y, z))

    return pontos_cilindro


def plotar_cilindro(pontos_cilindro):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(len(pontos_cilindro)):
        if i == 0:
            x_start = pontos_cilindro[i][0]
            y_start = pontos_cilindro[i][1]
            z_start = pontos_cilindro[i][2]
        if i == (len(pontos_cilindro) - 1):
            x_end = pontos_cilindro[i][0]
            y_end = pontos_cilindro[i][1]
            z_end = pontos_cilindro[i][2]

        x, y, z = pontos_cilindro[i]
        ax.plot(x, y, z, color='blue')
    for i in range(0, len(x_start)):
        ax.plot([x_start[i], x_end[i]], [y_start[i], y_end[i]], [z_start[i], z_end[i]], color="blue")

    plt.grid()
    plt.show()


def cone(circunferencias_intermediarias: int, raio_tampa: int, quantidade_pontos_circulo=20):
    pontos_cone = []
    centro = (0, 0, 0)
    altura = 3 * raio_tampa

    coordenada_z = np.linspace(centro[2], centro[2] + altura, circunferencias_intermediarias)

    for i in range(circunferencias_intermediarias):
        theta = np.linspace(0, 2 * np.pi, quantidade_pontos_circulo)
        r = raio_tampa * (1 - (i / circunferencias_intermediarias) * (1 - raio_tampa))
        x = centro[0] + r * np.cos(theta)
        y = centro[1] + r * np.sin(theta)
        z = np.full_like(theta, coordenada_z[i])
        pontos_cone.append((x, y, z))
    return pontos_cone


def plotar_cone(pontos_cone):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(len(pontos_cone)):
        ax.plot(x, y, z, color='blue')
        if i == 0:
            x_start = x
            y_start = y
            z_start = z
        if i == (circunferencias_intermediarias - 1):
            x_end = x
            y_end = y
            z_end = z
    for i in range(0, len(x_start)):
        ax.plot([x_start[i], x_end[i]], [y_start[i], y_end[i]], [z_start[i], z_end[i]], color="blue")

    plt.grid()
    plt.show()


def esfera(raio):
    pi = np.pi
    u, v = np.mgrid[0:2 * pi:20j, 0:pi:10j]
    x = raio * np.cos(u) * np.sin(v)
    y = raio * np.sin(u) * np.sin(v)
    z = raio * np.cos(v)
    return x, y, z


def plotar_esfera(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z, color='w', edgecolor='r')
    plt.show()


def cubo(tamanho_aresta):
    # vertices do cubo
    vertices = [
        [0, 0, 0],
        [tamanho_aresta, 0, 0],
        [0, tamanho_aresta, 0],
        [tamanho_aresta, tamanho_aresta, 0],
        [0, 0, tamanho_aresta],
        [tamanho_aresta, 0, tamanho_aresta],
        [0, tamanho_aresta, tamanho_aresta],
        [tamanho_aresta, tamanho_aresta, tamanho_aresta],
    ]

    # arestas do cubo
    # definir quais vertices estao ligados entre si na lista de vertices
    arestas = [
        [0, 1], [1, 3], [3, 2], [2, 0],
        [4, 5], [5, 7], [7, 6], [6, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    return vertices, arestas


def plotar_cubo(vertices, arestas, tamanho_aresta):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # plotar os vertices
    for aresta in arestas:
        x = [vertices[aresta[0]][0], vertices[aresta[1]][0]]
        y = [vertices[aresta[0]][1], vertices[aresta[1]][1]]
        z = [vertices[aresta[0]][2], vertices[aresta[1]][2]]
        ax.plot(x, y, z, color='k')

    ax.set_xlim(0, tamanho_aresta)
    ax.set_ylim(0, tamanho_aresta)
    ax.set_zlim(0, tamanho_aresta)
    plt.show()


def tronco_piramide(tamanho_base, tamanho_topo, altura):
    # vertices do tronco de piramide
    vertices = np.array([
        [-tamanho_base / 2, -tamanho_base / 2, 0],  # primeiro vertice
        [tamanho_base / 2, -tamanho_base / 2, 0],  # segundo vertice
        [tamanho_base / 2, tamanho_base / 2, 0],  # terceiro vertice
        [-tamanho_base / 2, tamanho_base / 2, 0],  # quarto vertice
        [-tamanho_topo / 2, -tamanho_topo / 2, altura],  # quinto vertice
        [tamanho_topo / 2, -tamanho_topo / 2, altura],  # sexto vertice
        [tamanho_topo / 2, tamanho_topo / 2, altura],  # setimo vertice
        [-tamanho_topo / 2, tamanho_topo / 2, altura],  # oitavo vertice
    ])

    faces = [
        [0, 1, 5, 4],  # base inferior
        [1, 2, 6, 5],  # face lateral
        [2, 3, 7, 6],  # topo
        [3, 0, 4, 7],  # face lateral
        [4, 5, 6, 7]  # lateral
    ]
    return vertices, faces


def plotar_tronco_piramide(vertices, faces, tamanho_base, tamanho_topo, altura):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # plotar as faces
    for face in faces:
        x = vertices[face, 0]
        y = vertices[face, 1]
        z = vertices[face, 2]

        ax.plot(x, z, y, color='k')

    tamanho_maximo = max(tamanho_base, tamanho_topo, altura)
    ax.set_xlim(-tamanho_maximo, tamanho_maximo)
    ax.set_ylim(-tamanho_maximo, tamanho_maximo)
    ax.set_zlim(0, altura)
    plt.show()


def toroide(raio_origem_toroide, raio_abertura_toroide, quantidades_pontos_circulo=30, num_points_per_circle=100,
            origin=np.array([0, 0, 0])):
    # Inicializa as listas para armazenar vértices e arestas
    vertices = []
    edges = []

    # Gera os vértices do toroide
    # quanto maior for a quantidade de circunferencias, mais redondo será o toroide
    for i in range(quantidades_pontos_circulo):
        theta = 2 * np.pi * i / quantidades_pontos_circulo
        circle_center = np.array([raio_origem_toroide * np.cos(theta), raio_origem_toroide * np.sin(theta), 0])

        for j in range(num_points_per_circle):
            phi = 2 * np.pi * j / num_points_per_circle
            point = circle_center + np.array(
                [raio_abertura_toroide * np.cos(phi), raio_abertura_toroide * np.sin(phi), 0])
            vertices.append(point)

    # Gera as arestas do toroide
    for i in range(quantidades_pontos_circulo):
        for j in range(num_points_per_circle):
            current_index = i * num_points_per_circle + j
            next_index = (i + 1) % quantidades_pontos_circulo * num_points_per_circle + j

            edges.append((current_index, next_index))

    return np.array(vertices), edges


def plot_toroide(r_raio, R_raio, circunferencias_intermediarias):
    phi = np.linspace(0, 2 * np.pi, circunferencias_intermediarias + 1)
    theta = np.linspace(0, 2 * np.pi, circunferencias_intermediarias + 1)

    phi, theta = np.meshgrid(phi, theta)
    x = (R_raio + r_raio * np.cos(phi)) * np.cos(theta)
    y = (R_raio + r_raio * np.cos(phi)) * np.sin(theta)
    z = r_raio * np.sin(phi)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z, alpha=0.5)

    plt.show()

# Exemplo de uso
R = 10
r = 5
num_circles = 30
plot_toroide(r_raio=5, R_raio=10, circunferencias_intermediarias=30)

tamanho_base = 2
tamanho_topo = 8
altura = 4
vertices_piramide, faces_piramide = tronco_piramide(tamanho_base, tamanho_topo, altura)
plotar_tronco_piramide(vertices_piramide, faces_piramide, tamanho_base, tamanho_topo, altura)

pontos_cone = cone(4, 3)
plotar_cilindro(pontos_cone)

pontos_cilindro = cilindro(raio=4, quantidade_pontos_circulo=10)
plotar_cilindro(pontos_cilindro)

x, y, z = esfera(raio=4)
plotar_esfera(x, y, z)

tamanho_aresta = 5
vertices_cubo, arestas_cubos = cubo(tamanho_aresta)
plotar_cubo(vertices_cubo, arestas_cubos, tamanho_aresta)
