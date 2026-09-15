# -*- coding: utf-8 -*-
"""
P07_3483_labirinto.py
---------------------
Matrícula: 3483
Aula 07 - Busca em Grafos e Labirintos (DFS Iterativo & Resolução)

Este módulo atende às questões 1 e 2 da Aula 07:
1. Implementação de uma versão iterativa do algoritmo DFS (Busca em Profundidade)
   para a geração procedural do labirinto perfeito (baseado no maze_builder.py).
2. Resolução iterativa do labirinto (encontrar o caminho da posição (1, 1) até o queijo)
   e exibição visual do caminho encontrado.
"""

import random
import sys

# Importa o maze_builder original se disponível na mesma pasta, ou fornece fallback completo
try:
    import maze_builder
except ImportError:
    maze_builder = None


# ==============================================================================
# QUESTÃO 1: Geração de Labirinto com DFS Iterativo
# ==============================================================================

def generate_maze_iterative(m, n, room=0, wall=1, cheese='.'):
    """
    Gera um labirinto perfeito de dimensão (2m+1) x (2n+1) utilizando DFS Iterativo
    com uma pilha explícita (substituindo a pilha de execução recursiva).

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int ou str
        Representação das passagens abertas.
    wall : int ou str
        Representação das paredes.
    cheese : str
        Símbolo do objetivo (queijo).

    Returns
    -------
    list[list]
        Matriz bidimensional representando o labirinto.
    """
    # Inicializa a matriz com paredes
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Direções cardeais de movimentação na grade lógica: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # --- DFS ITERATIVO USANDO PILHA EXPLÍCITA ---
    # Célula inicial na grade lógica: (0, 0), correspondente a (1, 1) no mapa expandido
    start_x, start_y = 0, 0
    maze[2 * start_x + 1][2 * start_y + 1] = room
    
    # A pilha armazena as coordenadas da grade lógica (x, y)
    pilha = [(start_x, start_y)]

    while pilha:
        x, y = pilha[-1]  # Espia o topo da pilha (sem remover para permitir backtracking)

        # Encontra vizinhos não visitados
        vizinhos_nao_visitados = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Verifica se a sala vizinha está dentro dos limites e ainda é parede (não visitada)
            if 0 <= nx < m and 0 <= ny < n:
                if maze[2 * nx + 1][2 * ny + 1] == wall:
                    vizinhos_nao_visitados.append((dx, dy, nx, ny))

        if vizinhos_nao_visitados:
            # Escolhe aleatoriamente um vizinho válido para avançar
            dx, dy, nx, ny = random.choice(vizinhos_nao_visitados)

            # Derruba a parede entre a sala atual e o vizinho
            maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
            # Marca o vizinho como sala (visitado)
            maze[2 * nx + 1][2 * ny + 1] = room

            # Empilha o novo nó (avança no caminho)
            pilha.append((nx, ny))
        else:
            # Não há vizinhos não visitados: realiza backtracking desempilhando
            pilha.pop()

    # Posiciona o queijo (cheese) aleatoriamente em uma sala livre (diferente da origem (1, 1))
    while True:
        i = random.randint(0, 2 * m)
        j = random.randint(0, 2 * n)
        if maze[i][j] == room and (i, j) != (1, 1):
            maze[i][j] = cheese
            break

    return maze


# ==============================================================================
# QUESTÃO 2: Busca Iterativa do Caminho (da Origem (1, 1) até o Queijo)
# ==============================================================================

def encontrar_caminho_dfs(maze, inicio=(1, 1), cheese='.'):
    """
    Encontra o caminho do ponto de início (1, 1) até a posição do queijo
    utilizando Busca em Profundidade (DFS) Iterativa com Pilha Explícita.

    Parameters
    ----------
    maze : list[list]
        Matriz do labirinto.
    inicio : tuple(int, int)
        Coordenada de início (linha, coluna). Padrão: (1, 1).
    cheese : str ou int
        Símbolo ou valor correspondente ao queijo.

    Returns
    -------
    list[tuple(int, int)] ou None
        Lista de coordenadas (linha, coluna) representando o caminho completo,
        ou None se não houver caminho.
    """
    linhas = len(maze)
    colunas = len(maze[0])

    # Pilha armazena tuplas: (posição_atual, caminho_percorrido_ate_aqui)
    pilha = [(inicio, [inicio])]
    visitados = {inicio}

    # Ordem de exploração dos 4 vizinhos (Cima, Baixo, Esquerda, Direita)
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pilha:
        pos_atual, caminho = pilha.pop()
        r, c = pos_atual

        # Se encontramos o queijo, retornamos o caminho acumulado
        if maze[r][c] == cheese:
            return caminho

        for dr, dc in movimentos:
            nr, nc = r + dr, c + dc
            if 0 <= nr < linhas and 0 <= nc < colunas:
                # É um caminho livre (não é parede) e ainda não foi visitado
                if maze[nr][nc] != 1 and (nr, nc) not in visitados:
                    visitados.add((nr, nc))
                    pilha.append(((nr, nc), caminho + [(nr, nc)]))

    return None


def exibir_labirinto_com_caminho(maze, caminho, wall=1, cheese='.'):
    """
    Exibe o labirinto no terminal formatando o caminho percorrido com o caractere '*'.

    Parameters
    ----------
    maze : list[list]
        Matriz original do labirinto.
    caminho : list[tuple(int, int)]
        Lista de coordenadas do caminho encontrado.
    wall : int ou str
        Símbolo de parede.
    cheese : str ou int
        Símbolo do objetivo.
    """
    # Cria cópia para não alterar a matriz original
    grid_copia = [row[:] for row in maze]
    set_caminho = set(caminho) if caminho else set()

    print("\n" + "=" * 50)
    print(" LABIRINTO RESOLVIDO (Caminho marcado com '*')")
    print("=" * 50)

    for r in range(len(grid_copia)):
        linha_str = []
        for c in range(len(grid_copia[0])):
            val = grid_copia[r][c]
            pos = (r, c)
            
            if pos == (1, 1):
                linha_str.append("S")  # S = Start (Início)
            elif val == cheese:
                linha_str.append("Q")  # Q = Queijo (Objetivo)
            elif pos in set_caminho:
                linha_str.append("*")  # * = Caminho percorrido
            elif val == wall:
                linha_str.append("█")  # Parede
            else:
                linha_str.append(" ")  # Espaço livre
        print(" ".join(linha_str))
    print("=" * 50)


# ==============================================================================
# EXECUÇÃO PRINCIPAL
# ==============================================================================

if __name__ == '__main__':
    # Tamanho da grade lógica (10x14 gera uma matriz 21x29 no mapa expandido)
    m, n = 10, 14
    
    # Fixa a semente aleatória para reprodutibilidade nos testes
    random.seed()

    print("=== AULA 07: GERANDO LABIRINTO COM DFS ITERATIVO (Questão 1) ===")
    maze = generate_maze_iterative(m, n, room=0, wall=1, cheese='.')
    print(f"Labirinto {2*m+1}x{2*n+1} gerado com sucesso!")

    print("\n=== ENCONTRANDO O CAMINHO DA POSIÇÃO (1, 1) ATÉ O QUEIJO (Questão 2) ===")
    caminho = encontrar_caminho_dfs(maze, inicio=(1, 1), cheese='.')

    if caminho:
        print(f"✓ Queijo encontrado! Tamanho do caminho: {len(caminho)} posições.")
        exibir_labirinto_com_caminho(maze, caminho, wall=1, cheese='.')
    else:
        print("✗ Caminho não encontrado!")
