palavra = 'abacate'
palavralista = list(palavra)
vogais = list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], palavralista))
print(len(vogais))
