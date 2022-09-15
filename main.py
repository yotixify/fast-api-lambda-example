from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def hello_world_read():
    return {"Hello": "World"}

handler = Mangum(app)