# Definindo os dados das cidades em uma lista de dicionários
cidades = [
    {"codigo": 1, "veiculos": 10000, "acidentes": 50},
    {"codigo": 2, "veiculos": 20000, "acidentes": 75},
    {"codigo": 3, "veiculos": 30000, "acidentes": 90},
    {"codigo": 4, "veiculos": 40000, "acidentes": 120},
    {"codigo": 5, "veiculos": 50000, "acidentes": 150}
]

total_veiculos = sum(cidade['veiculos'] for cidade in cidades)
total_acidentes = sum(cidade['acidentes'] for cidade in cidades)

media_veiculos = total_veiculos / len(cidades)



cidades_menos_2000 = [cidade for cidade in cidades if cidade['veiculos'] < 2000]
if cidades_menos_2000:
    media_acidentes_menos_2000 = sum(cidade['acidentes'] for cidade in cidades_menos_2000) / len(cidades_menos_2000)
else:
    media_acidentes_menos_2000 = 0

# Imprimindo os resultados
print("Maior índice de acidentes:")

print("\nMenor índice de acidentes:")

print(f"\nMédia de veículos: {media_veiculos}")

print(f"\nMédia de acidentes em cidades com menos de 2000 veículos: {media_acidentes_menos_2000}")