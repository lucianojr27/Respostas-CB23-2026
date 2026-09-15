class _No:
    """Classe auxiliar para representar o nó da lista encadeada."""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    """Pilha baseada em uma lista simplesmente encadeada."""
    
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """Insere o item no topo da pilha.
        Complexidade de Tempo: O(1)
        """
        novo_no = _No(item)
        novo_no.proximo = self._topo
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        """Remove e retorna o item do topo.
        Levanta IndexError se a pilha estiver vazia.
        Complexidade de Tempo: O(1)
        """
        if self.esta_vazia():
            raise IndexError("pop em pilha vazia")
        
        valor_removido = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor_removido

    def topo(self):
        """Retorna o item do topo sem removê-lo.
        Levanta IndexError se a pilha estiver vazia.
        Complexidade de Tempo: O(1)
        """
        if self.esta_vazia():
            raise IndexError("topo em pilha vazia")
        return self._topo.valor

    def esta_vazia(self):
        """Retorna True quando não há elementos armazenados.
        Complexidade de Tempo: O(1)
        """
        return self._tamanho == 0

    def __len__(self):
        """Retorna a quantidade de elementos armazenados.
        Complexidade de Tempo: O(1)
        """
        return self._tamanho

    def __repr__(self):
        """Representação textual legível, do topo para a base.
        Complexidade de Tempo: O(N)
        """
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(repr(atual.valor))
            atual = atual.proximo
        return f"PilhaEncadeada(Topo -> [{' -> '.join(elementos)}])"
