lista = []

while True:
    print("""
    1 - add
    2 - remover
    3 - mostrar todos
    4 - mostrar pares    
    5 - mostrar impares
    6 - mostrar primos
    7 - sair
""")
    
    escolha = int(input('>> '))

    if escolha == 1:
        num = int(input('Digite um número: '))
        lista.append(num)
    if escolha == 2:
        num = int(input('Digite um número para remover: '))
        if num in lista:
            lista.remove(num)
    if escolha == 3:
        for i in lista:
            print(i)
    if escolha == 4:
        for i in lista:
            if i % 2 == 0:
                print(i)
    if escolha == 5:
        for i in lista:
            if i % 2 == 1:
                print(i)
    if escolha == 6:
        for i in lista:
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        print(i)
    if escolha == 7:
        break
    