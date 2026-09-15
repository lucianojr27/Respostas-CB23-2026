from P06_3483_pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    """Fila construída exclusivamente utilizando duas pilhas encadeadas."""
    
    def __init__(self):
        self._pilha_entrada = PilhaEncadeada()
        self._pilha_saida = PilhaEncadeada()

    def enfileirar(self, item):
        """Insere o item no fim da fila.
        Complexidade de Tempo: O(1)
        """
        self._pilha_entrada.push(item)

    def _transferir_elementos(self):
        """Transfere os elementos da pilha de entrada para a pilha de saída, se necessário."""
        if self._pilha_saida.esta_vazia():
            while not self._pilha_entrada.esta_vazia():
                item = self._pilha_entrada.pop()
                self._pilha_saida.push(item)

    def desenfileirar(self):
        """Remove e retorna o item da frente da fila.
        Levanta IndexError se a fila estiver vazia.
        Complexidade de Tempo: O(1) amortizada (caso médio)
        """
        self._transferir_elementos()
        if self._pilha_saida.esta_vazia():
            raise IndexError("desenfileirar em fila vazia")
        return self._pilha_saida.pop()

    def frente(self):
        """Retorna o item da frente sem removê-lo.
        Levanta IndexError se a fila estiver vazia.
        Complexidade de Tempo: O(1) amortizada (caso médio)
        """
        self._transferir_elementos()
        if self._pilha_saida.esta_vazia():
            raise IndexError("frente em fila vazia")
        return self._pilha_saida.topo()

    def esta_vazia(self):
        """Retorna True quando não há elementos armazenados.
        Complexidade de Tempo: O(1)
        """
        return self._pilha_entrada.esta_vazia() and self._pilha_saida.esta_vazia()

    def __len__(self):
        """Retorna a quantidade de elementos da fila.
        Complexidade de Tempo: O(1)
        """
        return len(self._pilha_entrada) + len(self._pilha_saida)

    def __repr__(self):
        """Representação textual legível, da frente para o fim.
        Complexidade de Tempo: O(N)
        """
        return f"FilaEncadeada(Saída (Frente) = {self._pilha_saida!r}, Entrada (Fundo) = {self._pilha_entrada!r})"
