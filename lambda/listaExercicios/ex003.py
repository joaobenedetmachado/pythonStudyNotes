nomes = ['joao', 'murco', 'marina', 'lara', 'arthur']

resultado = list(map(lambda x : x.title(), filter(lambda x : 'a' in x, nomes)))

print(resultado)