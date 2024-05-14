from fastapi import FastAPI
from models import Todo



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# get all todos

@app.get("/todos/{todo-id}")
async def get_todos():
    return {"todos": todos}

# get single todo

@app.get("/todos")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo":todo}
    return {"message": "No todos found"}

# create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "todo has been added"}
# update a todo

# delete a todo