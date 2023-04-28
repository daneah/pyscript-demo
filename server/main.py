from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/client", StaticFiles(directory="client"), name="client")


@app.get("/")
async def root():
    return FileResponse("index.html")
