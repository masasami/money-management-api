from fastapi import APIRouter, Depends, Request
from modules.db import DB
from modules.sql import SQL
from modules.session import cookie

account_router = APIRouter()
account_router.dependencies = [Depends(cookie)]


@account_router.get('/get_accounts_by_id_user/{id_user}')
def get_accounts_by_id_user(id_user: int, start: str = None, end: str = None):
    db = DB()
    cur = db.cur

    param = {'id_user': id_user}
    sql = SQL.SELECT_ACCOUNT_BY_ID_USER
    if start and end:
        param['start'] = start
        param['end'] = end
        sql = SQL.SELECT_ACCOUNT_BY_ID_USER_START_END

    cur.execute(sql, param)
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


@account_router.post('/upsert_accounts')
async def upsert_accounts(request: Request):
    param = await request.json()
    accounts = param['accounts']

    db = DB()
    con = db.con
    cur = db.cur

    for index, account in enumerate(accounts):
        if account['id_account']:
            cur.execute(SQL.UPDATE_ACCOUNT, account)
            cur.execute(SQL.SELECT_ACCOUNT_BY_ID_ACCOUNT, {
                'id_account': account['id_account']
            })
            accounts[index] = cur.fetchone()
        else:
            cur.execute(SQL.INSERT_ACCOUNT, account)
            id_account = cur.lastrowid
            cur.execute(SQL.SELECT_ACCOUNT_BY_ID_ACCOUNT, {
                'id_account': id_account
            })
            accounts[index] = cur.fetchone()
    con.commit()

    return accounts


@account_router.post('/delete_accounts')
async def delete_accounts(request: Request):
    param = await request.json()
    id_accounts = param['id_accounts']
    print(id_accounts)

    db = DB()
    con = db.con
    cur = db.cur

    for id_account in id_accounts:
        cur.execute(SQL.DELETE_ACCOUNT, {'id_account': id_account})
    con.commit()

    return None
