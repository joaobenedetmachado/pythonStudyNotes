nome = input("qual seu nome>> ")
idade = int(input("sua idade>> "))

if idade < 16:
    print("nao vota")
if idade >=16 and idade < 18:
    print("nao obrigatorio")
if idade >= 18 and idade <= 65:
    print("obrigatorio")
if idade > 65:
    print("nao obrigatorio")