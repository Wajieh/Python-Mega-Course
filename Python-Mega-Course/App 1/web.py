from func import get_todos, write_todos
import streamlit as st

def add_task():
    todo = st.session_state["new_task"]
    todos.append(todo)
    write_todos(todos)

todos = get_todos()
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is good for you. Trust me")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = todo )
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label = "", placeholder= "Add new task", on_change=add_task, key = 'new_task')
st.session_state