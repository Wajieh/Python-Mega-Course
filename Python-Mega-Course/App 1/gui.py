from func import get_todos, write_todos
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

sg.theme('DarkPurple4')
clock = sg.Text('',key="clock")
label = sg.Text("Type in a to-do",size=(46,1))
input_box = sg.InputText(tooltip="enter a to-do",key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit",size=(8))
completed_button = sg.Button("Complete")
close_button = sg.Button("Close",size=(8))
listbox = sg.Listbox(values=get_todos(),key="todos",
                    enable_events=True,size=(44,10))
window=sg.Window("My To Do App",
                 layout=[[clock],[label],[input_box,add_button],[listbox],[edit_button,completed_button,close_button]],
                 font=("Helvetica",15))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime('%A, %d %B %Y %H:%M:%S'))
    if sg.WIN_CLOSED or event == "Close":
        break
    elif event == "Add":
        try:
            todo = values["todo"]
            if not todo:
                raise ValueError
            todos = get_todos()
            todos.append(todo)
            write_todos(todos)
            sg.popup(f"{todo} added to your to-do list")
            window["todos"].update(values=todos)
        except ValueError:
            sg.popup("Enter a to-do")
    
    elif event == "Edit":
        try:
            todos =get_todos()
            to_edit = values["todos"][0]
            index = todos.index(to_edit)
            new_todo = sg.popup_get_text("Enter the new to-do",default_text=to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["todos"].update(values=todos)
        except IndexError:
            sg.popup("Select a to-do to edit")

    elif event == "todos":
        todos = get_todos()
        to_do = values["todos"][0]
        window["todo"].update(value=to_do)
            
    elif event == "Complete":
        try:
            todos =get_todos()
            to_complete = values["todos"][0]
            todos.pop(todos.index(to_complete))
            write_todos(todos)
            window["todos"].update(values=todos)
        except IndexError:
            sg.popup("Select a to-do to complete")
    

window.close()