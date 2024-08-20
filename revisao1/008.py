i = 0
cand1 = 0
cand2 = 0
cand3 = 0

while i < 3:
    i = i + 1
    escolha = int(input('Qual candidato deseja? (1, 2 ou 3) >> '))
    if escolha == 1:
        cand1 = cand1 + 1
    elif escolha == 2:
        cand2 = cand2 + 1
    elif escolha == 3:
        cand3 = cand3 + 1
    else:
        print("Escolha inválida! Digite 1, 2 ou 3.")

print(f'Cand1: {cand1} votos')
print(f'Cand2: {cand2} votos')
print(f'Cand3: {cand3} votos')
