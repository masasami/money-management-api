from fastapi import APIRouter
from modules.db import DB
from modules.sql import SQL

account_router = APIRouter()


@account_router.get('/get_account_by_id_user/{id_user}')
def get_account_by_id_user(id_user: int):
    db = DB()
    cur = db.cur

    cur.execute(SQL.SELECT_ACCOUNT_BY_ID_USER, {'id_user': id_user})
    accounts = cur.fetchall()

    return accounts
