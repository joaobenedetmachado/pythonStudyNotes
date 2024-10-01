#Aluno: João Victor Benedet Machado
#Turma: 2190
#Data : 17/09/2024

from functools import reduce # importa o reduce

dicFuncionarios_x_Salarios = {} # cria o dicionario

def CadastrarFuncionarios(nome, salario, dicionario): # funcao para cadastrar com nome e salario
    dicionario[nome] = salario

def PrintarFuncionarios(): # printa os funcionarios para debug
    for i, o in dicFuncionarios_x_Salarios.items():
        print(f'{i} : {o}')

while True: # enquanto resposta nao for 'n', ele coloca o nome e seu respectivo salario
    nome = input("Nome do funcionario: ").title()
    salario = float(input(f"Salario de {nome}: "))
    CadastrarFuncionarios(nome, salario, dicFuncionarios_x_Salarios)
    resposta = input("Deseja continuar? [S/N]: ").lower()
    if resposta == 'n':
        break
    else:
        continue


valorDeterminado = float(input("Valor que deseja determinar: ")) # pergunta o valor determinado


def FiltrarSalario(dicionario,valorDeterminado): # filtra de acordo com o filter e retorna para a variavel
    salariosFiltrados = list(filter(lambda x : x < valorDeterminado, dicionario.values()))
    return salariosFiltrados


def AplicarAumento(valores): # cria um lista com o resultado do map, e com o for addciona para cada
    valorAumentado = list(map(lambda x : (x * 0.15) + 0, filter(lambda x : x < valorDeterminado, valores)))
    for i, o in dicFuncionarios_x_Salarios.items():
        if o < valorDeterminado:
            dicFuncionarios_x_Salarios[i] = ((o * 0.15) + o)


def MediaDeSalarios(dicionario): # faz a media com o reduce dividido pelo len e printa-o
    media = reduce(lambda x, y : x + y, dicionario.values()) / len(dicionario.keys())
    print()
    print(f'A média de salarios é {media}')


def MaiorEMenorSalario(dicionario): # chega o menor e o maior salario de acordo com sua posicao nos .values do dicionario
    menorSalario = min(dicionario.values())
    maiorSalario = max(dicionario.values()) 
    for i, o in dicionario.items():
        if o == menorSalario:
            print(f'{i} tem o menor salario!')
    for i, o in dicionario.items():
        if o == maiorSalario:
            print(f'{i} tem o maior salario!')



valores = FiltrarSalario(dicFuncionarios_x_Salarios, valorDeterminado) # essa area apenas declara variaveis como retorno de funcoes e chama as funcoes
AplicarAumento(valores)
MediaDeSalarios(dicFuncionarios_x_Salarios)
print()
MaiorEMenorSalario(dicFuncionarios_x_Salarios)
print()
PrintarFuncionarios()
print()