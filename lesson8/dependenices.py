import uvicorn as uvicorn
from fastapi import FastAPI, Depends,HTTPException
from pydantic import BaseModel, constr, ValidationError

app = FastAPI()


def isPositive(num: int):
    if num > 0:
        return num * 2
    return None


@app.get("/double-of-number/")
async def get_num(num: int = Depends(isPositive)):
    if num is not None:
        return num
    else:
        raise HTTPException(status_code=422, detail="oops... not valid value")


if __name__ == '__main__':
    uvicorn.run("dependencies:app", host='127.0.0.1', port=5000)