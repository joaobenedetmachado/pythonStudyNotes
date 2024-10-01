def fibonacci(n):
    fib_sequence = [0, 1]  # Inicia com os dois primeiros números da sequência
    fib_lambda = lambda x: (fib_sequence.append(x), x + fib_sequence[-2])[1]
    
    for i in range(2, n):  # Começa a partir do terceiro termo
        fib_lambda(fib_sequence[-1] + fib_sequence[-2])  # Calcula o próximo número

    return fib_sequence[:n]  # Retorna apenas os primeiros n números

# Exemplo de uso
N = 100  # Número de termos que você deseja na sequência de Fibonacci
resultado = fibonacci(N)
print(resultado)
