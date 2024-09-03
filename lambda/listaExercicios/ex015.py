from functools import reduce


def mediaLucro(receitas, despesas):
  resultado = list(map(lambda x, y : x - y, receita, despesa))
  media = (reduce(lambda x, y: x + y, resultado))/ len(receita)
  print(media)

receita = [
  1000,
  2000,
  2000,
  3000,
]

despesa = [
  500,
  1000,
  1000,
  1500,
]

mediaLucro(receita, despesa)
