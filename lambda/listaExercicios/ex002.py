from functools import reduce

listaNumero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultadoReduce = reduce(lambda x, y : x + y, listaNumero)
resultado = resultadoReduce/len(listaNumero)
print(resultado)