from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from uvicorn import run as RunServer

from schemas import DistributionSchema, UserSchema
from models import Base
from utils import ExceptionHandler

app = FastAPI()

Base.metadata.create_all(bind=engine)


# @app.exception_handler(ExceptionHandler)
# async def exception_handler(req: Request, exc: ExceptionHandler):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={
#             "msg": exc.error_msg
#         }
#     )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/users")
async def add_user(user: UserSchema):
    return {"message": "User Added!!", "user": user}


@app.put("/users/{id}")
async def put_user(id: int, user: UserSchema):
    return {"massage": "User Put!!!", "user": user}


@app.delete("/users/{id}")
async def delete_user(id: int):
    return {"message": "User deleted!!!"}


if __name__ == "__main__":
    RunServer('app:app', host='127.0.0.1', port=8000, reload=True, access_log=False)
