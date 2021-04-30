#Variaveis
excesso = 0
multa = 0
#Entrada
peso_peixes = float(input("Informe o peso dos peixes: "))
#Processamento
if peso_peixes > 50:
    excesso = peso_peixes - 50
    multa = excesso * 4
#saida
print("Peso dos peixes e {0:.2f}".format(peso_peixes))
print("Excesso de peso e {0:.2f}".format(excesso))
print("Valor da multa e R$ {0:.2f}".format(multa))