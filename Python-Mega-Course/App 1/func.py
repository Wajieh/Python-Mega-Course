
def get_todos(file_path="to_do_list.txt"):
    with open(file_path, "r") as file:
        todos = file.readlines()
    for i in range(len(todos)):
        todos[i] = todos[i][:-1]
    return todos

def write_todos(todos,file_path="to_do_list.txt"):
    with open(file_path, "w") as file:
        for todo in todos:
            file.write(f"{todo}\n")

