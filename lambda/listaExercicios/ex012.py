i = 0
produtos = []

while i < 10:
  precoProduto = int(input("Digite o valor do produto: "))
  produtos.append(precoProduto)
  i = i + 1

desconto = int(input("valor de desconto por produto: "))

def aplicarDesconto(desconto, produtos):
  descontoPorProduto = desconto * len(produtos)
  valorAplicado = list(map(lambda x : x-((x/100)*descontoPorProduto), produtos ))
  print(valorAplicado)
  
  
aplicarDesconto(desconto, produtos)