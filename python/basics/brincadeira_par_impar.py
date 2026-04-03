#brincadeira impar par

print("Escolha P para par ou I para ímpar:")
escolha=input()

if escolha=="P":
    print("Você escolheu par")
elif escolha=="I":
    print("Você escolheu impar")
else:
    print("Escolha inválida")

num_user = int(input("Agora digite um número de 1 a 10 de acordo com sua escolha:"))
import random
num_pc = random.randint(1,10)
print("O número do computador é:", num_pc)

soma = num_user + num_pc
print("A soma dos números é:", soma)

if soma % 2 == 0 and escolha == "P":
    print("A soma é par, você venceu!")
elif soma % 2 == 0 and escolha == "I":
    print("A soma é par, o computador venceu!")
elif soma % 2 == 1 and escolha == "I":
    print("A soma é impar, você venceu!")
elif soma % 2 == 1 and escolha == "P":
    print("A soma é impar, o computador venceu!")


