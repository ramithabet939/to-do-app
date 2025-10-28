import streamlit as st
import functions

def add_to_do():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("My ToDo app")
st.subheader("This is my todoapp")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox is True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()



st.text_input(label="Enter a todo: ", placeholder="Add a new todo...",
              on_change=add_to_do, key='new_todo')

