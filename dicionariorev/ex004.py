lista = [
    {'nome' : 'titanic', 'genero' : 'comedia'},
    {'nome' : 'homem aranha', 'genero' : 'acao'},
    {'nome' : 'american pie', 'genero' : 'suspense'},
]

print(lista[1]['genero'])

for i in range(len(lista)):
    print(lista[i]['nome'])
    print(lista[i]['genero'])