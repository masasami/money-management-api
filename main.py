import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

# ルーター
from routers.connect_router import connect_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('ALLOW_ORIGIN')],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(connect_router)


@app.get('/')
def index():
    return {'message': 'hello'}