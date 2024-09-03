clientes = [
    {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
    {"nome": "Carlos", "idade": 35, "cidade": "Rio de Janeiro"},
    {"nome": "Beatriz", "idade": 22, "cidade": "Belo Horizonte"},
    {"nome": "Diego", "idade": 40, "cidade": "São Paulo"},
    {"nome": "Fernanda", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Lucas", "idade": 26, "cidade": "Belo Horizonte"},
    {"nome": "Mariana", "idade": 32, "cidade": "São Paulo"},
]

def Filtrar(dicionario):
  idade = int(input("Idade maior que:"))
  cidade = input("Cidade: ")
  resultado = list(map(lambda x : f"{x["nome"]}, {x["cidade"]}" ,filter(lambda x : x["idade"] > idade and x["cidade"] == cidade, dicionario)))
  print(resultado)
  
Filtrar(clientes)