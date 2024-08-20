nome = input('seu nome: ')
idade = int(input('sua idade: '))
valordoplano = float(input('valor do plano: '))

if idade <= 18:
    valor = valordoplano * 1.05
    print(valor)
if idade > 18 and idade <= 35:
    valor = valordoplano * 1.1
    print(valor)
if idade > 35 and idade <= 60:
    valor = valordoplano + 1.15
    print(valor)
if idade > 60:
    valor = valordoplano * 1.2
    print(valor)
