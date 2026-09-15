# Análise de Complexidade e Funcionalidades - Aula 06

## Questão 1: Tabela de Operações da Pilha Encadeada (`PilhaEncadeada`)

A estrutura `PilhaEncadeada` foi implementada utilizando o conceito de Lista Simplesmente Encadeada (Linked List), onde as inserções e remoções ocorrem exclusivamente no topo.

| Método | Funcionalidade | Complexidade de Tempo (Pior Caso) | Justificativa da Complexidade |
| :--- | :--- | :--- | :--- |
| `push(item)` | Insere um novo elemento no topo da pilha. | **O(1)** | A inserção ocorre diretamente na cabeça (topo) da lista encadeada. Cria-se um novo nó que aponta para o antigo topo, e o ponteiro do topo é atualizado. Não há necessidade de percorrer a estrutura. |
| `pop()` | Remove e retorna o elemento que está no topo da pilha. Levanta erro se vazia. | **O(1)** | A remoção também ocorre na cabeça da lista. O ponteiro do topo é simplesmente redirecionado para o próximo nó (`self._topo.proximo`). Nenhuma iteração é necessária. |
| `topo()` | Retorna o valor do elemento no topo da pilha sem removê-lo. Levanta erro se vazia. | **O(1)** | O método apenas acessa o atributo `valor` do nó apontado pelo ponteiro `self._topo`. Acesso direto. |
| `esta_vazia()`| Verifica se a pilha não contém elementos (retorna `True` ou `False`). | **O(1)** | A verificação é feita checando se a variável de controle de tamanho (`self._tamanho`) é igual a zero, ou se o topo é `None`. Uma simples operação de comparação. |
| `__len__()` | Retorna a quantidade atual de elementos armazenados na pilha. | **O(1)** | O tamanho é mantido atualizado em uma variável (ex: `self._tamanho`) que é incrementada no `push` e decrementada no `pop`. Acessar esse valor inteiro tem custo constante. |
| `__repr__()` | Retorna uma representação textual e legível da pilha (do topo para a base). | **O(N)** | O método precisa obrigatoriamente iterar por todos os $N$ nós da pilha, a partir do topo até o fim da cadeia (quando `proximo` é `None`), para formatar a string de saída. |

---

## Questão 2: Tabela de Operações da Fila Encadeada (`FilaEncadeada`)

A `FilaEncadeada` foi construída utilizando **apenas duas instâncias de `PilhaEncadeada`** (`pilha_entrada` e `pilha_saida`), sem utilizar listas nativas do Python para armazenamento direto.

| Método | Funcionalidade | Complexidade de Tempo | Justificativa da Complexidade |
| :--- | :--- | :--- | :--- |
| `enfileirar(item)` | Insere um novo elemento no final da fila. | **O(1)** | O método realiza apenas um `push` na `pilha_entrada`. Como vimos na tabela anterior, o `push` da Pilha tem complexidade garantida de O(1). |
| `desenfileirar()` | Remove e retorna o elemento da frente da fila. Levanta erro se vazia. | **O(1)** amortizada | Caso a `pilha_saida` possua elementos, basta um `pop()` nela, que é O(1). Se a `pilha_saida` estiver vazia, ocorre a transferência de *todos* os $N$ elementos da `pilha_entrada`, o que leva O(N) pontualmente. Porém, como esse custo é diluído ao longo das operações seguintes, o tempo médio pago por elemento se mantém O(1) (ver justificativa detalhada abaixo). |
| `frente()` | Retorna o valor do elemento da frente da fila sem removê-lo. Levanta erro se vazia. | **O(1)** amortizada | Mesma lógica do `desenfileirar`. Exige a transferência (O(N)) caso a `pilha_saida` esteja vazia, mas na imensa maioria das vezes apenas executa o método `topo()` da pilha, que é O(1). |
| `esta_vazia()` | Verifica se a fila não contém elementos (retorna `True` ou `False`). | **O(1)** | Basta verificar se ambas as pilhas internas (`pilha_entrada` e `pilha_saida`) estão vazias. Como a verificação de vazio das pilhas é O(1), a conjunção das duas também é. |
| `__len__()` | Retorna a quantidade de elementos armazenados na fila. | **O(1)** | É calculado somando o tamanho (`len()`) da `pilha_entrada` com o da `pilha_saida`. Como ambas consultam um atributo interno em tempo constante, a soma das duas resulta em O(1). |
| `__repr__()` | Retorna a representação textual legível da fila (frente para o fundo). | **O(N)** | A operação invoca o `__repr__` das duas pilhas subjacentes. Juntas, elas contêm $N$ elementos no total, portanto os nós serão percorridos uma única vez resultando em custo linear em relação ao tamanho total da fila. |

---

## Justificativa Detalhada: Complexidade O(1) Amortizada no método `desenfileirar()` e `frente()`

É verdade que o método `desenfileirar()` pode atingir a complexidade de **O(N)** no pior caso isolado. Isso ocorre quando a `pilha_saida` está vazia e o algoritmo precisa transferir todos os $N$ elementos armazenados na `pilha_entrada` para a `pilha_saida` antes de retornar o item da frente.

No entanto, a complexidade **O(1) amortizada** garante que o custo médio por operação ao longo do tempo se manterá constante. Podemos justificar isso analisando o ciclo de vida e o custo total pago por cada elemento individualmente:

1. Quando chamamos `enfileirar(item)`, o item é inserido na `pilha_entrada` (Custo: **O(1)**).
2. Durante a transferência acionada pelo `desenfileirar()`, este elemento é removido da `pilha_entrada` (Custo: **O(1)**) e imediatamente empilhado na `pilha_saida` (Custo: **O(1)**).
3. Mais tarde, quando o elemento atingir a frente da fila e for definitivamente removido via `desenfileirar()`, ele sofrerá apenas mais um pop da `pilha_saida` (Custo: **O(1)**).

Ou seja, **todo e qualquer elemento sofre no máximo 4 operações de custo constante (O(1)) durante toda a sua existência na Fila** (um `push` de entrada, um `pop` na transferência, um `push` de saída e um `pop` final). 

Como um elemento nunca retorna para a pilha de entrada após ser transferido para a pilha de saída, as transferências "caras" de O(N) só ocorrem de forma esparsa e esporádica. O "trabalho pesado" de transferir tudo já foi pré-pago em pequenas parcelas no momento de cada enfileiramento. Distribuindo esse custo total ao longo de todas as operações prévias, concluímos matematicamente que o custo médio (amortizado) por operação se comporta estritamente como **O(1)**.
