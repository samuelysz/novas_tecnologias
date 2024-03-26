def quadrado_soma_impares(num):
    return sum(range(1, num * 2, 2))

num = int(input("Digite um número para calcular o quadrado usando soma de ímpares: "))
print(f"O quadrado de {num} é {quadrado_soma_impares(num)}.")
