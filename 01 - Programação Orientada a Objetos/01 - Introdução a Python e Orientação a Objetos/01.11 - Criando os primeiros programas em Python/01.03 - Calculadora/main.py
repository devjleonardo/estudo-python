def bem_vindo():
    print("******************************************")
    print("      Calculadora simples em Python       ")
    print("******************************************")
    calcular()


def calcular():
    print("\nQual operação deseja executar? (1) Soma (2) Subtração (3) Multiplicação (4) Divisão 5 (outra)")
    operacao = int(input("Digite a operação a ser realizada: "))

    if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
        print("Desculpe, esta calculadora não suporta outras operações. Por favor, execute o programa novamente")
        return

    primeiro_numero = int(input("Digite o primeiro número: "))
    segundo_numero = int(input("Digite o segundo número: "))

    if operacao == 1:
        print("O resultado é", primeiro_numero + segundo_numero)
    if operacao == 2:
        print("O resultado é", primeiro_numero - segundo_numero)
    if operacao == 3:
        print("O resultado é", primeiro_numero * segundo_numero)
    if operacao == 4:
        print("O resultado é", primeiro_numero / segundo_numero)

    calcular_outra_vez()


def calcular_outra_vez():
    outra_vez = input("Deseja realizar outra operação? Por favor, Digite S para SIM ou N para NÃO: ")

    if outra_vez == "S":
        calcular()
    elif outra_vez == "N":
        print("Até a próxima!")
    else:
        print("Opção inválida")
        calcular_outra_vez()
