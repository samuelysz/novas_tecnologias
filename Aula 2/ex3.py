import math

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def print_primos(n):
    count = 0
    num = 2
    while count < n:
        if primo(num):
            print(num, end=" ")
            count += 1
        num += 1

n = int(input("Digite o valor de n para os números primos: "))
print(f"Os {n} primeiros números primos são:")
print_primos(n)
