import uvicorn
from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel, constr, field_validator, ValidationError

app = FastAPI()


class Task(BaseModel):
    # pattern = r"^[a-zA-Z0-9_]+$",
    name: constr(min_length=2)
    describe: constr(min_length=5, max_length=20)
    id: int
    status: str

    @field_validator('status')
    @classmethod
    def check_status(cls, status):
        if status not in ['open','close']:
            raise HTTPException(status_code=400, detail="status must be open/close")
        return status


tasks = {}


@app.get("/taskes")
async def showTasks():
    if len(tasks)<0:
        return f"no found tasks"
    return f" {tasks}"

def check_input(id: int):
    return tasks[id];

@app.post("/task/")
async def add_task(task: Task):
    try:
        tasks[task.id]=task.dict()
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"hello {task.name}"

@app.put("/task/")
async def updateTaskById(task: Task):
    try:
        tasks[task.id] = task.dict()
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"update {task.id} and tasks={tasks}"

@app.delete("/task/{taskid}/")
async def DeleteTaskById(taskid:int):
    try:
        del tasks[taskid]
    except:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"delete {taskid}"

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
