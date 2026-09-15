# Análise de Complexidade - Fila Encadeada

## Justificativa para Complexidade O(1) Amortizada no método `desenfileirar()`

Para analisar a complexidade do método `desenfileirar`, precisamos olhar para o ciclo de vida de um elemento dentro da nossa estrutura baseada em duas pilhas (uma pilha de entrada e uma pilha de saída).

É verdade que o método `desenfileirar()` pode atingir a complexidade de **O(N)** no pior caso isolado. Isso ocorre quando a `pilha_saida` está vazia e o algoritmo precisa transferir todos os N elementos armazenados na `pilha_entrada` para a `pilha_saida` antes de retornar o item da frente.

No entanto, a complexidade **O(1) amortizada** garante que o custo médio por operação ao longo do tempo se manterá constante. Podemos justificar isso considerando o custo total pago por elemento:

1. Quando chamamos `enfileirar(item)`, o item é inserido na `pilha_entrada` (Custo: **O(1)**).
2. Durante a transferência acionada pelo `desenfileirar()`, este elemento é removido da `pilha_entrada` (Custo: **O(1)**) e imediatamente empilhado na `pilha_saida` (Custo: **O(1)**).
3. Mais tarde, quando o elemento atingir a frente da fila e for definitivamente removido via `desenfileirar()`, ele sofrerá apenas mais um pop da `pilha_saida` (Custo: **O(1)**).

Ou seja, **todo e qualquer elemento sofre exatamente 4 operações constantes (O(1)) durante toda a sua existência na Fila** (um `push` de entrada, um `pop` na transferência, um `push` de saída e um `pop` final). 

Como um elemento nunca retorna para a pilha de entrada após ser transferido para a pilha de saída, as transferências caras de O(N) só ocorrem de forma esparsa. O "trabalho pesado" do O(N) já foi pré-pago em "parcelas" de O(1) no momento de cada enfileiramento. Distribuindo esse custo total de transferência ao longo de todas as operações prévias, concluímos que o custo médio (amortizado) por operação no `desenfileirar()` se comporta como **O(1)** (constante).
