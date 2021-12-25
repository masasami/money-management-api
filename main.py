
# ルーター

from routers.connect_router import connect_router
from routers.user_router import user_router
from routers.account_router import account_router
from routers.tag_router import tag_router
from routers.session_router import session_router

# ライブラリ
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('ALLOW_ORIGIN')],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.middleware('http')
async def check_api_key(request: Request, call_next):
    response = await call_next(request)
    if request.method == 'OPTIONS':
        return response

    api_key = request.headers.get('api_key')
    my_api_key = os.getenv('API_KEY')
    if api_key and my_api_key and api_key == my_api_key:
        return response
    return JSONResponse(status_code=400)


app.include_router(connect_router)
app.include_router(user_router)
app.include_router(account_router)
app.include_router(tag_router)
app.include_router(session_router)
