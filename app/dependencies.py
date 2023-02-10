from typing import Callable, Generator, Type

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.database import SessionLocal
from app.domain.common.repository_base import RepositoryBase
from app.internal.utils import latency


def get_session_db() -> Generator:
    """Get database session"""
    session_local = SessionLocal()
    try:
        yield session_local
    finally:
        session_local.close()


def get_repository(repo_type: Type[RepositoryBase]) -> Callable[[Session], RepositoryBase]:
    """Get repository"""

    def __get_repo(session_db: Session = Depends(get_session_db)) -> RepositoryBase:
        return repo_type(session=session_db)

    return __get_repo


@latency
async def access_validation(_request: Request) -> None:
    """Validate token via SSO
    :param _request: Request
    :param authorization: HTTPAuthorizationCredentials

    :return: None
    :raise HTTPException
    """
