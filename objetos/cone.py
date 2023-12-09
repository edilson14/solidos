import numpy as np


def cone(raio, num_fatias=10, num_divisoes=10):
    altura = 3 * raio
    # Gera os ângulos theta para os vértices do círculo
    theta = np.linspace(0, 2 * np.pi, num_fatias)

    # Calcula as coordenadas x e y para a base
    x = raio * np.cos(theta)
    y = raio * np.sin(theta)

    # Calcula as coordenadas z para as divisões verticais do cone
    z = np.linspace(0, altura, num_divisoes)

    # Cria os pontos da base
    base = np.column_stack([x, y, np.full_like(x, z[0])])

    # Multiplicadores dos raios de cada pedaço
    mult_raio_fatias = np.linspace(1, 0, num_divisoes)

    vertices = base

    # Cria as divisões laterais
    for i in range(1, num_divisoes):
        z_atual = z[i]
        raio_atual = raio * mult_raio_fatias[i]
        circulo_lateral = np.column_stack(
            [raio_atual * np.cos(theta), raio_atual * np.sin(theta), np.full_like(theta, z_atual)])
        vertices = np.concatenate([vertices, circulo_lateral], axis=0)

    # Conecta as arestas laterais
    arestas = []
    for i in range(num_fatias):
        arestas.append([i, (i + 1) % num_fatias])

        # Conecta as arestas da superfície lateral
        for j in range(1, num_divisoes):
            current_vertex = i + (j - 1) * num_fatias
            next_vertex = (i + 1) % num_fatias + (j - 1) * num_fatias
            arestas.append([current_vertex, next_vertex])

            next_vertex = i + j * num_fatias
            arestas.append([current_vertex, next_vertex])

    # Adiciona o centro da base
    centro_base = [0, 0, z[0]]
    vertices = np.concatenate([vertices, [centro_base]], axis=0)

    # Conecta as arestas do centro aos pontos da base
    for i in range(num_fatias):
        arestas.append([i, vertices.shape[0] - 1])

    return vertices, arestas