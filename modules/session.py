# FastAPI
from fastapi import HTTPException

# セッション
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from fastapi_sessions.session_verifier import SessionVerifier
from pydantic import BaseModel

import os
from uuid import UUID
from dotenv import load_dotenv
load_dotenv()


class SessionData(BaseModel):
    id_user: int


cookie_params = CookieParameters()
cookie = SessionCookie(
    cookie_name='money_management_cookie',
    identifier='general_verifier',
    auto_error=True,
    secret_key=os.getenv('SECRET_KEY'),
    cookie_params=cookie_params,
)
backend = InMemoryBackend[UUID, SessionData]()


class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        return True


verifier = BasicVerifier(
    identifier='general_verifier',
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(401),
)
