def insertion_sort_miniaturas(lista, sentido="menor"):
    """
    Ordena a lista de miniaturas de carrinhos por preço.
    sentido="menor" -> Ordem Crescente (Menor para o Maior)
    sentido="maior" -> Ordem Decrescente (Maior para o Menor)
    """
    n = len(lista)
    
    for i in range(1, n):
        carrinho_atual = lista[i]
        preco_atual = carrinho_atual['preco']
        
        j = i - 1
        
        # A mágica acontece aqui: criamos uma condição flexível
        if sentido == "menor":
            # Condição clássica: empurra os mais caros para a direita
            deve_deslocar = lambda preco_lista: preco_lista > preco_atual
        else:
            # Condição inversa: empurra os mais baratos para a direita
            deve_deslocar = lambda preco_lista: preco_lista < preco_atual

        # Executa o deslocamento bruto baseado na regra escolhida
        while j >= 0 and deve_deslocar(lista[j]['preco']):
            lista[j + 1] = lista[j]
            j -= 1
            
        lista[j + 1] = carrinho_atual