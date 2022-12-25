from TodoBackend import cursor, db
def gettables():
    cursor.execute("use todoapp")
    show=("show tables")
    cursor.execute(show)
    tables=cursor.fetchall()
    return tables

def GetAllTodos():
    cursor.execute("use todoapp")
    selectQuery = ("select * from todos order by created_on desc")
    cursor.execute(selectQuery)
    todos = cursor.fetchall()
    return todos

def AddTodo(todo):
    cursor.execute("use todoapp")
    insertQuery = ("insert into todos(todo) values(%s)")
    cursor.execute(insertQuery, (todo,))
    db.commit()
    todoId = cursor.lastrowid
    return f'Added Todo with Id: {todoId} and Todo: {todo}'

def UpdateTodo(id, todo):
    cursor.execute("use todoapp")
    query = ("update todos set todo = %s  where id = %s")
    cursor.execute(query, (todo, id,))
    db.commit()
    return "Update Todo"

def GetTodo(id):
    cursor.execute("use todoapp")
    query = ("select * from todos where id = %s")
    cursor.execute(query, (id,))
    todo = cursor.fetchone()
    return todo

def DeleteTodo(id):
    cursor.execute("use todoapp")
    query = ("delete from todos where id = %s")
    cursor.execute(query, (id,))
    db.commit()
    return "Todo deleted successfully"

# DeleteTodo(9)
# DeleteTodo(10)
