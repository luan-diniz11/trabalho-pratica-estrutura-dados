tarefas = []        
estados = []        

def adicionar_tarefa(nome):
    tarefas.append(nome)
    estados.append('pendente')
    print(f"Tarefa '{nome}' adicionada com sucesso!")


def marcar_concluida(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        estados[indice] = 'concluída'
        print(f"Tarefa '{nome}' marcada como concluída!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        tarefas.pop(indice)
        estados.pop(indice)
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")


def listar_tarefas():
    if tarefas:
        print("\nLista de tarefas:")
        for i in range(len(tarefas)):
            print(f"{tarefas[i]} - {estados[i]}")
    else:
        print("Nenhuma tarefa cadastrada.")


def listar_pendentes():
    print("\nTarefas Pendentes:")
    encontrou = False
    for i in range(len(tarefas)):
        if estados[i] == 'pendente':
            print(tarefas[i])
            encontrou = True
    if not encontrou:
        print("Não há tarefas pendentes.")


def listar_concluidas():
    print("\nTarefas Concluídas:")
    encontrou = False
    for i in range(len(tarefas)):
        if estados[i] == 'concluída':
            print(tarefas[i])
            encontrou = True
    if not encontrou:
        print("Não há tarefas concluídas.")


def pesquisar_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        print(f"Tarefa '{nome}' encontrada. Estado: {estados[indice]}")
    else:
        print(f"Tarefa '{nome}' não encontrada.")


def menu():
    while True:
        print("\nMenu de Gerenciamento de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Marcar Tarefa como Concluída")
        print("3. Remover Tarefa")
        print("4. Listar Tarefas")
        print("5. Listar Tarefas Pendentes")
        print("6. Listar Tarefas Concluídas")
        print("7. Pesquisar Tarefa")
        print("8. Sair")
        
        opcao = input("Escolha uma opção (1-8): ")

        if opcao == '1':
            nome = input("Digite o nome da tarefa: ")
            adicionar_tarefa(nome)
        elif opcao == '2':
            nome = input("Digite o nome da tarefa a ser marcada como concluída: ")
            marcar_concluida(nome)
        elif opcao == '3':
            nome = input("Digite o nome da tarefa a ser removida: ")
            remover_tarefa(nome)
        elif opcao == '4':
            listar_tarefas()
        elif opcao == '5':
            listar_pendentes()
        elif opcao == '6':
            listar_concluidas()
        elif opcao == '7':
            nome = input("Digite o nome da tarefa a ser pesquisada: ")
            pesquisar_tarefa(nome)
        elif opcao == '8':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
