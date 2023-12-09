import numpy as np


# Função para gerar um cilindro
def cilindro(raio, num_fatias=10, num_divisoes=10):
    # Calcula a altura do cilindro
    altura = 2 * raio

    # Gera os ângulos theta para os vértices do círculo
    theta = np.linspace(0, 2 * np.pi, num_fatias)

    # Calcula as coordenadas x e y para o círculo inferior e superior
    x = raio * np.cos(theta)
    y = raio * np.sin(theta)

    # Calcula as coordenadas z para as divisões verticais do cilindro
    z = np.linspace(0, altura, num_divisoes)

    # Cria os pontos do círculo inferior e superior
    circulo_inferior = np.column_stack([x, y, np.full_like(x, z[0])])
    circulo_superior = np.column_stack([x, y, np.full_like(x, z[-1])])

    # Combina circulo inferior e superior
    vertices = np.concatenate([circulo_inferior, circulo_superior], axis=0)

    # Cria as divisões laterais
    for i in range(1, num_divisoes):
        z_atual = z[i]
        circulo_lateral = np.column_stack([raio * np.cos(theta), raio * np.sin(theta), np.full_like(x, z_atual)])
        vertices = np.concatenate([vertices, circulo_lateral], axis=0)

    # Conecta as arestas do círculo inferior e superior
    arestas = []
    for i in range(num_fatias):
        arestas.append([i, (i + 1) % num_fatias])
        arestas.append([i, i + num_fatias])
        arestas.append([i + num_fatias, (i + 1) % num_fatias + num_fatias])

        # Conecta as arestas laterais
        for j in range(1, num_divisoes):
            current_vertex = i + j * num_fatias
            next_vertex = (i + 1) % num_fatias + j * num_fatias
            arestas.append([current_vertex, next_vertex])

    # Adiciona o centro do círculo inferior e superior
    centro_inferior = [0, 0, z[0]]
    centro_superior = [0, 0, z[-1]]
    vertices = np.concatenate([vertices, [centro_inferior, centro_superior]], axis=0)

    # Conecta as arestas do centro aos pontos do círculo inferior e superior
    for i in range(num_fatias):
        arestas.append([i, vertices.shape[0] - 2])
        arestas.append([i + num_fatias, vertices.shape[0] - 1])

    return vertices, arestas
