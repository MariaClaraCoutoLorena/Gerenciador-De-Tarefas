def add_task(tasks: list, task_name: str):
    task = {}
    task["nome"] = task_name
    task["status"] = "Incompleta"
    tasks.append(task)

def view_tasks(tasks:list):
    print("\tSua lista de tarefas\n")
    for i, task in enumerate(tasks,start=1):
        print(f'{i}. {task["nome"]}: {task["status"]}')

def rename_task(tasks:list):
    print("\tSua lista de tarefas\n")
    for i, task in enumerate(tasks,start=1):
        print(f'{i}. {task["nome"]}: {task["status"]}')
    task_num = int(input("Digite o número da tarefa que gostaria de renomear: "))
    try:
        valid = tasks[task_num-1]["nome"]
        task_name = input("\nDigite o novo nome: ")
        tasks[task_num-1]["nome"] = task_name
    except:
        print("Parece que você escolheu uma tarefa inexistente para renomear.")
    