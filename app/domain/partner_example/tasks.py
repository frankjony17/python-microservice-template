import asyncio
from typing import Optional

from loguru import logger


async def send_email_background(sender_email: Optional[str], message: str) -> None:
    """Fake email sender (sleep for 15 seconds).
    :param: sender_email: email address
    :param: message: message to send

    :return: None
    """
    await asyncio.sleep(15)

    logger.info(f"[+] Email sent successfully - Sender={sender_email} - Message={message}")
