from aiogram import Bot, Dispatcher
from loguru import logger

from src.config import BotConfig
from src.handlers import (
    default_state_handler,
    errors_handlers
)


async def bot_inicialize_and_start() -> None:
    """
    Function for preparing and launching the bot.
    """

    logger.success('Bot started work.')

    # Creating bot and dispatcher
    bot: Bot = Bot(
        token=BotConfig.BOT_TOKEN,
        parse_mode='HTML'
    )
    dp: Dispatcher = Dispatcher()

    # Registering routers
    dp.include_router(default_state_handler.router)
    dp.include_router(errors_handlers.router)

    # Droping updates and starting the bot
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    logger.success('Bot completed work.')
