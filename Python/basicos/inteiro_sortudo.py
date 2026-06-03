numeros = [1, 1, 2, 2, 3, 4, 5, 6, 7]

numeros_dic = {}

for i in numeros:
    if i not in numeros_dic:
        numeros_dic[i] = 1
    else:
        numeros_dic[i] += 1

for chave, valor in numeros_dic.items():
    if chave == valor:
        print(chave)