import numpy as np
import matplotlib.pyplot as plt

from q3 import questao_tres

# Defina os valores de near e far
near = 1
far = 10

# Defina a largura e altura da janela de projeção
largura = 1920
altura = 1080

# Defina a matriz de projeção em perspectiva
matriz_projecao = np.array([
    [near / (largura / 2), 0, 0, 0],
    [0, near / (altura / 2), 0, 0],
    [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
    [0, 0, -1, 0]
])


# Função para projetar pontos tridimensionais

def projetar_pontos_e_arestas(pontos, arestas, matriz_projecao, cor):
    # Aplicar a projeção aos pontos
    pontos_homogeneos = np.hstack((pontos, np.ones((pontos.shape[0], 1)))).T
    pontos_projetados_homogeneos = (matriz_projecao @ pontos_homogeneos).T
    pontos_projetados = pontos_projetados_homogeneos[:, :2] / pontos_projetados_homogeneos[:, 2, None]

    # Desenha as arestas projetadas
    for aresta in arestas:
        aresta_projetada = pontos_projetados[aresta]
        plt.plot(*zip(*aresta_projetada, aresta_projetada[0]), color=cor)

    return pontos_projetados


# Pega pontos dos objetos da questão 2
pontos = questao_tres()

pontos_esfera = pontos['pontos_esfera']
pontos_cilindro = pontos['pontos_cilindro']
pontos_cubo = pontos['pontos_cubo']

arestas_esfera = pontos['arestas_esfera']
arestas_cilindro = pontos['arestas_cilindro']
arestas_cubo = pontos['arestas_cubo']

# Aplique a projeção aos pontos dos sólidos
projetar_pontos_e_arestas(pontos_esfera, arestas_esfera, matriz_projecao, 'b')
projetar_pontos_e_arestas(pontos_cilindro, arestas_cilindro, matriz_projecao, 'r')
projetar_pontos_e_arestas(pontos_cubo, arestas_cubo, matriz_projecao, 'g')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Projeção em Perspectiva dos Sólidos')
plt.grid()
plt.show()
