#Verificar múltiplos

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))

if num1 == num2:
    print("Os números não podem ser iguais")
elif num1 % num2 == 0:
    print("O número", num1, "é múltiplo de", num2)
elif num2 % num1 == 0:
    print("O número", num2, "é múltiplo de", num1)
else:
    print("Os números não são múltiplos")