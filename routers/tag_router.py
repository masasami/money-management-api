from fastapi import APIRouter, Depends, Request
from modules.db import DB
from modules.sql import SQL
from modules.session import SessionData, cookie, verifier

tag_router = APIRouter(
    dependencies=[Depends(cookie), Depends(verifier)]
)


@tag_router.get('/get_tags_by_id_user')
def get_tags_by_id_user(session_data: SessionData = Depends(verifier)):
    db = DB()
    cur = db.cur
    id_user = session_data.id_user

    cur.execute(SQL.SELECT_TAG_BY_ID_USER, {'id_user': id_user})
    tags = cur.fetchall()

    return tags


@tag_router.post('/create_tag')
async def create_tag(request: Request, session_data: SessionData = Depends(verifier)):
    tag_dto = await request.json()
    tag_dto['id_user'] = session_data.id_user

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.INSERT_TAG, tag_dto)
    con.commit()
    id_tag = cur.lastrowid
    cur.execute(SQL.SELECT_TAG_BY_ID_TAG_ID_USER, {
        'id_tag': id_tag,
        'id_user': tag_dto['id_user']
    })
    tag = cur.fetchone()

    return tag


@tag_router.put('/update_tag/{id_tag}')
async def update_tag(id_tag: int, request: Request, session_data: SessionData = Depends(verifier)):
    tag_dto = await request.json()
    tag_dto['id_tag'] = id_tag
    tag_dto['id_user'] = session_data.id_user

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.UPDATE_TAG, tag_dto)
    con.commit()
    cur.execute(SQL.SELECT_TAG_BY_ID_TAG_ID_USER, {
        'id_tag': id_tag,
        'id_user': tag_dto['id_user']
    })
    tag = cur.fetchone()

    return tag


@tag_router.delete('/delete_tag/{id_tag}')
def delete_tag(id_tag: int, session_data: SessionData = Depends(verifier)):
    db = DB()
    con = db.con
    cur = db.cur

    id_user = session_data.id_user

    cur.execute(SQL.DELETE_TAG, {
        'id_tag': id_tag,
        'id_user': id_user
    })
    con.commit()

    return None
