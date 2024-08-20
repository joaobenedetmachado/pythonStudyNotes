def valorPagamento(value, days):
    if days == 0:
        print(f"Você não tem atraso, valor a ser pago: {value:.2f}")
        exit()
    elif days > 0:
        value = (value/100) * 3 + value
        for i in range(days):
            porcentagem = (value / 100) * 1
            value += porcentagem
        print(f"Novo valor a ser pago: {value:.2f}")
    else:
        print("Erro: o número de dias não pode ser negativo.")

while True:
    valor = float(input("Escreva o valor: "))
    dias = int(input("numero de dias: "))
    valorPagamento(valor, dias)