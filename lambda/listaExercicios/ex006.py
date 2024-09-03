lista = ['maça', 'banana', 'churrasqueira', 'dente']

resultado = list(map(lambda x : len(x), lista))
resultado.sort()

print(resultado)