from fastapi import FastAPI

# ルーター
from routers.connect_router import connect_router

app = FastAPI()

app.include_router(connect_router)


@app.get('/')
def index():
    return {'message': 'hello'}