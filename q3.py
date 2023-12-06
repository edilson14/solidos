import numpy as np
from matplotlib import pyplot as plt

from q2 import questao_dois


def calcular_centro(pontos_transformados):
    # Calcule a média ao longo do eixo 0 para obter as coordenadas médias
    centro = np.mean(pontos_transformados, axis=0)
    return centro


def mostrar_solidos_no_sistema_de_camera(ax, pontos_solidos, matriz_transformacao, cor):
    # Transforma os pontos usando a matriz de transformação
    pontos_solidos_homogeneos = np.hstack((pontos_solidos, np.ones((pontos_solidos.shape[0], 1)))).T
    pontos_transformados = np.dot(matriz_transformacao, pontos_solidos_homogeneos).T

    # Plota os pontos transformados
    ax.plot(pontos_transformados[:, 0], pontos_transformados[:, 1], pontos_transformados[:, 2], c=cor)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


def questao_tres():
    # Pega pontos dos objetos da questão 2
    pontos = questao_dois()

    esfera = pontos['esfera']
    cilindro = pontos['cilindro']
    cubo = pontos['cubo']

    # Calcula o centro dos objetos
    centro_esfera = calcular_centro(esfera)
    centro_cilindro = calcular_centro(cilindro)
    centro_cubo = calcular_centro(cubo)

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

    ax.plot([0, u[0]], [0, u[1]], [0, u[2]], color='b', linestyle='dashed')
    ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color='r', linestyle='dashed')
    ax.plot([0, n[0]], [0, n[1]], [0, n[2]], color='g', linestyle='dashed')
    ax.plot([0, aux[0]], [0, aux[1]], [0, aux[2]], color='k', linestyle='dashed')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    mostrar_solidos_no_sistema_de_camera(ax, esfera, matriz_transformacao, 'b')
    mostrar_solidos_no_sistema_de_camera(ax, cubo, matriz_transformacao, 'g')
    mostrar_solidos_no_sistema_de_camera(ax, cilindro, matriz_transformacao, 'r')

    plt.show()


questao_tres()
