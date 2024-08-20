import random

def randomNumber():
    return random.randrange(0, 100)

while True:
    escolha = int(input("Escolha um numero de 0 a 100: "))
    numeroAleatorio = randomNumber()

    if escolha == numeroAleatorio:
        print("Você acertou!")
    else:
        print(f"Voce errou, numero escolhido {numeroAleatorio}")