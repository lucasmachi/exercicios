#classificador de idade

idade = int(input("Digite a idade: "))
if idade >=0 and idade <10:
    print("Counteúdo livre")
elif idade >=10 and idade <12:
    print("Counteúdo livre e para maiores de 10 anos")
elif idade >=12 and idade <14:
    print("Counteúdo livre e para maiores de 10 e 12 anos")
elif idade >=14 and idade <16:
    print("Counteúdo livre e para maiores de 10, 12 e 14 anos")
elif idade >=16 and idade <18:
    print("Counteúdo livre e para maiores de 10, 12, 14 e 16 anos")
else:
    print("Qualquer um dos tipos de conteúdo")
    