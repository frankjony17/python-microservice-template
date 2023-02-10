import traceback
from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable, Optional, Tuple, Type

from pydantic import BaseModel, ValidationError
from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError

from app.domain.common.exception_base import (
    NotFoundException,
    SQLAlchemyException,
    UniqueException,
    ValidationException,
)
from app.internal.utils import exc_info


@dataclass
class ServiceBase:
    @classmethod
    def query_result(cls, result: list[Any] | dict[str, Any] | Type[BaseModel] | Optional[Tuple[Any]]) -> Any:
        """Query result, obtain the result or raise an exception"""
        if result:
            return result
        raise NotFoundException()


def try_query_except(func: Callable):
    """Decorator to try to raise an exception"""

    @wraps(func)
    async def wrapped_func(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
        except NoResultFound as exc:
            raise NotFoundException() from exc
        except ValidationError as exc:
            raise ValidationException(stacktrace=traceback.format_exception_only(*exc_info())) from exc
        except IntegrityError as exc:
            raise UniqueException(stacktrace=traceback.format_exception_only(*exc_info())) from exc
        except SQLAlchemyError as exc:
            raise SQLAlchemyException(stacktrace=traceback.format_exception_only(*exc_info())) from exc
        return result

    return wrapped_func
