temperaturas = []

for i in range(12):
    temperatura = float(input(f"Digite a temperatura no mes f{i}: "))
    temperaturas.append(temperatura)

temperaturamedia = sum(temperaturas) / len(temperaturas)

for temp in temperaturas:
    if temp > temperaturamedia:
        print(temp)

