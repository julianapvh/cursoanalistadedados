emprestimos = []

def registrar_emprestimo():
    nome_material = input("Nome do material: ")
    pessoa_emprestimo = input("Nome da pessoa que fez o empréstimo: ")
    data_devolucao = input("Data de devolução prevista (dd/mm/aaaa): ")
    emprestimo = {
        "nome_material": nome_material,
        "pessoa_emprestimo": pessoa_emprestimo,
        "data_devolucao": data_devolucao
    }
    emprestimos.append(emprestimo)
    print("Empréstimo registrado com sucesso.")

def listar_emprestimos():
    print("Lista de empréstimos:")
    for emprestimo in emprestimos:
        print(f"Material: {emprestimo['nome_material']}, Pessoa: {emprestimo['pessoa_emprestimo']}, Data de devolução: {emprestimo['data_devolucao']}")

while True:
    print("Selecione uma opção:")
    print("1 - Registrar empréstimo")
    print("2 - Listar empréstimos")
    print("3 - Sair")
    opcao = input("Opção selecionada: ")

    if opcao == "1":
        registrar_emprestimo()
    elif opcao == "2":
        listar_emprestimos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")