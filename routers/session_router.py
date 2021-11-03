from fastapi import HTTPException, Request, Response, Depends, APIRouter

from modules.sql import SQL
from modules.db import DB
from modules.session import SessionData, backend, cookie, verifier

from uuid import UUID, uuid4
from dotenv import load_dotenv
load_dotenv()


session_router = APIRouter()


# ログイン
@session_router.post('/login')
async def login(request: Request, response: Response):
    param = await request.json()
    db = DB()
    cur = db.cur

    # TODO パスワードの暗号化、パスワードをもとにユーザーを取得

    cur.execute(SQL.SELECT_USER_BY_LOGIN_ID, {
        'login_id': param['login_id']
    })
    user = cur.fetchone()
    if user is None:
        raise HTTPException(401)

    id_user = user['id_user']
    session = uuid4()
    data = SessionData(id_user=id_user)
    await backend.create(session, data)
    cookie.attach_to_response(response, session)

    return user


# 認証
@session_router.get('/auth', dependencies=[Depends(cookie)])
async def auth(session_data: SessionData = Depends(verifier)):
    db = DB()
    cur = db.cur
    cur.execute(SQL.SELECT_USER_BY_ID_USER, {'id_user': session_data.id_user})
    user = cur.fetchone()
    if user is None:
        raise HTTPException(401)

    return user


# ログアウト
@session_router.post('/logout')
async def logout(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)

    return None
