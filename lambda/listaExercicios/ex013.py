funcionarios = []
i = 0
while i < 4:
  dic = {}
  nomeFuncionario = input("qual seu nome? ")
  dic['nome'] = nomeFuncionario
  salario = int(input("qual seu salario? "))
  dic['salario'] = salario
  funcionarios.append(dic)
  i = i + 1


def Filtrar(funcionarios):
  valorEscolha = int(input("Encontrar funcionarios com o salario acima de: "))
  resultadoFiltro = list(filter(lambda x : x['salario'] > valorEscolha, funcionarios))
  resultado = list(map(lambda x: {**x, 'salario': x['salario'] * 1.10}, resultadoFiltro))
  print(resultado)
  


Filtrar(funcionarios)
