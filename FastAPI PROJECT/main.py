from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Database - memory mein
todos = [
]

# Model
class Todo(BaseModel):
    title: str
    completed: bool = False

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

# 1. Saari tasks lene ke liye
@app.get("/todos")
def get_todos():
    return todos

# 2. ID se 1 task lene ke liye - Yahan masla tha
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id: # <-- int se int compare ho raha hai
            return todo
    raise HTTPException(status_code=404, detail="No found task")

# 3. Nayi task banane ke liye
@app.post("/todos")
def create_todo(todo: Todo):
    new_id = len(todos) + 1
    new_todo = {"id": new_id, "title": todo.title, "completed": todo.completed}
    todos.append(new_todo)
    return new_todo

# 4. Task update karne ke liye
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for i, t in enumerate(todos):
        if t["id"] == todo_id:
            todos[i] = {"id": todo_id, "title": todo.title, "completed": todo.completed}
            return todos[i]
    raise HTTPException(status_code=404, detail="No found task")

# 5. Task delete karne ke liye
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t["id"] == todo_id:
            return todos.pop(i)
    raise HTTPException(status_code=404, detail="No found task")