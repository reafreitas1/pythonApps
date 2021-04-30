#Entrada
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
valor_hora = float(input("Informe valor da hora $: "))
#Processamento
salario = horas_trabalhadas * valor_hora
#saida
print("O salario a receber e $: {0:.2f}". format(salario))