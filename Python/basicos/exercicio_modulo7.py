livros = {}
emprestimo = []

#colocar pra tudo virar minuscula


def adicionar_livro(livros):
    nome = str(input("Digite o nome do livro: ")).strip().upper()
    if nome in livros:
        return "O exemplar já foi adicionado."
    else:
        qntd = int(input("Quantidade: "))
        autor = str(input("Autor: ")).upper()
        livros[nome] = {"quantidade": qntd, "autor": autor}
        return f"{nome} adicionado com sucesso!"
    
def listar_livro(livros):
    if not livros:
        return "Nenhum exemplar existente na base."
    else:
        resultado = ["Exemplares:"]
        for nome, qnt_autor in sorted(livros.items(), key=lambda item: item[0]):
           resultado.append(f"{nome} - {qnt_autor['autor']} - {qnt_autor['quantidade']} exemplares cadastrados")
        return "\n".join(resultado)
    
def remover_livro(livros):
    removido = str(input("Digite o nome do livro a ser removido: ")).upper()
    if removido not in livros:
        return "Erro! O livro não está cadastrado"
    else:
        del livros[removido]
        return f"Exemplar '{removido}' removido com sucesso!"
    
def atualizar_quantidade(livros):
    atualizado = str(input("Digite o nome do livro a atualizar: ")).upper()
    if atualizado in livros:
        qnt_atualizada = int(input("Digite a quantidade: "))
        livros[atualizado]["quantidade"] = qnt_atualizada
        return "Quantidade atualizada com sucesso!"
    else:
        return "Produto não existe!"
    
def registrar_emprestimo(livros):
    titulo = str(input("Digite o título do livro que deseja emprestar: ")).upper()
    quantia = int(input("Digite quantos exemplares deseja emprestar: "))
    if titulo not in livros:
        return "Erro! Esse livro não foi cadastrado"
    else:
        if quantia <= livros[titulo]["quantidade"]:
            livros[titulo]["quantidade"] -= quantia
            emprestimo.append((titulo, quantia))         
            return f"Empréstimo de {quantia} exemplar(es) de '{titulo}' registrado!"
        else:
            return f"Não temos {quantia} exemplares disponíveis para empréstimo"

def historico():
    if not emprestimo:
        return "Nenhum empréstimo registrado"
    resultado = ["Histórico de empréstimos:\n"]
    for titulo, quantia in emprestimo:
        resultado.append(f"'{titulo}' - {quantia} exemplar(es)")
    return "\n".join(resultado)

def exibir_menu():
    return(
        "Menu:\n"
        "1- Adicionar livro\n"
        "2- Listar livros\n"
        "3- Remover livro\n"
        "4- Atualizar quantidade\n"
        "5- Registrar empréstimo\n"
        "6- Histórico de empréstimos\n"
        "7- Sair"
    )

def main():
    print("Bem vindo(a) a biblioteca :D")
    while True:
        print(exibir_menu())
        opcao = int(input("Escolha a ação a realizar: "))
        if opcao == 1:
            print(adicionar_livro(livros))
        elif opcao == 2:
            print(listar_livro(livros))
        elif opcao == 3:
            print(remover_livro(livros))
        elif opcao == 4:
            print(atualizar_quantidade(livros))
        elif opcao == 5:
            print(registrar_emprestimo(livros))
        elif opcao == 6:
            print(historico())
        elif opcao == 7:
            print("Saindo...\n","Obrigado por utilizar o serviço!")
            break
        else:
            print("Opção inválida! Tente novamente :P")
        
if __name__ == "__main__":
    main()