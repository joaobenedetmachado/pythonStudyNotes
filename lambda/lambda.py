# # strings = ["ola", "mundo", "oi", "python", "a", "lambda"]
# # resultado = list(map(lambda x: x.upper(), filter(lambda x: len(x) > 3, strings)))
# # print(resultado)

# # numeros = [1, 3, 6, 9, 11, 4, 8, 13, 15]
# # resultado = list(filter(lambda x : x > 5 and x % 2 ==1, numeros))
# # print(resultado)

# produtos = [("Celular", 2000), ("Camiseta", 30), ("Relógio", 150), ("Livro", 45), ("Teclado", 100)]
# resultado = list(map(lambda x: x[0].upper(), filter(lambda x: x[1] > 50, produtos)))
# print(resultado)

# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
# resultado = list(map(sum, filter(lambda x: sum(x) % 2 == 0, listas)))
# print(resultado)

# estudantes = [
#     {"nome": "Ana", "notas": [6, 7, 8]},
#     {"nome": "Pedro", "notas": [5, 6, 5]},
#     {"nome": "Maria", "notas": [9, 7, 8]},
#     {"nome": "João", "notas": [4, 6, 5]}
# ]

# resultado = list(map(
#     lambda e: e["nome"],
#     filter(
#         lambda e: sum(e["notas"]) / len(e["notas"]) >= 7,
#         estudantes
#     )
# ))
# print(resultado)

# nums = [1, 2, 3, 4, 5, 6]
# resultado = list(map(lambda x : x**2, filter(lambda x: x % 2 == 0, nums)))
# print(resultado)

# livros = [
#     {"titulo": "a revolução dos bichos", "ano": 1945},
#     {"titulo": "o senhor dos anéis", "ano": 1954},
#     {"titulo": "harry potter e a pedra filosofal", "ano": 1997},
#     {"titulo": "o código da vinci", "ano": 2003},
#     {"titulo": "a breve história do tempo", "ano": 1988},
#     {"titulo": "game of thrones", "ano": 1996}
# ]

# resultado = list(
#   map(lambda x: x["titulo"].title(), 
#   filter(lambda livro: livro["ano"] > 2000, livros)))
# print(resultado)



# produtos = [
#     {"nome": "teclado mecânico", "preço": 120},
#     {"nome": "mouse", "preço": 45},
#     {"nome": "monitor", "preço": 300},
#     {"nome": "cadeira gamer", "preço": 350},
#     {"nome": "pendrive", "preço": 30},
#     {"nome": "headset", "preço": 75}
# ]

# resultado = list(map(lambda x : x["nome"].upper(), 
#             filter(lambda y: y["preço"] > 50, produtos)))
# print(resultado)

# alunos = [
#     {"nome": "joão silva", "nota_final": 6.5, "passou": False},
#     {"nome": "maria oliveira", "nota_final": 7.2, "passou": True},
#     {"nome": "pedro alves", "nota_final": 8.0, "passou": True},
#     {"nome": "ana souza", "nota_final": 5.8, "passou": False},
#     {"nome": "luana martins", "nota_final": 7.8, "passou": True},
#     {"nome": "carlos mendes", "nota_final": 6.9, "passou": True}
# ]

# resultado = list(map(lambda x : x["nome"].title(),
#             filter(lambda x: x["nota_final"] >= 7 and x["passou"] == True, alunos)))
# print(resultado)


# transacoes = [
#     {"cliente": "Ana", "valor": 120.50, "data": "2023-01-15"},
#     {"cliente": "Pedro", "valor": 45.00, "data": "2022-12-30"},
#     {"cliente": "Ana", "valor": 80.75, "data": "2023-03-22"},
#     {"cliente": "João", "valor": 200.00, "data": "2023-04-10"},
#     {"cliente": "Pedro", "valor": 60.25, "data": "2023-02-18"},
#     {"cliente": "Carlos", "valor": 150.00, "data": "2023-05-25"},
#     {"cliente": "Ana", "valor": 40.00, "data": "2023-06-30"},
#     {"cliente": "Carlos", "valor": 100.00, "data": "2023-07-15"}
# ]

resultado = list(map)
print(resultado)
