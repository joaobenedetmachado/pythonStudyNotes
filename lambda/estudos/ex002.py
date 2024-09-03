numeros = [1, 3, 6, 9, 11, 4, 8, 13, 15]
resultado = list(filter(lambda x : x > 5 and x % 2 ==1, numeros))
print(resultado)