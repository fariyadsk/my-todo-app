FILEPATH = "todos.txt"
def get_todods(filepath=FILEPATH):
    with open (filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, filepath=FILEPATH):
    with open (filepath, "w") as file_local:
        file_local.writelines(todos_list)
