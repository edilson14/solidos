import numpy as np
from matplotlib import pyplot as plt

from q2 import questao_dois

origem_mundo = np.array([0, 0, 0, 1])


def calcular_centro(pontos_transformados):
    # Calcule a média ao longo do eixo 0 para obter as coordenadas médias
    centro = np.mean(pontos_transformados, axis=0)
    return centro


def mostrar_solidos_no_sistema_de_camera(ax, pontos_solido, arestas_solido, matriz_transformacao, cor):
    # Transforma os pontos usando a matriz de transformação
    pontos_solidos_homogeneos = np.hstack((pontos_solido, np.ones((pontos_solido.shape[0], 1)))).T
    pontos_transformados = (matriz_transformacao @ pontos_solidos_homogeneos).T

    pontos_transformados = pontos_transformados[:, :3]
    print(np.linalg.norm(pontos_transformados[0]))
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

    at = np.array([0.0, 0.0, 0.0])  # Ponto para onde a câmera está olhando
    at += np.array(centro_esfera)
    at += np.array(centro_cilindro)
    at += np.array(centro_cubo)
    at /= 3.0


    eye = np.array([5, -5, 5])

    print(np.linalg.norm(pontos_cubo[0] - eye))


    n = (at - eye)
    norma_n = np.sqrt(sum(n ** 2))

    # Vetor auxiliar
    up = np.array([0, 1, 0])


    v = up - (np.dot(up, n) / norma_n **2)*n # projecao de up em n em plano ortogonal para obter v
    u = np.cross(v, n)

    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    n /= np.linalg.norm(n)

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
    # matriz_transformacao = np.dot(R, T)
    matriz_transformacao = (R@T)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #origem mundo
    origem_transformada = np.dot(matriz_transformacao, origem_mundo)
    origem_transformada = origem_transformada[:3]
    ax.scatter(origem_transformada[0], origem_transformada[1], origem_transformada[2], color='cyan', s=100)



    ax.plot([0, u[0] * 3], [0, u[1] * 3], [0, u[2] * 3], color='b', linestyle='dashed')
    ax.plot([0, v[0] * 3], [0, v[1] * 3], [0, v[2] * 3], color='r', linestyle='dashed')
    ax.plot([0, n[0] * -3], [0, n[1] * -3], [0, n[2] * -3], color='g', linestyle='dashed')
    ax.plot([0, up[0] * 3], [0, up[1] * 3], [0, up[2] * 3], color='k', linestyle='dashed')


    # Adicionando descrições para cada linha
    ax.text(u[0] * 3, u[1] * 3, u[2] * 3, 'vetor u', color='b')
    ax.text(v[0] * 3, v[1] * 3, v[2] * 3, 'vetor v', color='r')
    ax.text(n[0] * -3, n[1] * -3, n[2] * -3, 'vetor n', color='g')
    ax.text(up[0] * 3, up[1] * 3, up[2] * 3, 'vetor up', color='k')


    mostrar_solidos_no_sistema_de_camera(ax, pontos_esfera, arestas_esfera, matriz_transformacao, 'b')
    mostrar_solidos_no_sistema_de_camera(ax, pontos_cilindro, arestas_cilindro, matriz_transformacao, 'r')
    mostrar_solidos_no_sistema_de_camera(ax, pontos_cubo, arestas_cubo, matriz_transformacao, 'g')



    plt.show()


questao_tres()
