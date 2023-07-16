def menu():
    menu = """
    [c] Cadastrar Cliente
    [b] Cadastrar Conta Bancária
    [d] Depositar
    [s] Sacar
    [e] Exibir Extrato
    [q] Sair 
    => """
    return input(menu)

def depositar(saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")

    return saldo, extrato

def sacar(*, saldo, valor, limite, numero_saques, extrato, limite_saques):
    if limite_saques <= 3:
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("========MOVIMENTAÇÃO BANCÁRIA - EXTRATO========")
    print(extrato)
    print("-----------------------------------------------")
    print(f"Saldo: {saldo:.2f}")
    print("===============================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado")
        return

    nome = input("Nome completo ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço (logradouro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Cadastro efetuado com sucesso.")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta cadastrada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Erro ao cadastrar conta.")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor para depositar: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                limite=limite,
                numero_saques=numero_saques,
                extrato=extrato,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "c":
            criar_usuario(usuarios)

        elif opcao == "b":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()