#Entrada
numero = int(input("Digite um numero para tabuada: "))
#Processamento
while numero > 10:
    print("O numero deve ser de 1 ao 10")
    numero = int(input("Digite um numero para tabuada: "))
print("Tabuada do {0}".format(numero))
for n in range (1, 11):
    valor = numero * n
    print("{0} X {1} = {2}". format(numero, n, valor))