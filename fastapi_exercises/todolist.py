from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    todo :str
    completed: bool = False
    
tasks = []
    
@app.get("/")
def welcome():
    return {"message": "want to see your to do list}!"}

@app.post("/tasks")
def add_task(task: Todo):
    tasks.append(task)
    return {"message": " task added", "task": task}

@app.get("/tasks")
def list_tasks():
    return tasks

@app.delete("/tasks/{task_id")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted", "task": task}
    raise HTTPException(status_code=404, detail="Task not found") 

@app.put("/tasks/{task_id}")
def mark_completed(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")

