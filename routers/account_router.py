from fastapi import APIRouter, Depends, Request
from modules.db import DB
from modules.sql import SQL
from modules.session import SessionData, cookie, verifier

account_router = APIRouter(
    dependencies=[Depends(cookie), Depends(verifier)]
)


@account_router.get('/get_accounts_by_id_user')
async def get_accounts_by_id_user(
    start: str = None,
    end: str = None,
    session_data: SessionData = Depends(verifier)
):
    # ユーザーID
    id_user = session_data.id_user

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


@account_router.post('/create_account')
async def create_account(request: Request, session_data: SessionData = Depends(verifier)):
    account_dto = await request.json()
    account_dto['id_user'] = session_data.id_user

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.INSERT_ACCOUNT, account_dto)
    con.commit()

    id_account = cur.lastrowid
    account_dto['id_account'] = id_account

    return account_dto


@account_router.put('/update_account/{id_account}')
async def update_account(id_account: int, request: Request, session_data: SessionData = Depends(verifier)):
    account_dto = await request.json()
    account_dto['id_account'] = id_account
    account_dto['id_user'] = session_data.id_user

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.UPDATE_ACCOUNT, account_dto)
    con.commit()

    return account_dto


@account_router.delete('/delete_account/{id_account}')
def delete_account(id_account: int, session_data: SessionData = Depends(verifier)):
    id_user = session_data.id_user
    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.DELETE_ACCOUNT, {
        'id_account': id_account,
        'id_user': id_user
    })
    con.commit()

    return None


@account_router.post('/upsert_accounts')
async def upsert_accounts(request: Request, session_data: SessionData = Depends(verifier)):
    param = await request.json()
    accounts = param['accounts']
    id_user = session_data.id_user

    db = DB()
    con = db.con
    cur = db.cur

    for index, account in enumerate(accounts):
        if account['id_account']:
            account['id_user'] = id_user
            cur.execute(SQL.UPDATE_ACCOUNT, account)
            cur.execute(SQL.SELECT_ACCOUNT_BY_ID_ACCOUNT_ID_USER, {
                'id_account': account['id_account'],
                'id_user': id_user
            })
            accounts[index] = cur.fetchone()
        else:
            account['id_user'] = id_user
            cur.execute(SQL.INSERT_ACCOUNT, account)
            id_account = cur.lastrowid
            cur.execute(SQL.SELECT_ACCOUNT_BY_ID_ACCOUNT_ID_USER, {
                'id_account': id_account,
                'id_user': id_user
            })
            accounts[index] = cur.fetchone()
    con.commit()

    return accounts


@account_router.post('/delete_accounts')
async def delete_accounts(request: Request, session_data: SessionData = Depends(verifier)):
    param = await request.json()
    id_accounts = param['id_accounts']
    id_user = session_data.id_user

    db = DB()
    con = db.con
    cur = db.cur

    for id_account in id_accounts:
        cur.execute(SQL.DELETE_ACCOUNT, {
            'id_account': id_account,
            'id_user': id_user,
        })
    con.commit()

    return None
