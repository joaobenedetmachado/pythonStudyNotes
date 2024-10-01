# Aluno: Joao Victor Benedet Machado          
# Turma: 2190
# Data: 27/08/2024

Tarefas = {} # cria o dicionario

def LastPosition(dic): # uma funcao para nao dar conflito de novas posicoes quando excluir e uma sobrepor a outra por exemplo
    NovaLista = list(dic)
    if NovaLista == []:
        return 1
    else: 
        UltimaPos = NovaLista[-1:]
        Numero = UltimaPos[0]
        return Numero + 1


def Adcionar(dic, pos, tarefa): # adciona pedindo o dicionario, posicao e tarefa nova
    dic[pos] = tarefa
    print("Tarefa Adcionada com sucesso!")


def Alterar(dic, pos, tarefa): # altera de acordo com o dicionario, pos, e tarefa 
    if pos not in dic.keys():
        print("ERROR! Posicao nao encontrada!")
    else:
        dic[pos] = tarefa
        print("Tarefa Alterada com sucesso!")


def Excluir(dic, pos): # pede o dicionario e a pos para excluir
    if pos not in dic.keys():
        print("ERROR! Posicao nao encontrada!")
    else:
        del dic[pos]
        print(f"Posição {pos} Excluida")

    
def Pesquisar(dic): # mostra o key e value do dicionario
    for i, o in dic.items():
        print(f"{i} : {o}")


def ShowMenu(): # mostra o menu
    print(""" 
Menu de Opções de Tarefas:
          
    1 - Adcionar
    2 - Alterar
    3 - Excluir
    4 - Pesquisar
    S - Sair  
               
""")
    

while True: # roda para sempre ate que haja ou break / exit()

    ShowMenu()
    
    escolha = str(input("> "))

    if escolha == '1': # se escolha igual a 1, cria a pos com a funcao e a nova tarefa o user que escolhe
        pos = LastPosition(Tarefas)
        novaTarefa = str(input("Digite a Tarefa: "))
        Adcionar(Tarefas, pos, novaTarefa)
        
    elif escolha == '2': # aqui ele pede a posicao, e alterar com a funcao 
        pos = int(input("Digite a posição da Tarefa que deseja alterar: "))
        novaTarefa = str(input("Digite a nova Tarefa: "))
        Alterar(Tarefas, pos, novaTarefa)
    
    elif escolha == '3': # excloi de acordo com a pos que o usuario escolher
        pos = int(input("Digite a posição da Tarefa que deseja EXCLUIR: "))
        Excluir(Tarefas ,pos)

    elif escolha == '4': # chama a funcao
        Pesquisar(Tarefas)

    elif escolha == '5': #sai com o exit(), e o break tambem funcionaria
        print("Saindo Do Programa...")
        exit()

    elif escolha not in ('1', '2', '3', '4', '5'): # caso a escolha nao esteja aq, da erro
        print("ERROR! Função nao encontrada! Tente Novamente")