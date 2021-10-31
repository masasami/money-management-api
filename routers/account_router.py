from fastapi import APIRouter
from modules.db import DB
from modules.sql import SQL
from fastapi.requests import Request

account_router = APIRouter()


@account_router.get('/get_accounts_by_id_user/{id_user}')
def get_account_by_id_user(id_user: int):
    db = DB()
    cur = db.cur

    cur.execute(SQL.SELECT_ACCOUNT_BY_ID_USER, {'id_user': id_user})
    accounts = cur.fetchall()

    return accounts


@account_router.get('/get_account_by_id_account/{id_account}')
def get_account_by_id_account(id_account: int):
    db = DB()
    cur = db.cur

    cur.execute(SQL.SELECT_ACCOUNT_BY_ID_ACCOUNT, {'id_account': id_account})
    account = cur.fetchone()

    return account


@account_router.post('/create_account')
async def create_account(request: Request):
    account_dto = await request.json()

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.INSERT_ACCOUNT, account_dto)
    con.commit()

    id_account = cur.lastrowid
    account_dto['id_account'] = id_account

    return account_dto


@account_router.put('/update_account/{id_account}')
async def update_account(id_account: int, request: Request):
    account_dto = await request.json()
    account_dto['id_account'] = id_account

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.UPDATE_ACCOUNT, account_dto)
    con.commit()

    return account_dto


@account_router.delete('/delete_account/{id_account}')
def delete_account(id_account: int):
    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.DELETE_ACCOUNT, {'id_account': id_account})
    con.commit()

    return None
