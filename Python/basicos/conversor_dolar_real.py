#conversor dolar real

cotacao_dolar = 0
valor_real = 0
valor_dolar = 0
opcao = 0
print("Vamos converter o valor do dólar para real ou vice-versa")
opcao = int(input("Se deseja converter dólar para real digite 1, se deseja converter real para dólar digite 2: "))  
cotacao_dolar = float(input("Digite a cotação do dólar: "))

if opcao == 1:
    valor_dolar = float(input("Vamos converter dólar para real. Digite o valor em dólares: "))
    print("O valor em dólares inserido é", valor_dolar)
    valor_real = valor_dolar * cotacao_dolar
    print("O valor convertido para real é", valor_real)
elif opcao == 2:
    valor_real = float(input("Vamos converter real para dólar. Digite o valor em reais: "))
    print("O valor em reais inserido é", valor_real)
    valor_dolar = valor_real / cotacao_dolar
    print("O valor convertido para dólar é", valor_dolar)
else:
    print("Opção inválida. Por favor, escolha 1 para dólar para real ou 2 para real para dólar.")


