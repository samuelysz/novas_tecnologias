def tabuada():
    n = int(input("Digite o número para a tabuada: "))
    print(f"Tabuada de {n}:")
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

tabuada()
