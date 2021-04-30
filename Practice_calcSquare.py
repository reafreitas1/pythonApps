#Entrada
n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))
n3 = int(input("Digite o numero 3: "))
n4 = int(input("Digite o numero 4: "))
#Processamento
q1 = n1 * n1
q2 = n2 * n2
q3 = n3 * n3
q4 = n4 * n4
if(q3 >= 1000):
    print("O quadrado do numero 3 e maior que 1000: {0}.".format(q3))
else:
    print("O quadrado do numero {0} e {1}.".format(n1,q1))
    print("O quadrado do numero {0} e {1}.".format(n2,q2))
    print("O quadrado do numero {0} e {1}.".format(n3,q3))
    print("O quadrado do numero {0} e {1}.".format(n4,q4))