listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
resultado = list(map(sum, filter(lambda x: sum(x) % 2 == 0, listas)))
print(resultado)