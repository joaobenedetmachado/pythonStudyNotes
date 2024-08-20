def Multiplicar(a, b):
    print(a*b)


def Dividir(a, b):
    print(a/b)


def Diminuir(a, b):
    print(a-b)


def Somar(a, b):
    print(a+b)


while True:
    print(""" 
        -=-=- CALCULADORA GEOMETRICA -=-=-
        (1) Multiplicar
        (2) Dividir
        (3) Diminuir
        (4) Somar
        (5) Sair
""")
        
    escolha = int(input("> "))

    if escolha == 1:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: ")) 
        Multiplicar(a, b)

    elif escolha == 2:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: ")) 
        Dividir(a, b)

    elif escolha == 3:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: ")) 
        Diminuir(a, b)

    elif escolha == 4:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: ")) 
        Somar(a, b)
    
    elif escolha == 5:
        print("saindo do programa...")
        exit()

    else:
        print("Funcao nao encontrada, tente novamente! ")


