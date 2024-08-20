while True: 
    TempCelcius = float(input("Graus em Celcius >>"))
    TempF = TempCelcius * 1.8 + 32
    TempK = TempCelcius + 273.15
    TempRe = TempCelcius * 0.8

    print(f"""
        {TempF} Fareheit
        {TempK} Kelvin
        {TempRe} Reaumor
    """)