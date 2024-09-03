produtos = [("Celular", 2000), ("Camiseta", 30), ("Relógio", 150), ("Livro", 45), ("Teclado", 100)]
resultado = list(map(lambda x: x[0].upper(), filter(lambda x: x[1] > 50, produtos)))
print(resultado)