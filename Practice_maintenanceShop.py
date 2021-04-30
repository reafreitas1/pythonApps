#variaveis
quantidade = 0
necessita_de_esfera = 0
necessita_de_limpeza = 0
necessita_troca_pecas = 0
quebrado_inutilizado = 0

#Entrada
identificacao = int(input("Numero de identificacao do mouse: "))
#Entrada/Processamento
while identificacao != 0:
    print("Digite 1 - Necessita de esfera")
    print("Digite 2 - Necessita de limpeza")
    print("Digite 3 - Necessita de troca de pecas")
    print("Digite 4 - Quebrado ou inutilizado")
    #Entrada
    defeito = int(input("Informe o defeito: "))
    #Processamento
    if defeito == 1:
        necessita_de_esfera = necessita_de_esfera + 1
    elif defeito == 2:
        necessita_de_limpeza = necessita_de_limpeza + 1
    elif defeito == 3:
        necessita_troca_pecas = necessita_troca_pecas + 1
    elif defeito == 4:
        quebrado_inutilizado = quebrado_inutilizado + 1
    elif defeito > 4:
        print("Atencao: Defeito inexistente!")
    quantidade = quantidade + 1
    identificacao = int(input("Numero de identificacao do mouse: "))
perc1 = necessita_de_esfera / quantidade * 100.0
perc2 = necessita_de_limpeza / quantidade * 100.0
perc3 = necessita_troca_pecas / quantidade * 100.0
perc4 = quebrado_inutilizado / quantidade * 100.0
#Saida
print("QUANTIDADE DE MOUSES: {0}.". format(quantidade))
print("Situacao                        Quantidade   Percentual")
print("1 - Necessita de esfera             {0}        {1:.2f}%".format(necessita_de_esfera, perc1))
print("2 - Necessita de limpeza            {0}        {1:.2f}%".format(necessita_de_limpeza, perc2))
print("3 - Necessita de troca de pecas     {0}        {1:.2f}%".format(necessita_troca_pecas, perc3))
print("4 - Quebrado ou inutillizado        {0}        {1:.2f}%".format(quebrado_inutilizado, perc4))
    

