estudantes = [
    {"nome": "Ana", "notas": [6, 7, 8]},
    {"nome": "Pedro", "notas": [5, 6, 5]},
    {"nome": "Maria", "notas": [9, 7, 8]},
    {"nome": "João", "notas": [4, 6, 5]}
]

resultado = list(map(
    lambda e: e["nome"],
    filter(
        lambda e: sum(e["notas"]) / len(e["notas"]) >= 7,
        estudantes
    )
))
print(resultado)