def gerar_numero_conta(numero):
    soma_digitos = sum(map(int, str(numero)))
    digito_verificador = soma_digitos % 10
    return f"00{numero}-{digito_verificador}"

num_conta = int(input("Digite o número da conta: "))
print("Número de conta completo:", gerar_numero_conta(num_conta))
