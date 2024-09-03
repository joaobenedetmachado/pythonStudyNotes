lista = [
  lambda x : x*2,
  lambda x : x**2,
  lambda x : x**3,
]

while True:
  numero = int(input("escolha um numero ('0' para sair!): "))
  if numero == 0:
    exit()
  else:
    for i in lista:
      print(i(numero))
  (lambda x,y : print(f"{x}, possui {y} anos")) ((input("qual seu nome: ")), (input("quantos anos vc tem ")))

