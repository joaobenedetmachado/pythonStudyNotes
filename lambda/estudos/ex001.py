strings = ["ola", "mundo", "oi", "python", "a", "lambda"]
resultado = list(map(lambda x: x.upper(), filter(lambda x: len(x) > 3, strings)))
print(resultado)
