from fastapi import APIRouter
from modules.db import DB

connect_router = APIRouter()

@connect_router.get('/connect')
def connect():
    db = DB()
    print(db)
    return {'message': '接続成功'}