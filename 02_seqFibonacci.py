def verifica_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

# Número para verificar
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
verifica_fibonacci(numero)
