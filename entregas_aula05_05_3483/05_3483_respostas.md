# Respostas - Aula 5 (Orientação a Objetos)

## 1. Relações de Herança
Analisando as classes, podemos organizá-las na seguinte hierarquia de herança:

*   **Hierarquia de Pessoas/Funcionários:**
    *   **Classe Base:** `Pessoa`
    *   **Subclasse:** `Funcionário` (Herda `nome` e `idade` de Pessoa).
    *   **Subclasses de Funcionário:** `Garçom`, `Chefe de cozinha` e `Gerente`. (Estas três herdam `salario` e `carga_horaria` de Funcionário, além de `nome` e `idade` de Pessoa).

*   **Hierarquia de Comidas:**
    *   **Classe Base:** `Iguaria (comida)`
    *   **Subclasses:** `Pizza` e `Bolo`. (Ambas herdam `nome` e `preco` de Iguaria).

*   **Hierarquia de Estabelecimentos:**
    *   **Classe Base:** `Restaurante`
    *   **Subclasse:** `Pizzaria`. (Herda `nome`, `endereco` e `telefone` de Restaurante).

## 2. Relação entre Restaurante e Iguaria
A relação entre `Restaurante` e `Iguaria` seria melhor modelada como uma **Agregação**. Um restaurante possui iguarias (como parte de seu menu), mas as iguarias podem existir conceitualmente independentes do restaurante.

*   **Implementação:** Para implementar isso, eu adicionaria um novo atributo na classe `Restaurante` chamado `cardapio`.
*   **Tipagem:** O atributo `cardapio` seria uma lista de instâncias da classe Iguaria (ex: `cardapio: List[Iguaria]`). Alternativamente, poderia ser criada uma nova classe chamada `Cardapio` que encapsularia essa lista, e o `Restaurante` teria uma instância de `Cardapio`.

## 3. Tipagem dos Argumentos
*   **`argumento1` (método `anotar_pedido` em Garçom):**
    *   **Tipo sugerido:** Uma lista de instâncias da classe `Iguaria` (ex: `List[Iguaria]`) ou uma nova classe `Pedido` que contenha as iguarias escolhidas e o número da mesa.
    *   **Justificativa:** O garçom anota itens do menu. Fazer referência direta aos objetos `Iguaria` garante que o pedido contenha os preços e nomes corretos já cadastrados.
*   **`argumento2` (método `preparar` em Chefe de cozinha):**
    *   **Tipo sugerido:** Uma instância da classe `Iguaria` ou da classe sugerida `Pedido`.
    *   **Justificativa:** O chefe precisa saber exatamente qual prato (objeto Iguaria) preparar. Se for um `Pedido`, ele terá acesso a toda a lista de iguarias daquela requisição.
*   **`argumento3` (método `demitir` em Gerente):**
    *   **Tipo sugerido:** Uma instância da classe `Funcionário`.
    *   **Justificativa:** O gerente demite uma pessoa específica da equipe. Passar o objeto `Funcionário` permite que o método altere o status do funcionário no sistema (ex: removê-lo da lista do restaurante ou inativar seu contrato).
