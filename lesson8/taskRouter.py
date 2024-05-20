from fastapi import FastAPI, Depends, APIRouter, HTTPException
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from fastapi.encoders import jsonable_encoder


task_router = APIRouter()


class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    description: str
    id: int
    status: str

    @field_validator('status')
    def check_status(cls, status):
        if status not in ["open", "close"]:
            raise ValueError('error in status')
        return status


tasks = {}


@task_router.get("/tasks")
async def get_Tasks():
    if not tasks:
        raise ValueError('error the array tasks is empty')
    return tasks

@task_router.post("/task/")
async def add_Task(task: Task):
    try:
        print("not dict", task)
        print(" dict", task.dict())

        tasks.append(task.dict())
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return task


@task_router.delete("/tasks/{id}")
async def deleteTask(id: int):
    try:
        global tasks
        tasks = [task for task in tasks if task['id'] != id]
    except Exception as e:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return "Task deleted successfully"




@task_router.put("/task/{task_id}")
async def update_task(task_id: int, task: Task):
    global tasks
    for t in tasks:
        if t['id'] == task_id:
            t.update(task.dict())
            return {"message": "Task updated successfully"}
    raise HTTPException(status_code=404, detail="oops... an error occurred")