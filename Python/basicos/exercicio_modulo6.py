#Calculadora

while True:
    try:
        print("Escolha dois números para calcular")
        primeiro_numero = int(input("Digite o primeiro número: "))
        segundo_numero = int(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: o valor inserido não é um número inteiro")
        continue
    try:
        opcoes_menu = ["Soma", "Subtração", "Multiplicação", "Divisão"]
        menu = [f"{numero} - {operacao}" for numero, operacao in enumerate(opcoes_menu, start=1)]
        print("\n".join(menu))
        opcao = int(input("Operação: "))
        if opcao > 4 or opcao < 1:
            print("Erro: escolha uma opção disponível")
            continue
    except ValueError:
        print("Erro: o valor inserido não é um número")
        continue

    operacoes = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x * y,
        4: lambda x, y: x / y
    }
    if opcao == 4:
        while segundo_numero == 0:
            print("Erro: divisão por zero não é permitida")
            segundo_numero = int(input("Digite outro número: "))

    resultado = operacoes[opcao](primeiro_numero, segundo_numero)
    print(f"O resultado é {resultado}")
    
    denovo = input("Deseja realizar outra operação? S/N   ")
    if denovo == "N":
        print("Encerrando programa...")
        break