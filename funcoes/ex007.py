import math

def CalcularHipotenusa(a=0, b=0):
    c = a**2 + b**2
    resultado = math.sqrt(c)
    print(f'{resultado:.2f}')


while True:
    cateto1 = int(input("Ensira o valor do cateto 1> "))
    cateto2 = int(input("Ensira o valor do cateto 2> "))
    CalcularHipotenusa(a=cateto1, b=cateto2)
