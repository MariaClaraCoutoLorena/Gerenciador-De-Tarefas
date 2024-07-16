import tasks_functions

tasks = []
while True:
    print("\n\tBem vindo ao menu da sua Lista de Tarefas:\n")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Renomear tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa.")
    print("6. Deletar todas as tarefas completadas")
    print("7. Sair\n")
    try:
        option = int(input("Digite a opção que gostaria de realizar: "))
    except:
        print("Opção inválida!")
        continue

    match option:

        case 2:
            task_name = input("Digite o nome da tarefa a ser adicionada: ")
            tasks_functions.add_task(tasks,task_name)
            print("Tarefa adicionada com sucesso, você será redirecionado ao menu!\n")
        case 6:
            break
        
        case _:
            continue

    