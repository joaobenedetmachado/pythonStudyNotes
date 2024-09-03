palavras = ["casa", "livro", "carro", "árvore", "cachorro", "sol", "computador", "mesa", "gato", "janela"]

# Expressão lambda para contar o número de vogais em uma palavra
conta_vogais = lambda palavra: sum(1 for letra in palavra if letra in "aeiouAEIOU")

# Ordenando a lista com base na quantidade de vogais em cada palavra
palavras_ordenadas = sorted(palavras, key=conta_vogais)

print(palavras_ordenadas) # RESOLUCAO DO CHAT GPT!!! *#
