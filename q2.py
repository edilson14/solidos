import  matplotlib.pyplot as plt
import numpy as np

from objetos.cone import cone
from objetos.cilindro import cilindro
from objetos.esfera import criar_esfera
from objetos.cubo import cubo
from objetos.tronco import tronco
from objetos.toroide import toroide



fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.set_title('Coordenadas do Mundo')
    # Define os limites do gráfico
limites = [-10, 10]

    # Desenha as linhas que dividem o espaço 3D em octantes para facilitar a identificação dos solidos em seus respectivos octantes
for s in [-1, 1]:
    ax.plot([0, 0], [0, 0], [s * limites[0], s * limites[1]], color='k', linestyle='--', linewidth=1)
    ax.plot([0, 0], [s * limites[0], s * limites[1]], [0, 0], color='k', linestyle='--', linewidth=1)
    ax.plot([s * limites[0], s * limites[1]], [0, 0], [0, 0], color='k', linestyle='--', linewidth=1)
    # Legenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# matriz de translacao em coordenadas homogeneas
def matriz_translacao(tx,ty,tz):
    return np.array([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]])

def matriz_escalonamento(x,y,z):
    return np.array([[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]])



escala= matriz_escalonamento(1/2,0.5,0.5)
def plots():
    # Esfera
    raio_esfera = 3
    vertices_esfera, arestas_esfera = criar_esfera(raio_esfera, 10)
    translacao_esfera = matriz_translacao(raio_esfera * 3, raio_esfera * 4, raio_esfera * 3)
    # escala = matriz_escalonamento(0.5, 0.5, 0.5)
    for aresta in arestas_esfera:
        vertice_homo = np.concatenate(
            [np.array(vertices_esfera[aresta]), np.ones((np.array(vertices_esfera[aresta]).shape[0], 1))],
            axis=-1)
        vertice_translado = (translacao_esfera @ vertice_homo.T).T
        vertice_escalado = (escala @ vertice_translado.T).T
        vertice_escalado = vertice_escalado[:, :3]  # remover a ultima coluna por causa da coordenadas homogenias

        ax.plot3D(*zip(*vertice_escalado), color='blue')

    # Cilindro
    raio = 4
    vertices, arestas = cilindro(raio=raio)
    translacao_cilindro = matriz_translacao(raio +1,raio,raio )

    for aresta in arestas:
        vertice_homo = np.concatenate([np.array(vertices[aresta]),np.ones((np.array(vertices[aresta]).shape[0],1))],axis=-1)
        vertice_translado = (translacao_cilindro @ vertice_homo.T).T
        vertice_escalado = (escala @ vertice_translado.T).T
        vertice_escalado = vertice_escalado[:,:3] # remover a ultima coluna por causa da coordenadas homogenias

        ax.plot3D(*zip(*vertice_escalado), color='red')

    #cubo
    tamanho_aresta = 3
    vertices_cubos , arestas_cubos = cubo(tamanho_aresta)
    translacao_cubo = matriz_translacao(tamanho_aresta +2,1,0)
    for aresta in arestas_cubos:
        vertice_homo = np.concatenate(
            [np.array(vertices_cubos[aresta]), np.ones((np.array(vertices_cubos[aresta]).shape[0], 1))],
            axis=-1)
        vertice_translado = (translacao_cubo @ vertice_homo.T).T
        vertice_translado = vertice_translado[:,:3] # remover a ultima coluna por causa da coordenadas homogenias


        ax.plot3D(*zip(*vertice_translado), color='green')

    #Cone
    raio_base = 6
    vertices_cone, aresta_cone = cone(raio_base)
    escalonamento_cone = matriz_escalonamento(0.5,0.5,0.5)
    translacao_cone = matriz_translacao(-5,10,0)
    for aresta in aresta_cone:
        vertices_homo = np.concatenate(
            [np.array(vertices_cone[aresta]),np.ones((np.array(vertices_cone[aresta]).shape[0],1))]
            ,axis=-1
        )
        vertice_escalonado = (escalonamento_cone @ vertices_homo.T).T
        vertice_translado = (translacao_cone @ vertice_escalonado.T).T
        vertice_translado = vertice_translado[:,:3]


        ax.plot3D(*zip(*vertice_translado),color="black")

    #tronco de piramide
    tamanho_base = 8
    tamanho_topo = 4
    altura = 5
    vertices_tronco, arestas_tronco = tronco(tamanho_aresta_base=tamanho_base,tamanho_aresta_topo=tamanho_topo,altura=altura)
    translacao_tronco = matriz_translacao(-5,5,0)
    escalonamento_tronco = matriz_escalonamento(1,0.6,1)
    for aresta in arestas_tronco:
        vertices_homo = np.concatenate(
            [np.array(vertices_tronco[aresta]),np.ones((np.array(vertices_tronco[aresta]).shape[0],1))],
            axis=-1
        )
        vertices_ecalonado  = (translacao_tronco @ vertices_homo.T).T
        vertice_final = (escalonamento_tronco @ vertices_ecalonado.T).T
        vertice_final = vertice_final[:,:3]

        ax.plot(*zip(*vertice_final),color="yellow")


    #toroide

    Raio = 2
    raio = 1
    vertices_toroide, arestas_toroide = toroide(r_raio=raio,R_raio=Raio,circunferencias_intermediarias=10)
    translacao_tronco = matriz_translacao(-5,5,10)
    escalonamento_tronco = matriz_escalonamento(1,0.6,1)
    for aresta in arestas_toroide:
        vertices_homo = np.concatenate(
            [np.array(vertices_toroide[aresta]),np.ones((np.array(vertices_toroide[aresta]).shape[0],1))],
            axis=-1
        )
        vertices_ecalonado  = (translacao_tronco @ vertices_homo.T).T
        vertice_final = (escalonamento_tronco @ vertices_ecalonado.T).T
        vertice_final = vertice_final[:,:3]

        ax.plot(*zip(*vertice_final),color="grey")



    plt.grid()
    plt.show()

plots()