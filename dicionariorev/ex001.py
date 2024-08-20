dic = {}

while True:
    print(""" 
        1 - add
        2 - remove
        3 - altera
        4 - pesquisa
        6 - sair
    """)

    escolha = int(input(">> "))

    if escolha == 1 :
        nome = str(input('nome: '))
        numero = int(input("numero "))
        dic[nome] = numero
    if escolha == 2:
        nome = str(input("nome remover"))
        del dic[nome]
    if escolha == 3:
        nome = str(input('nome: '))
        numero = int(input("numero "))
        dic[nome] = numero
    if escolha == 4:
        for i, k in dic.items():
            print(f'{i} : {k}')