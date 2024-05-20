import string
from http.client import HTTPException
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from starlette.staticfiles import StaticFiles

from taskRouter import task_router
from userRouter import user_router
app = FastAPI()

app.include_router(task_router, prefix='./tasks')
app.include_router(user_router, prefix='./users')
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("Sample:app", host="127.0.0.1",
                port=8000, reload=True)
