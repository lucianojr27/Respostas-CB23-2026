# Análise Teórica e Respostas - Aula 07

**Matrícula:** 3483  
**Disciplina:** CB23 - Estruturas de Dados e Algoritmos (2026)  
**Aula:** Aula 07 - Busca em Grafos e Labirintos (14/09/2026)  
**Título do Pull Request:** `07_3483`  
**Caminho do Diretório no Repositório:** `entregas/aula07/07_3483/`

---

## Questão 1: Implementação da Busca em Profundidade Iterativa (`dfs`)

### 1.1. Modificação da Estrutura de Controle (Recursão vs. Pilha Explícita)
No arquivo original `maze_builder.py`, a função `dfs(x, y)` utilizava recursão implícita, delegando o controle do estado e da navegação no labirinto para a **pilha de chamadas de função (call stack)** da própria linguagem Python. 

Para a Questão 1, a recursão foi removida e substituída por uma **versão iterativa puramente orientada a dados**, empregando uma pilha explícita (estrutura de dados `pilha = []` do Python).

### 1.2. Funcionamento do Algoritmo Iterativo de Geração
O algoritmo iterativo contido na função `generate_maze_iterative` opera da seguinte forma:
1. **Inicialização:** A grade lógica m x n é expandida para uma matriz (2m+1) x (2n+1) totalmente preenchida com paredes. A célula lógica (0, 0) — que no mapa expandido equivale às coordenadas (1, 1) — é aberta e empilhada em `pilha = [(0, 0)]`.
2. **Laço Principal (`while pilha`):**
   - **Consulta do Topo:** O algoritmo observa o elemento atual no topo da pilha (`x, y = pilha[-1]`) sem removê-lo.
   - **Exploração de Vizinhos:** Verifica-se quais das 4 direções cardeais (Norte, Sul, Leste, Oeste) possuem vizinhos na grade lógica que ainda estão não visitados (ou seja, cuja célula correspondente no mapa expandido é uma parede).
   - **Avanço (Empilhamento):** Caso existam vizinhos válidos não visitados, um deles é selecionado aleatoriamente via `random.choice`. A parede física entre a sala atual e a vizinha é removida, a sala vizinha é marcada como aberta e suas coordenadas são empilhadas em `pilha.append((nx, ny))`.
   - **Backtracking (Desempilhamento):** Se o nó atual não possuir nenhum vizinho válido não visitado (beco sem saída ou interseção cujos caminhos já foram explorados), o algoritmo realiza o *backtracking* desempilhando a posição atual (`pilha.pop()`).
3. **Término:** O processo encerra quando a pilha esvazia (`pilha` fica vazia), o que garante que todas as salas alcançáveis foram exploradas, gerando uma Árvore Geradora (Labirinto Perfeito).

---

## Questão 2: Resolução do Labirinto e Discussão Teórica (DFS vs. BFS)

### 2.1. Solução Implementada
Na função `encontrar_caminho_dfs`, foi adotada uma Busca em Profundidade (DFS) Iterativa com uma pilha explícita contendo tuplas no formato `(posicao_atual, caminho_acumulado)`. A busca parte da posição inicial (1, 1) e encerra imediatamente assim que o queijo (`cheese`) é localizado.

### 2.2. Discussão Teórica: Escolha entre DFS (Busca em Profundidade) e BFS (Busca em Largura)

#### A. Propriedade Topológica de Labirintos Perfeitos
O gerador `maze_builder.py` constrói o que a teoria dos grafos conceitua como um **Labirinto Perfeito**. Por definição:
- Um labirinto perfeito é uma **Árvore Geradora (Spanning Tree)** sobre a grade de salas.
- Em qualquer árvore, existe **exatamente UM único caminho simples** entre qualquer par de vértices do grafo.

#### B. Consequências Teóricas da Unicidade de Caminho
1. **Identidade de Caminho Encontrado:** 
   - Como não existem ciclos nem caminhos alternativos no labirinto perfeito, **tanto a Busca em Profundidade (DFS) quanto a Busca em Largura (BFS) obrigatoriamente encontrarão o exato mesmo caminho final** entre a entrada (1, 1) e o queijo.
   - A BFS é reconhecida por encontrar o caminho mais curto (menor número de arestas) em grafos genéricos não ponderados. Contudo, em uma árvore, como existe apenas um único caminho possível, o caminho mais curto é o próprio caminho único existente.
2. **Eficiência e Uso de Memória:**
   - **DFS (Pilha):** Mergulha profundamente em um ramo até atingir um objetivo ou beco sem saída. A quantidade de memória utilizada pela pilha da DFS é proporcional à profundidade do caminho atual, O(D), onde D é o comprimento do ramo. Para a resolução gráfica de labirintos, a DFS emula o comportamento físico intuitivo de um "agente" percorrendo o corredor.
   - **BFS (Fila):** Explora o grafo em "ondas de choque" concêntricas (nível a nível). O consumo de memória da BFS é proporcional à largura da fronteira de busca, O(W), armazenando todos os nós vizinhos do mesmo nível simultaneamente na fila.

#### C. Justificativa da Escolha da DFS Iterativa
Optou-se pela **DFS Iterativa** pelos seguintes motivos fundamentais:
1. **Consistência Arquitetural:** Mantém alinhamento com a Questão 1, utilizando o modelo conceitual de pilha explícita para ambos os problemas.
2. **Navegação Natural:** A DFS simula a caminhada sequencial de um explorador que avança por um corredor até ser forçado a voltar no primeiro cruzamento não esgotado.
3. **Desempenho em Grafos Acíclicos:** Como não há múltiplos caminhos concorrentes para o queijo, o overhead de manutenção da fila por níveis da BFS é desnecessário.

---

## 3. Análise de Complexidade de Tempo e Espaço

| Operação | Complexidade de Tempo (Pior Caso) | Complexidade de Espaço | Justificativa |
| :--- | :--- | :--- | :--- |
| **Geração do Labirinto (DFS Iterativo)** | **O(V + E) = O(m * n)** | **O(m * n)** | Cada uma das m * n salas é empilhada e desempilhada no máximo uma vez. Cada parede/aresta é checada um número constante de vezes. |
| **Busca do Caminho (DFS Iterativo)** | **O(V) = O(m * n)** | **O(m * n)** | No pior caso (quando o queijo está no último ramo visitado), todas as células acessíveis serão visitadas uma vez. O conjunto de visitados e a pilha ocupam espaço proporcional ao total de salas. |
| **Exibição do Labirinto com Caminho** | **O(m * n)** | **O(m * n)** | Uma varredura completa da matriz (2m+1) x (2n+1) é realizada para construir a representação textual do labirinto no terminal. |

