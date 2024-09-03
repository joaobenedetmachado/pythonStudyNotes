listaNumero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultado = list(map(lambda x: x * 2 if x % 2 != 0 else x, listaNumero))

print(resultado)
