numeros = [1,1,2,2,3,3,4,4,5,6,6,7,7]

dicionario = {}

for i in numeros:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1

for chave,valor in dicionario.items():
    if valor == 1:
        print(chave)

