from fastapi import APIRouter, Request
from modules.db import DB
from modules.sql import SQL

login_router = APIRouter()


@login_router.post('/login')
async def login(request: Request):
    param = await request.json()
    db = DB()
    cur = db.cur

    # TODO パスワードの暗号化、パスワードをもとにユーザーを取得

    cur.execute(SQL.SELECT_USER_BY_LOGIN_ID, {
        'login_id': param['login_id']
    })
    user = cur.fetchone()
    return user
