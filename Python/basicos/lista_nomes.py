#Construindo uma lista de até 100 nomes

lista = ["vazio"] * 100
cont = 0 

resposta = input("Deseja preencher a lista? (s/n)")

while resposta == "s" or resposta == "S":
    nome = input("Digite um nome:")
    lista[cont] = nome
    cont += 1
    resposta = input("Deseja continuar preenchendo a lista? (s/n)")

print(f"A lista possui {cont} nomes:")
for nome in lista:
    if nome != "vazio":
     print(nome)



