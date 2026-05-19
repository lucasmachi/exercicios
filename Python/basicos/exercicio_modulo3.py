# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(tarefas):
    nome = input("Nome da tarefa: ").strip()
    if nome in tarefas:
        return "Essa tarefa já existe."
    else:
        tarefas[nome] = False
        return f"Tarefa '{nome}' adicionada com sucesso!"

def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = ["Tarefas:"]
        for nome, status in sorted(tarefas.items(), key=lambda item: item[0]):
            emoji = "✅ Concluída" if status else "❌ Não concluída"
            resultado.append(f"{nome}: {emoji}")
        return "\n".join(resultado)

def remover_tarefa(tarefas):
    nome = input("Nome da tarefa: ").strip()
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(tarefas):
    nome = input("Nome da tarefa: ").strip()
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    else:
        return "Erro: Tarefa não encontrada."

def exibir_menu():
    return (
        "Menu:\n"
        "1 - Adicionar tarefa\n"
        "2 - Listar tarefas\n"
        "3 - Remover tarefa\n"
        "4 - Marcar tarefa como concluída\n"
        "5 - Sair"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Opção: ").strip()

        if opcao == "1":
            print(adicionar_tarefa(tarefas))
        elif opcao == "2":
            print(listar_tarefas(tarefas))
        elif opcao == "3":
            print(remover_tarefa(tarefas))
        elif opcao == "4":
            print(marcar_concluida(tarefas))
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()