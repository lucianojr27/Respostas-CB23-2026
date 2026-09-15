import unittest
from P06_3483_pilha_encadeada import PilhaEncadeada
from P06_3483_fila_encadeada import FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):
    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_ordem_lifo(self):
        self.pilha.push(10)
        self.pilha.push(20)
        self.pilha.push(30)
        self.assertEqual(self.pilha.pop(), 30)
        self.assertEqual(self.pilha.pop(), 20)
        self.assertEqual(self.pilha.pop(), 10)

    def test_excecoes_pilha_vazia(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()
        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_tamanho(self):
        self.assertEqual(len(self.pilha), 0)
        self.pilha.push("A")
        self.assertEqual(len(self.pilha), 1)
        self.pilha.push("B")
        self.assertEqual(len(self.pilha), 2)
        self.pilha.pop()
        self.assertEqual(len(self.pilha), 1)

    def test_armazenamento_tipos_diferentes(self):
        self.pilha.push(None)
        self.pilha.push(True)
        self.pilha.push(10)
        self.assertEqual(self.pilha.pop(), 10)
        self.assertTrue(self.pilha.pop())
        self.assertIsNone(self.pilha.pop())

    def test_alternancia_operacoes(self):
        self.pilha.push(1)
        self.assertEqual(self.pilha.pop(), 1)
        self.pilha.push(2)
        self.assertEqual(self.pilha.topo(), 2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(len(self.pilha), 1)


class TestFilaEncadeada(unittest.TestCase):
    def setUp(self):
        self.fila = FilaEncadeada()

    def test_ordem_fifo(self):
        self.fila.enfileirar("A")
        self.fila.enfileirar("B")
        self.fila.enfileirar("C")
        self.assertEqual(self.fila.desenfileirar(), "A")
        self.assertEqual(self.fila.desenfileirar(), "B")
        self.assertEqual(self.fila.desenfileirar(), "C")

    def test_intercalacao_operacoes(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.frente(), 3)
        self.assertEqual(self.fila.desenfileirar(), 3)
        self.assertTrue(self.fila.esta_vazia())

    def test_esvaziar_e_voltar_a_usar(self):
        self.fila.enfileirar(10)
        self.fila.desenfileirar()
        self.assertTrue(self.fila.esta_vazia())
        
        self.fila.enfileirar(20)
        self.assertEqual(len(self.fila), 1)
        self.assertEqual(self.fila.frente(), 20)
        self.assertEqual(self.fila.desenfileirar(), 20)

    def test_excecoes_fila_vazia(self):
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()
        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_coerencia_tamanho(self):
        self.assertEqual(len(self.fila), 0)
        self.fila.enfileirar(100)
        self.fila.enfileirar(200)
        self.assertEqual(len(self.fila), 2)
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 1)
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 0)

if __name__ == "__main__":
    unittest.main()
