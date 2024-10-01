nomes = ['a', 'joao', 'lara', 'gabriel', 'carlos']

ordenado = sorted(nomes, key=lambda x : len(x))
odernadoinverso = sorted(nomes, reverse=True, key=lambda x: len(x))
print(odernadoinverso)
print(ordenado  )