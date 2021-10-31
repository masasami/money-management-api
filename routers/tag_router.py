from fastapi import APIRouter, Request
from modules.db import DB
from modules.sql import SQL

tag_router = APIRouter()


@tag_router.get('/get_tags_by_id_user/{id_user}')
def get_tags_by_id_user(id_user: int):
    db = DB()
    cur = db.cur

    cur.execute(SQL.SELECT_TAG_BY_ID_USER, {'id_user': id_user})
    tags = cur.fetchall()

    return tags


@tag_router.post('/create_tag')
async def create_tag(request: Request):
    tag_dto = await request.json()

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.INSERT_TAG, tag_dto)
    con.commit()
    id_tag = cur.lastrowid
    tag_dto['id_tag'] = id_tag

    return tag_dto


@tag_router.put('/update_tag/{id_tag}')
async def update_tag(id_tag: int, request: Request):
    tag_dto = await request.json()
    tag_dto['id_tag'] = id_tag

    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.UPDATE_TAG, tag_dto)
    con.commit()

    return tag_dto


@tag_router.delete('/delete_tag/{id_tag}')
def delete_tag(id_tag: int):
    db = DB()
    con = db.con
    cur = db.cur

    cur.execute(SQL.DELETE_TAG, {'id_tag': id_tag})
    con.commit()

    return None