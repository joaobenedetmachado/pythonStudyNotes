destinos = {
    "new york": [["2019/20/10", "2020-19-10"], 12]
}

def Add(Destino, datas, numPassageiros):
    destinos[Destino] = [datas, numPassageiros]

def Show(dictionary):
    for i, o in destinos.items():
        print(f"Destino: {i}, data inicio: {o[0][0]} data fim: {o[0][1]}, numero de passageirs {o[1]}")

while True:
    print("""
    -=-=- MENU DE DESTINOS -=-=-
    (1) Adicionar novo destino
    (2) Mostrar destinos
    (3) Sair
    """)

    escolha = int(input("> "))

    if escolha == 1:
        destino = input("Qual o local de escolha?: ")
        datas = []
        dataInicio = input("Qual a data de inicio? USE [dd-mm-aaaa]")
        datafim = input("Qual a data de fim? USE [dd-mm-aaaa]")
        datas.append(dataInicio)
        datas.append(datafim)
        numeroDePassegeiros = int(input("Qual o numero de passageiros?: "))
        Add(destino, datas, numeroDePassegeiros)

    

    elif escolha == 2:
        Show(destinos)

    elif escolha == 3:
        print("saindo do programa...")
        exit()


    else:
        print("Funcao nao encontrada, tente novamente! ")