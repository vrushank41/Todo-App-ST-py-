import streamlit as st
from TodoApi import AddTodo, GetAllTodos, GetTodo, DeleteTodo, UpdateTodo, gettables

def gettablesUI():
    tables=gettables()
    st.subheader("Select Tables")
    selected=st.selectbox("Select",tables)
    st.info(selected)


def AddTodoUI():
    todo = st.text_input(label="Todo", placeholder="Todo")
    if st.button("Add Todo"):
        res = AddTodo(todo)
        st.success(res)

def GetAllTodosUI(todos):
    st.subheader('All Todos')
    for index, todo in enumerate(todos):
        st.write(f'{index+1}. {todo[1]}')

def DeleteTodoUI():
    todos = GetAllTodos()
    todo_text = [todo[1] for todo in todos]
    selected = st.multiselect("Delete Todos", todo_text)
    if st.button("Delete"):
        for todo in todos:
            if todo[1] in selected:
                st.balloons()
                st.success(DeleteTodo(todo[0]))
                todos = GetAllTodos()

def UpdateTodoUI():
    todos = GetAllTodos()
    todo_text = [todo[1] for todo in todos]
    selected = st.selectbox("Update Todo", todo_text)
    edit_todo = st.text_input(label="Edit Todo", placeholder="Edit Todo", value= selected)
    if st.button("Edit Todo"):
        for todo in todos:
            if todo[1] == selected:
                st.success(UpdateTodo(todo[0], edit_todo))
                todos = GetAllTodos()

def GetTodoUI():
    todo_id = st.number_input(label = "Get Todo By Id", min_value=1, step=1)
    if st.button("Get Todo"):
        res = GetTodo(todo_id)
        if res:
            st.info(res[1])
        else:
            st.warning("No Todo found with given Id: {}".format(todo_id))
            
    


st.title("Todo Listing")
st.subheader("List day to day tasks here")

activeWindow = st.sidebar.radio("Menu", ["All Todos", "Add Todo", "Update Todo", "Delete Todo", "Get Todo","Show Tables"], index = 0)

if activeWindow == "Add Todo":
    AddTodoUI()
    # st.write(AddTodo())
elif activeWindow == "Update Todo":
    # st.write(UpdateTodo())
    UpdateTodoUI()
elif activeWindow == "Delete Todo":
    DeleteTodoUI()
elif activeWindow == "Get Todo":
    GetTodoUI()
elif activeWindow == "Show Tables":
    gettablesUI()
else:
    # st.write(GetAllTodos())
    GetAllTodosUI(GetAllTodos())