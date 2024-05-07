from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: str = None  # Optional description
    completed: bool = False

@app.post("/todos")
async def create_todo(text: str = Body(...)):
    global todo_id, todos
    new_todo = {"id": todo_id, "text": text}
    todos.append(new_todo)
    todo_id += 1
    return new_todo

@app.get("/todos")
async def get_todos():
    return todos

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, text: str = Body(...)):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[i]["text"] = text
            return todos[i]
    return {"error": "Todo not found"}
    
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    global todos
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            del todos[i]
            return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}
