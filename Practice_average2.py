#entradas
quantidade_minima = int(input("Informe a quantidade minima: "))
quantidade_maxima = int(input("Informe a quantidade maxima: "))
#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
#saida
print("O estoque medio e {0}". format(estoque_medio))