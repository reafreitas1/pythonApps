#Variaveis (esta mais para constante)
valor_hora = 10.00
valor_hora_excedente = 20.00
salario = 500.00
e = 0
#Entrada
c = int(input("Informe o codigo: "))
n = float(input("Informe a quantidade de hotas trabalhadas: "))
#Processamento
if n > 50:
    e = (n - 50) * valor_hora_excedente #20.00
    salario_total = (50 * valor_hora) + e #10.00
    print("Salario: R$ {0:.2f}".format(salario))
    print("Salario excendente: R$ {0:.2f}".format(e))
    print("Salario a receber: R$ {0:.2f}".format(salario_total))
else:
    salario_perdido = salario - (valor_hora * n)
    salario_total = (n * valor_hora) #10.00
    horas_nao_trabalhadas = 50 - n
    print("Salario: R$ {0:.2f}".format(salario))
    print("Horas nao trabalhadas de 50hrs: {0}hrs".format(horas_nao_trabalhadas))
    print("Salario perdido: - R$ {0:.2f}".format(salario_perdido))
    print("Salario a receber: R$ {0:.2f}".format(salario_total))
    