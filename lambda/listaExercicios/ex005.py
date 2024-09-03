listaNumero = [1, 5, 6, 7, 8, 10, 15, 20, 50]

resultado = list(filter(lambda x : x % 5 == 0, listaNumero))

print(resultado)