import datetime

saldo = 0
extrato = []
saques_diarios = 0
data_ultimo_saque = None


def deposito(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(("DEPÓSITO", valor, datetime.datetime.now()))
        print("Depósito realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")


def saque(valor):
    global saldo, extrato, saques_diarios, data_ultimo_saque
    data_atual = datetime.date.today()

    if data_ultimo_saque != data_atual:
        saques_diarios = 0
        data_ultimo_saque = data_atual

    if saldo >= valor and saques_diarios < 3 and valor <= 500:
        saldo -= valor
        saques_diarios += 1
        extrato.append(("SAQUE", valor, datetime.datetime.now()))
        print("Saque realizado com sucesso!")
    elif saldo < valor:
        print("Saldo insuficiente.")
    elif saques_diarios >= 3:
        print("Limite de saques diários atingido.")
    elif valor > 500:
        print("Limite máximo de R$ 500,00 por saque.")


def mostrar_extrato():
    print("\nEXTRATO:")
    for operacao in extrato:
        print(f"{operacao[0]}: R$ {operacao[1]:.2f} - {operacao[2].strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"\nSALDO ATUAL: R$ {saldo:.2f}")


def menu():
    print("╔══════════════════════════════╗")
    print("║                              ║")
    print("║   Selecione uma opção:       ║")
    print("║                              ║")
    print("║   1 - Depósito               ║")
    print("║   2 - Saque                  ║")
    print("║   3 - Extrato                ║")
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
            valor = float(input("Informe o valor do depósito: "))
            deposito(valor)
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            saque(valor)
        elif opcao == 3:
            mostrar_extrato()
        else:
            print("Opção inválida. Tente novamente.")
