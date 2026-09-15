import random
import time
import sys

# Aumenta o limite de recursão para o Quick Sort suportar o pior caso
sys.setrecursionlimit(10000)

try:
    # Importando estritamente o que existe no arquivo AP_03_ordenacao.py
    from AP_03_ordenacao import selection_sort, divide_and_conquer_sort, quick_sort
except ImportError:
    print("Erro: 'AP_03_ordenacao.py' não encontrado. Certifique-se de colocá-lo no mesmo diretório.")
    sys.exit(1)

def gerar_caso_medio(n):
    """Gera uma lista com números inteiros aleatórios (Caso Médio)."""
    return [random.randint(0, 10000) for _ in range(n)]

def gerar_pior_caso(n):
    """Gera uma lista em ordem decrescente (Pior Caso para a maioria dos algoritmos)."""
    return list(range(n, 0, -1))

def benchmark_algoritmo(algoritmo, n, cenario, k=50):
    """
    Executa o benchmark de um algoritmo específico para um dado N e cenário.
    Repete K vezes e retorna a média do tempo.
    """
    tempos = []
    
    for _ in range(k):
        # 1. Preparar os dados de entrada
        if cenario == "Médio":
            lista = gerar_caso_medio(n)
        elif cenario == "Pior":
            lista = gerar_pior_caso(n)
            
        # 2. Medir o tempo de execução
        inicio = time.perf_counter()
        algoritmo(lista)
        fim = time.perf_counter()
        
        # 3. Guardar o tempo da execução atual
        tempos.append(fim - inicio)
        
    # Retorna a média aritmética dos tempos coletados
    return sum(tempos) / k

def main():
    # Tamanhos de N a serem testados
    # Reduzi K e os maiores Ns para o teste não demorar uma eternidade no Selection Sort
    tamanhos_n = [100, 500, 1000]
    cenarios = ["Médio", "Pior"]
    repeticoes_k = 20

    # Lista mapeando o nome legível com a função exata do seu arquivo
    algoritmos = [
        ("Selection Sort", selection_sort),
        ("Merge Sort", divide_and_conquer_sort),
        ("Quick Sort", quick_sort)
    ]

    print("=" * 70)
    print(" RELATÓRIO DE BENCHMARKING DE ALGORITMOS DE ORDENAÇÃO")
    print(f" (Repetições por teste: K = {repeticoes_k})")
    print("=" * 70)
    
    # Cabeçalho da tabela
    print(f"{'Algoritmo':<18} | {'N':<6} | {'Cenário':<10} | {'Tempo Médio (s)':<15}")
    print("-" * 70)

    for nome, funcao in algoritmos:
        for n in tamanhos_n:
            for cenario in cenarios:
                try:
                    tempo_medio = benchmark_algoritmo(funcao, n, cenario, k=repeticoes_k)
                    print(f"{nome:<18} | {n:<6} | {cenario:<10} | {tempo_medio:.6f}")
                except RecursionError:
                    print(f"{nome:<18} | {n:<6} | {cenario:<10} | Erro: Stack Overflow")
                except Exception as e:
                    print(f"{nome:<18} | {n:<6} | {cenario:<10} | Erro: {e}")
        print("-" * 70)

if __name__ == '__main__':
    main()