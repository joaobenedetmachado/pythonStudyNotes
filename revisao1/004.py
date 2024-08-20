nome = input('Seu nome >>')
idade = int(input("Sua idade >> "))
peso = float(input("Seu Peso >> "))

if idade <= 15:
    print('negado')
if idade >= 16 and idade <= 17 and peso > 55:
    print('autorizado com responsaveis')
if idade >= 18 and idade <= 69 and peso > 60:
    print('autorizado')
if idade > 69:
    print('negado')