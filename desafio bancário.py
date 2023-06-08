import datetime

clientes = []
contas = {}

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    global clientes
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    clientes.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(cpf, saldo_inicial=0):
    global contas
    if cpf not in [cliente['cpf'] for cliente in clientes]:
        print("CPF não cadastrado.")
        return
    if cpf in contas.keys():
        print("Conta já cadastrada para este CPF.")
        return
    contas[cpf] = {
        'saldo': saldo_inicial,
        'extrato': [],
        'saques_diarios': 0,
        'data_ultimo_saque': None
    }
    print("Conta cadastrada com sucesso!")

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(("DEPÓSITO", valor, datetime.datetime.now()))
        print("Depósito realizado com sucesso!")
        return saldo, extrato
    else:
        print("Valor de depósito inválido.")
        return saldo, extrato

def saque(*, saldo, valor, extrato, limite=500, limite_saques=3):
    global saques_diarios, data_ultimo_saque
    data_atual = datetime.date.today()

    if data_ultimo_saque != data_atual:
        saques_diarios = 0
        data_ultimo_saque = data_atual

    if saldo >= valor and saques_diarios < limite_saques and valor <= limite:
        saldo -= valor
        saques_diarios += 1
        extrato.append(("SAQUE", valor, datetime.datetime.now()))
        print("Saque realizado com sucesso!")
        return saldo, extrato
    elif saldo < valor:
        print("Saldo insuficiente.")
        return saldo, extrato
    elif saques_diarios >= limite_saques:
        print("Limite de saques diários atingido.")
        return saldo, extrato
    elif valor > limite:
        print("Limite máximo de R$ 500,00 por saque.")
        return saldo, extrato

def mostrar_extrato(saldo, *, extrato):
    print("\nEXTRATO:")
    for operacao in extrato:
        print(f"{operacao[0]}: R$ {operacao[1]:.2f} - {operacao[2].strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"\nSALDO ATUAL: R$ {saldo:.2f}")

# Restante do código...
def menu():
    print("╔══════════════════════════════╗")
    print("║                              ║")
    print("║   Selecione uma opção:       ║")
    print("║                              ║")
    print("║   1 - Cadastrar Usuário      ║")
    print("║   2 - Cadastrar Conta        ║")
    print("║   3 - Realizar Depósito      ║")
    print("║   4 - Realizar Saque         ║")
    print("║   5 - Mostrar Extrato        ║")
    print("║   0 - Sair                   ║")
    print("║                              ║")
    print("╚══════════════════════════════╝")

if __name__ == "__main__":
    while True:
        menu()
        opcao = int(input("Opção: "))

        if opcao == 0:
            print("Saindo do programa...")
            break
        elif opcao == 1:
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == 2:
            cpf = input("CPF do usuário: ")
            saldo_inicial = float(input("Saldo Inicial: "))
            cadastrar_conta(cpf, saldo_inicial)
        elif opcao == 3:
            cpf = input("CPF do usuário: ")
            valor = float(input("Valor do Depósito: "))
            if cpf in contas.keys():
                saldo = contas[cpf]['saldo']
                extrato = contas[cpf]['extrato']
                saldo, extrato = deposito(saldo, valor, extrato)
                contas[cpf]['saldo'] = saldo
                contas[cpf]['extrato'] = extrato
            else:
                print("Conta não encontrada.")
        elif opcao == 4:
            cpf = input("CPF do usuário: ")
            valor = float(input("Valor do Saque: "))
            if cpf in contas.keys():
                saldo = contas[cpf]['saldo']
                extrato = contas[cpf]['extrato']
                data_ultimo_saque = contas[cpf]['data_ultimo_saque']
                saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato,limite=500, limite_saques=3)
                contas[cpf]['saldo'] = saldo
                contas[cpf]['extrato'] = extrato
                contas[cpf]['data_ultimo_saque'] = data_ultimo_saque
            else:
                print("Conta não encontrada.")
        elif opcao == 5:
            cpf = input("CPF do usuário: ")
            if cpf in contas.keys():
                saldo = contas[cpf]['saldo']
                extrato = contas[cpf]['extrato']
                mostrar_extrato(saldo=saldo, extrato=extrato)
            else:
                    print("Conta não encontrada.")
        else:
            print("Opção inválida. Tente novamente.")
