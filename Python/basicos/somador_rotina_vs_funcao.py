
def somar_rotina(a, b):
    print(f"{a} + {b} =", a + b) 

def somar_funcao(a, b):
    return a + b

vezes = int(input("Quantas vezes quer somar? "))

for i in range(vezes):
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))

    print("-- Rotina:")
    somar_rotina(a, b)

    print("-- Função:")
    resultado = somar_funcao(a, b)
    print(f"{a} + {b} =", resultado)

    print()
