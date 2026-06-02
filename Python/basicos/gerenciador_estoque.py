produtos = {}

def adicionar_produto(produtos):
    nome = input("Nome do produto: ").strip()
    if nome in produtos:
        return "Esse produto já existe."
    else:
        qntd = int(input("Quantidade: "))
        valor = float(input("Valor (R$): "))
        produtos[nome] = {"quantidade": qntd, "preço": valor}
        return f"{nome} adicionado com sucesso!"


def listar_produtos(produtos):
    if not produtos:
        return "Nenhum produto listado."
    else:
        resultado = ["Produtos:"]
        for nome, qnt_valor in sorted(produtos.items(), key=lambda item: item[0]):
           resultado.append(f"{nome}: {qnt_valor['quantidade']} em estoque - R${qnt_valor['preço']} unid.")
        return "\n".join(resultado)


def remover_produtos(produtos):
    removido = input("Digite o nome do produto a ser removido: ")
    if removido not in produtos:
        return "Erro! O produto não existe"
    else:
        del produtos[removido]
        return f"Produto '{removido}' removido com sucesso!"


def atualizar_quantidade(produtos):
    atualizado = input("Digite o nome do produto a atualizar: ")
    if atualizado in produtos:
        qnt_atualizada = input("Digite a quantidade: ")
        produtos[atualizado]["quantidade"] = qnt_atualizada
        return "Quantidade atualizada com sucesso!"
    else:
        return "Produto não existe!"
       

def exibir_menu():
    return(
        "Menu:\n"
        "1- Adicionar produto\n"
        "2- Listar produtos\n"
        "3- Remover produto\n"
        "4- Atualizar quantidade\n"
        "5- Sair"
    )

def main():
    print("Bem vindo ao gerenciador de produtos :D")
    while True:
        print(exibir_menu())
        opcao = int(input("Escolha a ação a realizar: "))
        if opcao == 1:
            print(adicionar_produto(produtos))
        elif opcao == 2:
            print(listar_produtos(produtos))
        elif opcao == 3:
            print(remover_produtos(produtos))
        elif opcao == 4:
            print(atualizar_quantidade(produtos))
        elif opcao == 5:
            print("Saindo...\n","Obrigado por utilizar o serviço!")
            break
        else:
            print("Opção inválida! Tente novamente :P")
        
if __name__ == "__main__":
    main()
