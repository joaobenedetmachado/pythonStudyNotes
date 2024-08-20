litrosvendidos = int(input("Litros vendidos >> "))
tipo = str(input("G ou A >> "))

if tipo == 'A':  
    if litrosvendidos <= 20:
        desconto = 0.03  
    else:
        desconto = 0.05 
    preco = 4.22 * litrosvendidos * (1 - desconto)
    print(preco)

elif tipo == 'G':
    if litrosvendidos <= 20:
        desconto = 0.04 
    else:
        desconto = 0.06 
    preco = 5.65 * litrosvendidos * (1 - desconto)
    print(preco)
