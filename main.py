
# ルーター
from routers.connect_router import connect_router
from routers.account_router import account_router
from routers.tag_router import tag_router
from routers.session_router import session_router

# ライブラリ
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('ALLOW_ORIGIN')],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(connect_router)
app.include_router(account_router)
app.include_router(tag_router)
app.include_router(session_router)
