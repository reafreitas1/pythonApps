#Entrada
indice_poluicao = float(input("Informe o indice de poluicao: "))
#Processamento
if(indice_poluicao < 0.3):
    print("Indice de poluicao aceitavel.")
else:
    if(indice_poluicao >= 0.3 and indice_poluicao < 0.4):
        print("Atencao: Grupo 1 suspender atividades!")
    elif(indice_poluicao >= 0.4 and indice_poluicao < 0.5):
        print("Atencao: Grupo 2 suspender atividades!")
    elif(indice_poluicao >= 0.5):
        print("Atencao: Todos grupos suspender atividades!")