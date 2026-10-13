def merge_sort_miniaturas(lista, sentido="crescente"):
    """
    Ordena uma lista de dicionários de miniaturas em ordem alfabética 
    baseado na chave 'nome', utilizando o algoritmo Merge Sort (O(N log N)).
    
    Args:
        lista (list): Lista de dicionários (produtos) a ser ordenada in-place.
        sentido (str): "crescente" para A-Z, "decrescente" para Z-A.
    """
    if len(lista) > 1:
        # 1. DIVISÃO: Encontra o meio e divide a lista em duas sublistas
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Chamadas recursivas para dividir até atingir sublistas de 1 elemento
        merge_sort_miniaturas(esquerda, sentido)
        merge_sort_miniaturas(direita, sentido)

        i = j = k = 0

        # 2. CONQUISTA (Mesclagem): Combina as sublistas em ordem
        while i < len(esquerda) and j < len(direita):
            # O .lower() garante ordenação correta independente de maiúsculas/minúsculas
            nome_esq = esquerda[i]['nome'].lower()
            nome_dir = direita[j]['nome'].lower()
            
            # Define a lógica de comparação com base no sentido escolhido
            if sentido == "crescente":
                condicao = nome_esq <= nome_dir
            else:
                condicao = nome_esq >= nome_dir

            if condicao:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # 3. Coleta elementos que sobraram na sublista esquerda
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Coleta elementos que sobraram na sublista direita
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1