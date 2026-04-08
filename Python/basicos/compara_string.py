#Verificar se duas strings são iguais, e repetir o processo até que sejam

while True:
    frase1 = input("Digite uma frase:")
    frase2 = input("Digite outra frase:")
    if frase1 == frase2:
        print("As frases são iguais.")
        break
    else:
        print("As frases são diferentes. Tente novamente.")