#Entrada
nome = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")
#Processamento
while senha == nome:
    print("Usuario e senha nao podem ser iguais")
    nome = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")