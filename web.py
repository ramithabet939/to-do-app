import streamlit as st

st.title("My To-Do App")
st.subheader("Personal task tracker")
st.write("This app helps you stay productive — your todos stay private in your browser session.")

# Initialize todos for this session only
if "todos" not in st.session_state:
    st.session_state.todos = []

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        st.session_state.todos.append(todo)
        st.session_state["new_todo"] = ""  # clear input

# Add todos
st.text_input("Enter a new todo:", key="new_todo", on_change=add_todo)

# Display todos
for i, todo in enumerate(st.session_state.todos):
    checkbox = st.checkbox(todo, key=f"todo_{i}")
    if checkbox:
        st.session_state.todos.pop(i)
        st.rerun()
