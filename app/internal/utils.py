import sys
import time
import typing as t
from functools import wraps

from loguru import logger


def exc_info():
    """Get current exception information
    :return: Return current exception information: (type, value).
    """
    type_, value, _ = sys.exc_info()
    return type_, value


def latency(func: t.Callable):
    """Decorator to calculate endpoint latency. Print latency and response logs.
    :param: func: A callaable function

    :return: A callaable function
    """

    @wraps(func)
    async def wrapped_func(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)

        if result:
            message = f"[+] {result}"
            logger.log("RESPONSE", message)

        logger.log("LATENCY", f"[+] {round(time.time() - start_time, 10)} s")
        return result

    return wrapped_func
