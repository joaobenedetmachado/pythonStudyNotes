#Aluno: João Victor Benedet Machado
#Turma: 2190
#Data : 17/09/2024

from functools import reduce # importa o reduce

listaReceitas = [] # crias ambas listas
listaDespesas = []

listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] # lista para os meses

dicLucros = {} # para os lucros que sera relacionado MES x LUCRO

i = 0

while i <= 11: # faz isso 12 vezes para cada mes e adciona para as listas
    receita = float(input(f'Qual foi sua receita do mês de {listaMeses[i]}? '))
    despesa = float(input(f'Qual foi sua despesa do mês de {listaMeses[i]}? '))
    listaReceitas.append(receita)
    listaDespesas.append(despesa)
    i = i + 1


def CalcularLucroMensal(receitas, despesas): # calcula o lucro com a funcao, usa o map e o for para "atualizar" e fazer a relacao
    ListaLucroMensal = list(map(lambda x, y : x - y, receitas, despesas))
    for i in range(len(ListaLucroMensal)):
        dicLucros[(listaMeses[i])] = ListaLucroMensal[i]
    for i in range(len(ListaLucroMensal)):
        print(f'O mês {listaMeses[i]} faturou {ListaLucroMensal[i]}')
    return ListaLucroMensal 


def CalcularMediaLucroAnual(lista, tamanho): # calcula a media com o reduce
    media = (reduce(lambda x, y : x + y, lista) / tamanho)
    return media


def CalcularPrejuizo(lista): # checa se algum mes tem o value como menor que zero, se sim, printa o seu key junto
    prejuizo = list(filter(lambda x : x < 0, lista))
    for i, o in dicLucros.items():
        if o < 0:
            print(f'O mês {i} esta negativado com {o}')   
    if len(prejuizo) == 0:
        print("Não houveram meses com preju")     

print() # essa area printa e chama as funcoes
listaLucros = CalcularLucroMensal(listaReceitas, listaDespesas)
print()
MediaLucros = CalcularMediaLucroAnual(listaLucros, len(listaMeses))
print(f'A Média de lucro foi de {MediaLucros}')
print()
CalcularPrejuizo(listaLucros)
print()