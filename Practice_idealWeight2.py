#Entrada
altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo M ou F: ")
#processamento #lower = converte o maiusculo para minusculo
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo nao reconhecido.")
#saida
print("Seu peso ideal e {0:.2f}".format(peso_ideal))    

"""if sexo == "M" or sexo == "m":
    peso_ideal = (72.7 * altura) - 58
if sexo == "F" or sexo == "f":
    peso_ideal = (62.1 * altura) - 44.7
#saida
print("Seu peso ideal e {0:.2f}".format(peso_ideal))"""