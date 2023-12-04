import matplotlib.pyplot as plt

from objetos.cilindro import cilindro
from objetos.cone import cone
from objetos.cubo import cubo
from objetos.esfera import criar_esfera
from objetos.toroide import toroide
from objetos.tronco import tronco


def questao_um():
    # Cilindro
    vertices, arestas = cilindro(raio=4)
    plot_solido(vertices, arestas)

    # Cone
    vertices, arestas = cone(raio=4)
    plot_solido(vertices, arestas)

    # Cubo
    tamanho_aresta = 5
    vertices_cubo, arestas_cubos = cubo(tamanho_aresta)
    plot_solido(vertices_cubo, arestas_cubos)

    # Toroide
    R = 2
    r = 1
    num_circles = 10
    vertices, arestas = toroide(r, R, num_circles)
    plot_solido(vertices, arestas)

    # Esfera
    vertices, arestas = criar_esfera(raio=2, num_esferas_intermediarias=10)
    plot_solido(vertices, arestas)

    # Tronco
    tamanho_base = 2
    tamanho_topo = 8
    altura = 4
    vertices, arestas = tronco(tamanho_base, tamanho_topo, altura)
    plot_solido(vertices, arestas)


def plot_solido(vertices, arestas):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for aresta in arestas:
        ax.plot3D(*zip(*vertices[aresta]), color='black')

    # Define os rótulos dos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    plt.show()
