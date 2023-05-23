from fastapi import FastAPI
from database import config
from controllers import SensorController
app = FastAPI()
app.include_router(SensorController.router,prefix="/sensor/api/v1")
db = config.db
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
