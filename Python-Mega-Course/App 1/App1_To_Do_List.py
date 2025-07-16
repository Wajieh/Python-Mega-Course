def add():
    task = input("Enter your task: ") + "\n"
    with open("to_do_list.txt",'r') as file:
              print("file read...")
              todos = file.readlines()
    todos.append(task)
    with open("to_do_list.txt",'w') as file:
              print("file write...")
              file.writelines(todos)

def show():
    with open("to_do_list.txt",'r') as file:
        print("file read...")
        todo_list = file.readlines()
    for i, item in enumerate(todo_list):
        item = item.strip().title()
        
        print(f"{i + 1}- {item}")

def edit():
    try: 
        edit_num = int(input("Which task you want to edit: "))
        edit_num -= 1
        with open("to_do_list.txt",'r') as file:
            print("file read...")
            todo_list = file.readlines()

        new_task = input("Enter the new modified task: ")
        todo_list[edit_num] = new_task + "\n"
        with open("to_do_list.txt",'w') as file:
                    print("file write...")
                    file.writelines(todo_list)
    except IndexError:
        print("Error in Prompt.")

def complete():
     num = int(input("Enter the number of the task you have completed: "))
     num -= 1
     with open("to_do_list.txt",'r') as file:
        print("file read...")
        todo_list = file.readlines()

     todo_list.pop(num)
     with open("to_do_list.txt",'w') as file:
        print("file write...")
        file.writelines(todo_list)

todos = []
while True:
    choice = input("Enter what you want to do: ")
    choice = choice.strip().lower()   

    match choice:
        case "add": add()
        case "show": show()
        case "edit": edit()
        case "complete": complete()
        case "exit":
            break
        case _:
            print("Error, choose the correct action from the following: add / edit / complete / show / exit")

