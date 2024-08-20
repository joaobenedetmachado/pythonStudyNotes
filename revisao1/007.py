nome = input('nome: ')
peso = int(input('peso: '))
altura = float(input('altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print("abaixo do peso")
if imc >= 18.5 and imc < 25:
    print("peso normal")
if imc >= 25 and imc < 30:
    print("acima do peso")
if imc >= 30:
    print("obeso")