palavras = ["casa", "livro", "carro", "árvore", "cachorro", "sol", "computador", "mesa", "gato", "janela"]

resultado = list(map(lambda x: len(x), filter(lambda x : len(x)> 3, palavras)))

print(resultado)