while True: 
    nome = input("seu nome >>")
    idade = int(input('sua idade >>'))

    if idade < 2:
        print("Bercario")
    elif idade >= 3 and idade <= 6:
        print("Educacao Infantil")
    elif idade >= 7 and idade <= 10:
        print("Fund I")
    elif idade >= 11 and idade <= 15:
        print("Fund II")
    elif idade >= 15 and idade <= 18:
        print("Ensino Medio")
    else:
        print("voce nao digitou um valor valido")
        exit()