from fastapi import APIRouter, Request
from modules.db import DB
from modules.sql import SQL
from modules.hash import create_hash

user_router = APIRouter()


@user_router.post('/create_user')
async def create_user(request: Request):
    user_dto = await request.json()

    db = DB()
    con = db.con
    cur = db.cur

    # パスワードをハッシュ化
    user_dto['password'] = create_hash(user_dto['password'])
    cur.execute(SQL.INSERT_USER, user_dto)
    id_user = cur.lastrowid
    cur.execute(SQL.INSERT_TAG, {
        'id_user': id_user,
        'title': '給料',
        'color_code': '0000ff'
    })
    cur.execute(SQL.INSERT_TAG, {
        'id_user': id_user,
        'title': '食費',
        'color_code': '00ff00'
    })
    cur.execute(SQL.INSERT_TAG, {
        'id_user': id_user,
        'title': '娯楽費',
        'color_code': 'ff0000'
    })
    con.commit()

    cur.execute(SQL.SELECT_USER_BY_ID_USER, {'id_user': id_user})
    user = cur.fetchone()

    return user


@user_router.post('/get_user_by_login_id')
async def get_user_by_login_id(request: Request):
    login_id = (await request.json())['login_id']

    db = DB()
    cur = db.cur

    cur.execute(SQL.SELECT_USER_BY_LOGIN_ID, {'login_id': login_id})
    user = cur.fetchone()

    return user


@user_router.post('/get_user_by_email')
async def get_user_by_email(request: Request):
    email = (await request.json())['email']

    db = DB()
    cur = db.cur

    cur.execute(SQL.SELECT_USER_BY_EMAIL, {'email': email})
    user = cur.fetchone()

    return user
