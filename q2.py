import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Line3DCollection

from objetos.cone import cone
from objetos.cilindro import cilindro
from objetos.esfera import criar_esfera
from objetos.cubo import cubo
from objetos.tronco import tronco
from objetos.toroide import toroide

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_title('Coordenadas do Mundo')
# Define os limites do gráfico
limites = [-10, 10]

# Desenha as linhas que dividem o espaço 3D em octantes para facilitar
# a identificação dos solidos em seus respectivos octantes
for s in [-1, 1]:
    ax.plot([0, 0], [0, 0], [s * limites[0], s * limites[1]], color='k', linestyle='--', linewidth=1)
    ax.plot([0, 0], [s * limites[0], s * limites[1]], [0, 0], color='k', linestyle='--', linewidth=1)
    ax.plot([s * limites[0], s * limites[1]], [0, 0], [0, 0], color='k', linestyle='--', linewidth=1)
    # Legenda

# definição dos octantes
ax.text(5, 5, 5, "octante 1")  # (+,+,+)
ax.text(-5, 5, 5, "octante 2")  # (-,+,+)
ax.text(-5, -5, 5, "octante 3")  # (-,-,+)
ax.text(5, -5, 5, "octante 4")  # (+,-,+)
ax.text(5, 5, -5, "octante 5")  # (+,+,-)
ax.text(-5, 5, -5, "octante 6")  # (-,+,-)
ax.text(-5, -5, -5, "octante 7")  # (-,-,-)
ax.text(5, -5, -5, "octante 8")  # (+,-,-)
# ax


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# matriz de translacao em coordenadas homogeneas
def matriz_translacao(tx, ty, tz):
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])


def matriz_escalonamento(sx, sy, sz):
    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]])


def rotacao_x(theta):
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ])


def rotacao_y(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ])


def rotacao_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def plot_3d(ax, vertices, arestas, transformacao, cor, rotacionar=False, angulo=0, eixo='x'):
    vertices_homogeneos = np.concatenate([vertices, np.ones((vertices.shape[0], 1))], axis=-1)

    vertices_transformados = (transformacao @ vertices_homogeneos.T).T
    if rotacionar:
        if eixo == 'x':
            vertices_transformados = (rotacao_x(angulo) @ vertices_transformados.T).T
        elif eixo == 'y':
            vertices_transformados = (rotacao_y(angulo) @ vertices_transformados.T).T
        else:
            vertices_transformados = (rotacao_z(angulo) @ vertices_transformados.T).T

    vertices_transformados = vertices_transformados[:, :3]
    linhas = [(vertices_transformados[aresta[0]], vertices_transformados[aresta[1]]) for aresta in arestas]
    ax.add_collection3d(Line3DCollection(linhas, colors=cor))

    return vertices_transformados


def questao_dois(eye = np.array([5, 5, -8])):
    # Esfera
    raio_esfera = 3
    vertices_esfera, arestas_esfera = criar_esfera(raio_esfera, 10)
    translacao_esfera = matriz_translacao(raio_esfera * 3, raio_esfera * 4, raio_esfera * 3)
    escala_esfera = matriz_escalonamento(1 / 2, 0.5, 0.5)
    pontos_esfera = plot_3d(ax, vertices_esfera, arestas_esfera, escala_esfera @ translacao_esfera, 'blue')

    # Cilindro
    raio_cilindro = 4
    vertices_cilindro, arestas_cilindro = cilindro(raio=raio_cilindro)
    translacao_cilindro = matriz_translacao(raio_cilindro + 1, raio_cilindro, 0)
    escala_cilindro = matriz_escalonamento(1 / 2, 0.5, 0.5)
    pontos_cilindro = plot_3d(ax, vertices_cilindro, arestas_cilindro, escala_cilindro @ translacao_cilindro, 'red')

    # Cubo
    tamanho_aresta = 3
    vertices_cubo, arestas_cubo = cubo(tamanho_aresta)
    translacao_cubo = matriz_translacao(7, 3, 0)
    escala_cubo = matriz_escalonamento(1, 1, 1)
    pontos_cubo = plot_3d(ax, vertices_cubo, arestas_cubo, escala_cubo @ translacao_cubo, 'green')

    # Cone
    raio_base_cone = 6
    vertices_cone, arestas_cone = cone(raio_base_cone)
    translacao_cone = matriz_translacao(-5, 8.5, 0)
    escala_cone = matriz_escalonamento(0.4, 0.4, 0.4)
    pontos_cone = plot_3d(ax, vertices_cone, arestas_cone, translacao_cone @ escala_cone, 'black', rotacionar=False,
                          angulo=(-np.pi / 5), eixo='y')

    # Tronco de pirâmide
    tamanho_base_tronco = 8
    tamanho_topo_tronco = 4
    altura_tronco = 5
    vertices_tronco, arestas_tronco = tronco(tamanho_aresta_base=tamanho_base_tronco,
                                             tamanho_aresta_topo=tamanho_topo_tronco, altura=altura_tronco)
    translacao_tronco = matriz_translacao(-5, 5, 0)
    escala_tronco = matriz_escalonamento(1, 0.6, 1)
    pontos_tronco = plot_3d(ax, vertices_tronco, arestas_tronco, escala_tronco @ translacao_tronco, 'yellow')

    # Toroide
    Raio_toroide = 2
    raio_toroide = 1
    vertices_toroide, arestas_toroide = toroide(r_raio=raio_toroide, R_raio=Raio_toroide,
                                                circunferencias_intermediarias=10)
    translacao_toroide = matriz_translacao(-1, 5, 10)
    escala_toroide = matriz_escalonamento(1, 0.6, 1)
    pontos_toroide = plot_3d(ax, vertices_toroide, arestas_toroide, escala_toroide @ translacao_toroide, 'grey',
                             rotacionar=True, angulo=(-np.pi / 4), eixo='y')

    ax.scatter(*zip(eye), color='black', s=100)

    plt.grid()
    plt.show()

    return {
        'pontos_esfera': pontos_esfera,
        'pontos_cilindro': pontos_cilindro,
        'pontos_cubo': pontos_cubo,
        'pontos_cone': pontos_cone,
        'pontos_tronco': pontos_tronco,
        'pontos_toroide': pontos_toroide,
        'arestas_esfera': arestas_esfera,
        'arestas_cilindro': arestas_cilindro,
        'arestas_cubo': arestas_cubo,
        'arestas_cone': arestas_cone,
        'arestas_tronco': arestas_tronco,
        'arestas_toroide': arestas_toroide,
    }