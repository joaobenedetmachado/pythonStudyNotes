alunos = [
    {"nome": "joão silva", "nota_final": 6.5, "passou": False},
    {"nome": "maria oliveira", "nota_final": 7.2, "passou": True},
    {"nome": "pedro alves", "nota_final": 8.0, "passou": True},
    {"nome": "ana souza", "nota_final": 5.8, "passou": False},
    {"nome": "luana martins", "nota_final": 7.8, "passou": True},
    {"nome": "carlos mendes", "nota_final": 6.9, "passou": True}
]

resultado = list(map(lambda x : x["nome"].title(),
            filter(lambda x: x["nota_final"] >= 7 and x["passou"] == True, alunos)))
print(resultado)