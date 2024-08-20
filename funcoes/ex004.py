agenda = {}

def NewPosition(dictionary):
    if dictionary:
        return list(dictionary.keys())[-1] + 1
    else:
        return 0 

def Add(contato, pos):
    agenda[pos] = contato

def View(obj):
    if obj:
        for i, o in obj.items():
            print(f"{i} = {o}")
    else:
        print("A agenda está vazia.")

def Edit(pos, NewInfo):
    if pos in agenda:
        agenda[pos] = NewInfo
    else:
        print(f"Posição {pos} não encontrada na agenda.")

while True: 
    print("""
    -=-=- AGENDA TELEFÔNICA -=-=-
    (1) Adicionar contato
    (2) Visualizar contatos
    (3) Editar contato
    (4) Sair
    """)

    escolha = int(input("> "))

    if escolha == 1:
        contato = input("Qual a informacao do novo contato?: ")
        pos = NewPosition(agenda)
        Add(contato, pos)

    elif escolha == 2:
        View(agenda)

    elif escolha == 3:
        pos = input("Qual a posicao que deseja alterar: ")
        NewInfo = input("Qual a nova informação?: ")
        Edit(pos, NewInfo)

    
    elif escolha == 4:
        print("saindo do programa...")
        exit()

    else:
        print("Funcao nao encontrada, tente novamente! ")
