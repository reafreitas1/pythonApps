#Variaveis
maior = -999
menor = 999
soma = 0
#Entrada
for n in range(1, 11):
    valor = int(input("Informe um numero: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input("Informe um numero: "))
media = soma / 10
#saidas
print("O maior numero e {0}.".format(maior))
print("O menor numero e {0}.".format(menor))
print("O media dos numeros e {0}.".format(media))
