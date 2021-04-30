#Entrada
idade_nadador = int(input("Informe a idade: "))
#processsamento
if(idade_nadador < 5):
    print("Idade invalida!")
else:
    if(idade_nadador >= 5 and idade_nadador <= 7):
        print("Aluno pertence a turma: Infantil A")
    elif(idade_nadador >= 8 and idade_nadador <= 11):
        print("Aluno pertence a turma: Infantil B")
    elif(idade_nadador >= 12 and idade_nadador <= 13):
        print("Aluno pertence a turma: Juvenil A")
    elif(idade_nadador >= 14 and idade_nadador <= 17):
        print("Aluno pertence a turma: Juvenil B")
    elif(idade_nadador >= 18):
        print("Aluno pertence a turma: Adultos")