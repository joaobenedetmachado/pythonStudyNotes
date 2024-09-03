pessoas = [
    {"nome": "joão", "idade": 17},
    {"nome": "maria", "idade": 22},
    {"nome": "ana", "idade": 19},
    {"nome": "pedro", "idade": 15},
    {"nome": "camila", "idade": 25},
    {"nome": "luis", "idade": 30}
]

resultado = list(map(lambda x: x["nome"].title(), 
            filter(lambda x : "a" in x["nome"] and x["idade"] > 18, pessoas)))
print(resultado)