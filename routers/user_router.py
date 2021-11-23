from fastapi import APIRouter, Request
from modules.db import DB
from modules.sql import SQL

user_router = APIRouter()


@user_router.post('/create_user')
async def create_user(request: Request):
    user_dto = await request.json()
    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.INSERT_USER, user_dto)
    con.commit()

    id_user = cur.lastrowid
    cur.execute(SQL.SELECT_USER_BY_ID_USER, {'id_user': id_user})
    user = cur.fetchone()

    return user
