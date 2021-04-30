#Entrada
numero = int(input("Digite um numero: "))
#processamento
if numero % 2 == 0:
    par = numero
    print("O numero {0} e par".format(par))
else:
    impar = numero
    print("O numero {0} e impar".format(impar))