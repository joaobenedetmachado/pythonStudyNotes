def calcularAreaCirculo(raio):
    print("A area é:", (raio**2) * 3.14)


def calcularAreaTriangulo(base, altura):
    print("A area é:", (base * altura) / 2)


def calcularAreaRetangulo(base, altura):
    print("A area é:", (base * altura))


while True:
    print(""" 
        -=-=- CALCULADORA GEOMETRICA -=-=-
        (1) Calcular Circulo
        (2) Calcular Triangulo
        (3) Calcular Retangulo
        (4) Sair
""")
    
    escolha = int(input("> "))

    if escolha == 1:
        raio = float(input("Qual o raio? "))
        calcularAreaCirculo(raio)

    elif escolha == 2:
        base = float(input("Qual a base? "))
        altura = float(input("Qual a altura? "))
        calcularAreaTriangulo(base, altura)

    elif escolha == 3:
        base = float(input("Qual a base? "))
        altura = float(input("Qual a altura? "))
        calcularAreaRetangulo(base, altura)

    elif escolha == 4:
        print("saindo do programa...")
        exit()

    else:
        print("Funcao nao encontrada, tente novamente! ")

    