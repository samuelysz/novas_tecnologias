def fibonacci(n):
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

n = int(input("Digite o valor de n para o termo da série de Fibonacci: "))
print(f"O {n}-ésimo termo da série de Fibonacci é {fibonacci(n)}.")
