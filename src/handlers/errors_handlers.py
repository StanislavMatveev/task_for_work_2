"""
All the main handlers that are used when working with errors are listed here.
"""

from loguru import logger
from aiogram import Router
from aiogram.types import ErrorEvent


router: Router = Router()


@router.error()
async def error_handler(event: ErrorEvent) -> None:
    """
    Handler for logging all errors that
    occurred during the operation of other handlers.
    """
    
    logger.exception(event.exception)
