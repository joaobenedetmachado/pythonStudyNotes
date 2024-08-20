while True: 
    porHora = int(input("Quanto ganha por hora? >>"))
    HorasPorMes = int(input("Quantas horas por mes? >>"))

    SalarioTotal = porHora * HorasPorMes
    IR = (SalarioTotal/100)*11
    INSS = (SalarioTotal/100)*8
    SINDICATO = (SalarioTotal/100)*5
    SalarioLiquido = SalarioTotal - (IR + INSS + SINDICATO)

    print(SalarioTotal, "Bruto")
    print(IR, "IR")
    print(INSS, "INSS")
    print(SINDICATO, "SINDICATO")
    print(SalarioLiquido, "LIQUIDO")
