"""
All basic handlers are listed here.
"""

from typing import Dict

from aiogram import F, Router
from aiogram.types import Message

from src.utils import mongodb_manipulator
from src.filters import IsCorrectData


router: Router = Router()
router.message.filter(
    F.text
)


@router.message(IsCorrectData())
async def process_data(message: Message, cor_data: Dict[str, str]) -> None:
    """
    Handler to receive a request and return a response.
    """

    data_for_message: str | None = await mongodb_manipulator.get_data(data=cor_data)
    if data_for_message:
        await message.answer(data_for_message)
