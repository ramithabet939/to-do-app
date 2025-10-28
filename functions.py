def get_todos(filepath="todos.txt"):
    """
    read a text file and return a list of the todos
    """
    with open(filepath,"r") as file_local:
        data = file_local.readlines()
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath="todos.txt"):
    """
    write a list of todos to a text file

    """

    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

