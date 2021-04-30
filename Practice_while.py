#Variaveis
maior = 0
#Entrada
n = int(input("Digite um numero: "))
#processamento
while n != 0:
    if n > maior:
        maior = n
    n = int(input("Digite um numero: "))
print("O maior numero e {0}".format(maior))