def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)

num = int(input("Digite um número não negativo para calcular o fatorial: "))
print(f"O fatorial de {num} é {fatorial(num)}.")
