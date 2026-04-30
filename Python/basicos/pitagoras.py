#Teorema de pitágoras

print("Esse programa recebe 3 valores e verifica se podem formar um triângulo retângulo")

hipotenusa = float(input("Digite um valor para a hipotenusa: "))
cateto1 = float(input("Digite um valor para o cateto 1: "))
cateto2 = float(input("Digite um valor para o cateto 2: "))

if hipotenusa * hipotenusa == (cateto1 * cateto1) + (cateto2 * cateto2):
    print("Os valores formam um triângulo retângulo :D")
else:
    print("Os valores não formam um triângulo retângulo :C")
    