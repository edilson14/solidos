import numpy as np
from matplotlib import pyplot as plt

from q2 import questao_dois


def calcular_centro(pontos_transformados):
    # Calcule a média ao longo do eixo 0 para obter as coordenadas médias
    centro = np.mean(pontos_transformados, axis=0)
    return centro


def mostrar_solidos_no_sistema_de_camera(ax, pontos_solido, arestas_solido, matriz_transformacao, cor):
    # Transforma os pontos usando a matriz de transformação
    pontos_solidos_homogeneos = np.hstack((pontos_solido, np.ones((pontos_solido.shape[0], 1)))).T
    pontos_transformados = np.dot(matriz_transformacao, pontos_solidos_homogeneos).T

    pontos_transformados = pontos_transformados[:, :3]
    # Plota os pontos transformados
    for aresta in arestas_solido:
        ax.plot3D(*zip(*pontos_transformados[aresta]), color=cor)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


def questao_tres():
    # Pega pontos dos objetos da questão 2
    pontos = questao_dois()

    pontos_esfera = pontos['pontos_esfera']
    pontos_cilindro = pontos['pontos_cilindro']
    pontos_cubo = pontos['pontos_cubo']

    arestas_esfera = pontos['arestas_esfera']
    arestas_cilindro = pontos['arestas_cilindro']
    arestas_cubo = pontos['arestas_cubo']

    # Calcula o centro dos objetos
    centro_esfera = calcular_centro(pontos_esfera)
    centro_cilindro = calcular_centro(pontos_cilindro)
    centro_cubo = calcular_centro(pontos_cubo)

    at = (centro_esfera + centro_cilindro + centro_cubo) / 3.0  # Média dos centros

    eye = np.array([5, -6, 5])

    n = (at - eye)
    n /= np.linalg.norm(n)

    # Vetor auxiliar
    aux = np.array([0, 1, 0])

    u = np.cross(aux, n)
    u /= np.linalg.norm(u)

    v = np.cross(n, u)
    v /= np.linalg.norm(v)

    # A matriz de translação é obtida como a matriz que leva a posição da câmera p = (xc, yc, zc) para a origem
    T = np.array([
        [1, 0, 0, -eye[0]],
        [0, 1, 0, -eye[1]],
        [0, 0, 1, -eye[2]],
        [0, 0, 0, 1]
    ])

    # Matriz de rotação do Sistema de Coordenadas do Mundo para o da Câmera
    R = np.array([
        [u[0], u[1], u[2], 0],
        [v[0], v[1], v[2], 0],
        [n[0], n[1], n[2], 0],
        [0, 0, 0, 1]
    ])

    # Construindo a matriz de transformação
    matriz_transformacao = np.dot(R, T)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot([0, u[0] * 3], [0, u[1] * 3], [0, u[2] * 3], color='b', linestyle='dashed')
    ax.plot([0, v[0] * 3], [0, v[1] * 3], [0, v[2] * 3], color='r', linestyle='dashed')
    ax.plot([0, n[0] * -3], [0, n[1] * -3], [0, n[2] * -3], color='g', linestyle='dashed')
    ax.plot([0, aux[0] * 3], [0, aux[1] * 3], [0, aux[2] * 3], color='k', linestyle='dashed')

    # Adicionando descrições para cada linha
    ax.text(u[0] * 3, u[1] * 3, u[2] * 3, 'vetor u', color='b')
    ax.text(v[0] * 3, v[1] * 3, v[2] * 3, 'vetor v', color='r')
    ax.text(n[0] * -3, n[1] * -3, n[2] * -3, 'vetor n', color='g')
    ax.text(aux[0] * 3, aux[1] * 3, aux[2] * 3, 'vetor aux', color='k')

    mostrar_solidos_no_sistema_de_camera(ax, pontos_cubo, arestas_cubo, matriz_transformacao, 'g')
    mostrar_solidos_no_sistema_de_camera(ax, pontos_esfera, arestas_esfera, matriz_transformacao, 'b')
    mostrar_solidos_no_sistema_de_camera(ax, pontos_cilindro, arestas_cilindro, matriz_transformacao, 'r')

    plt.show()


questao_tres()
