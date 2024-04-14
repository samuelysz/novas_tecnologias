def apagar_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato apagado com sucesso.")
    else:
        print("Contato não encontrado na agenda.")

def alterar_contato(agenda, nome):
    if nome in agenda:
        print("Por favor, insira os novos dados do contato:")
        novo_nome = input("Novo nome: ")
        novo_telefone = input("Novo telefone: ")
        nova_data_aniversario = input("Nova data de aniversário (DD/MM/AAAA): ")
        novo_email = input("Novo email: ")
        agenda[novo_nome] = {'telefone': novo_telefone, 'data_aniversario': nova_data_aniversario, 'email': novo_email}
        del agenda[nome]
        print("Contato alterado com sucesso.")
    else:
        print("Contato não encontrado na agenda.")

def listar_nomes(agenda):
    for i, nome in enumerate(agenda.keys(), 1):
        print(f"{i}. Nome: {nome}")

def buscar_contato(agenda, nome):
    if nome in agenda:
        contato = agenda[nome]
        print(f"Nome: {nome}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Data de Aniversário: {contato['data_aniversario']}")
        print(f"Email: {contato['email']}")
    else:
        print("Contato não encontrado na agenda.")

def gravar_agenda(agenda, arquivo):
    with open(arquivo, 'w') as f:
        for nome, contato in agenda.items():
            f.write(f"{nome},{contato['telefone']},{contato['data_aniversario']},{contato['email']}\n")
    print("Agenda gravada com sucesso.")

def menu():
    print("----- MENU -----")
    print("1. Adicionar contato")
    print("2. Apagar contato")
    print("3. Alterar contato")
    print("4. Listar contatos")
    print("5. Buscar contato")
    print("6. Gravar agenda")
    print("7. Exibir tamanho da agenda")
    print("8. Ordenar agenda por nome")
    print("9. Sair")

def main():
    agenda = {}
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            if nome in agenda:
                print("Erro: Já existe um contato com esse nome.")
                continue
            telefone = input("Telefone: ")
            data_aniversario = input("Data de aniversário (DD/MM/AAAA): ")
            email = input("Email: ")
            agenda[nome] = {'telefone': telefone, 'data_aniversario': data_aniversario, 'email': email}
        elif opcao == '2':
            nome = input("Nome do contato a ser apagado: ")
            apagar_contato(agenda, nome)
        elif opcao == '3':
            nome = input("Nome do contato a ser alterado: ")
            alterar_contato(agenda, nome)
        elif opcao == '4':
            listar_nomes(agenda)
        elif opcao == '5':
            nome = input("Nome do contato a ser buscado: ")
            buscar_contato(agenda, nome)
        elif opcao == '6':
            arquivo = input("Digite o nome do arquivo para gravar a agenda: ")
            gravar_agenda(agenda, arquivo)
        elif opcao == '7':
            print(f"Tamanho da agenda: {len(agenda)} contatos.")
        elif opcao == '8':
            agenda = dict(sorted(agenda.items()))
            print("Agenda ordenada por nome.")
        elif opcao == '9':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
