tarefas = {}

def ultimaPos():
    if tarefas:
        return max(tarefas.keys())
    return 0

while True:
    print("1. Agregar tarefa")
    print("2. Ver tarefas")
    print("3. Eliminar tarefa")
    print("4. Procurar Tarefa Específica")
    print("5. Sair")
    escolha = int(input(' >> '))

    if escolha == 1:
        tarefa = input("Digite a tarefa: ")
        tarefas[ultimaPos() + 1] = tarefa
        print("Tarefa adicionada com sucesso!")

    elif escolha == 2:
        if tarefas:
            for i, o in tarefas.items():
                print(f" {i} : {o} ")

    elif escolha == 3:
        if tarefas:
                tarefa = int(input("Digite o número da tarefa que deseja excluir: "))
                if tarefa in tarefas:
                    del tarefas[tarefa]
                    print("tarefa excluida com sucesso!")
                else:
                    print("nmero da tarefa não encontrado.")
        else:
            print("n tem tarefas para excluir.")

    elif escolha == 4:
        if tarefas:
                tarefa = int(input("Digite o número da tarefa que deseja procurar: "))
                if tarefa in tarefas:
                    print(f"tarefa {tarefa} : {tarefas[tarefa]}")
                else:
                    print("unmero da tarefa não encontrado.")

    elif escolha == 5:
        print("Saindo...")
        break




    