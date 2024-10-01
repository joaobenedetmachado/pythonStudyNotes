# Aluno: Joao Victor Benedet Machado          
# Turma: 2190
# Data: 27/08/2024

TabelaCamp = ("Botafogo", "Fortaleza", "Flamengo", "Palmeiras", "São Paulo", "Cruzeiro", "Bahia", "Atletico-PR",
            "Atlético-MG", "Vasco", "Bragantino", "Juventude", "Grêmio", "Criciúma", "Internacional", "Vitória",
            "Corinthians", "Fluminense", "Cuiabá", "Atletico-GO") #Declaracão da tupla de acordo com o descrito na prova

def Primeiros(tupleName, n):  #Criaçao de uma funcao para mostrar os primeiros (N) colocados de uma tupla ou lista
    print(f"Os Primeiros {n} colocados são:") 
    for i in tupleName[0:n]:
        print("   ", i)


def Ultimos(tupleName, n):  #Criaçao de uma funcao para mostrar os ultimos (N) colocados de uma tupla ou lista
    print(f"Os Ultimos {n} colocados são:")
    for i in tupleName[-n:]:
        print("   ", i)


def OrdemAlfabetica(tupleName):  #Criação de uma funcao que recebe uma tupla e lista-a em ordem alfabetica com o .sort()
    ListaTabela = list(tupleName)
    ListaTabela.sort()
    print("Em ordem Alfabetica: ")
    for i in ListaTabela:
        print("   ", i)
    
            

def PosicaoDeItem(tupleName, msg): #Criação de uma função onde ele recebe a tupla e um "obj", que nesse caso é um valor que esta inserido, ou não
    if msg in tupleName:
        print(f"{msg} está na posicao {tupleName.index(msg) + 1}")
    else:
        print("ERRO, OBJETO NÃO ENCONTRADO")
    


Primeiros(TabelaCamp, 5) #Chamado de cada uma das 4 funcoes e seus respectivos argumentos
Ultimos(TabelaCamp, 4)
OrdemAlfabetica(TabelaCamp)
PosicaoDeItem(TabelaCamp, "Criciúma")

