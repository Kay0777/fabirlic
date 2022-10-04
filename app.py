from fastapi import FastAPI, Request, Response, Header
from fastapi.responses import JSONResponse, StreamingResponse

from uvicorn import run as RunServer

from schemas import DistributionSchema, UserSchema
from models import Base
from utils import ExceptionHandler
from pathlib import Path

from os import getcwd, path

app = FastAPI()

VIDEO_PATH = Path("video.mp4")

# Base.metadata.create_all(bind=engine)


@app.exception_handler(ExceptionHandler)
async def exception_handler(req: Request, exc: ExceptionHandler):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "msg": exc.error_msg
        }
    )


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


@app.get("/video1")
async def video_streaming(start: str, end: str = None):
    start = int(start)
    end = int(end) if end else start + 1024*1024
    with open(VIDEO_PATH, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(VIDEO_PATH.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")

@app.get("/video/{filename}")
async def video_streaming(filename: str, range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(start + 1024 * 1024)

    file = f"{getcwd()}/{filename}"

    with open(file, "rb") as myfile:
        myfile.seek(start)
        data = myfile.read(end - start)
        video_size = str(path.getsize(file))

        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{video_size}',
            'Accept-Ranges': 'bytes'
        }
        return Response(content=data, status_code=206, headers=headers, media_type="video/mp4")

if __name__ == "__main__":
    RunServer('app:app', host='127.0.0.1', port=8000, reload=True, access_log=False)
