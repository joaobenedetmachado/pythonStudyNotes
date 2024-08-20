lista = []

def Add(info):
    lista.append(info)

def View():
    for i in lista:
        print(i)

def Update(oldInfo, newInfo):
    if oldInfo in lista:
        index = lista.index(oldInfo)
        lista[index] = newInfo
    else:
        print(f"{oldInfo} nao encontrado na lista.")

def Delete(info):
    if info in lista:
        index = lista.index(info)
        del lista[index]
    else:
        print(f"{info} nao encontrado na lista.")


while True:
    print("""
    -=-=- LISTA DE FUNÇÕES -=-=-
    (1) Adicionar item à lista
    (2) Visualizar itens da lista
    (3) Atualizar item na lista
    (4) Deletar item da lista
    (5) Sair
""")
    
    escolha = int(input("> "))

    if escolha == 1:
        info = input("O que deseja add?: ")
        Add(info)

    elif escolha == 2:
        View()
    
    elif escolha == 3:
        View()
        oldInfo = input("Qual info deseja alterar: ")
        newInfo = input("Alterar para: ")
        Update(oldInfo, newInfo)

    elif escolha == 4:
        View()
        info = input("O que deseja excluir: ")
        Delete(info)

    elif escolha == 5:
        print("saindo do programa...")
        exit()

    else:
        print("Funcao nao encontrada, tente novamente! ")