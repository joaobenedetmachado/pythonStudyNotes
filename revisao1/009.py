i = 0
alturaf = []
alturam = []
sexof = 0
sexom = 0

while i < 5:
    i = i + 1
    nome = input('Digite o nome: ')
    sexo = input("Maculino ou Feminino (f ou m)")
    altura = float(input('Digite a altura: '))
    if sexo == 'f':
        alturaf.append(altura)
        sexof = sexof + 1
    else:
        alturam.append(altura)
        sexom = sexom + 1


maioralturaf = max(alturaf)
maioralturam = max(alturam)
total_pessoas = sexof + sexom
mediamulheres = sum(alturaf) / len(alturaf)
porcentagensf = (sexof / total_pessoas) * 100
porcentagensm = (sexom / total_pessoas) * 100

print(f"Maior altura feminina: {maioralturaf} cm")
print(f"Maior altura masculina: {maioralturam} cm")
print(f"Média de altura das mulheres: {mediamulheres:.2f} cm")
print(f"Porcentagem feminina: {porcentagensf:.2f}%")
print(f"Porcentagem masculina: {porcentagensm:.2f}%")