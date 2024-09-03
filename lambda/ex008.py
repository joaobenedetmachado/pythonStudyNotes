produtos = [
    {"nome": "teclado mecânico", "preço": 120},
    {"nome": "mouse", "preço": 45},
    {"nome": "monitor", "preço": 300},
    {"nome": "cadeira gamer", "preço": 350},
    {"nome": "pendrive", "preço": 30},
    {"nome": "headset", "preço": 75}
]

resultado = list(map(lambda x : x["nome"].upper(), 
            filter(lambda y: y["preço"] > 50, produtos)))
print(resultado)