print("Bem vindo a calculadora :D")

def definir_operacao():
    print("Escolha a operação que deseja realizar: ")
    opcao = int(input("1- Soma, 2- Subtração, 3- Multiplicação, 4- Divisão: "))
    return opcao #retorno pra poder chamar no loop
    

def calcular(opcao):
    print("Escolha dois números")
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print(f"O resultado é {numero_1 + numero_2}")
    elif opcao == 2:
        if numero_2 < numero_1:
            print(f"O resultado é {numero_1 - numero_2}")
        else:
            print(f"O resultado é {numero_2 - numero_1}")
    elif opcao == 3:
        print(f"O resultado é {numero_1 * numero_2}")
    elif opcao == 4:
        if numero_2 == 0:
            print("Não é possível dividir por zero")
        else:
            print(f"O resultado é {numero_1 / numero_2}")
    else:
        print("Operação inválida")

while True: #colocar True faz o while virar infinito e precisar de break
    opcao = definir_operacao() #recebe o retorno la de cima
    if opcao < 1 or opcao > 4:
        print("Operação inválida")
    else:
        calcular(opcao)
        de_novo = int(input("Deseja realizar outra operação? 1- Sim, 2- Não: "))
        if de_novo == 2:
            print("Obrigado, volte sempre ;D")
            break

