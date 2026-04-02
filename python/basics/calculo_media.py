#calculo de média de alunos

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print("A média do aluno é:", media)

if media >=0 and media <6:
    print("O aluno está reprovado.")
elif media >= 6 and media <8:
    print("O aluno está de recuperação.")
else:
    print("O aluno está aprovado.")