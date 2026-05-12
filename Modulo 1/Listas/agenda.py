import os

def limpa_tela():
    os.system("cls")

def adiciona_nome(lista_nomes,nome):
    lista_nomes.append(nome) #Adiciona nome na lista_nome.

def remover_nome(lista_nomes, nome):
    if nome in lista_nomes: # <--- A VERIFICAÇÃO FICA AQUI
        lista_nomes.remove(nome)
        print(f"O nome {nome} foi removido!")
    else:
        print("Erro: Este nome não existe na lista!")
    input("Aperte enter para continuar") # Para o usuário ler a mensagem

def mostrar_nomes(lista_nomes):
    for nome in lista_nomes: #["joao","maria","Ana"]
        print(nome)

nomes = []
while True:
    limpa_tela()
    menu = input("Escolha sua opção;\n[1] - Listar nomes\n[2] - Adicionar nomes\n[3] - Remover nomes\n[0] - Sair\n - Sua opções:")
    if menu == "0":
        break
    elif menu == "1":
        mostrar_nomes(nomes)
        input("Aperta enter pra continuar")
    elif menu == "2":
        nome_salvar = input("Digite o nome que deseja adicionar: ")
        adiciona_nome(nomes , nome_salvar)
    elif menu == "3":
        nome_remover = input("Digite o nome que deseja remover: ")
        remover_nome(nomes, nome_remover)
    else:
        print("Opção invalida.")
        input("Aperta enter pra continuar")



for i in range(5):
    nome = input("Digite o nome que deseja salvar: ")
    adiciona_nome(nomes,nome)