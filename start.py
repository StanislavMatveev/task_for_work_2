import asyncio
from loguru import logger

# Initializing logger
logger.add(
    sink='logs/tgbt_log.json',
    rotation='monthly',
    compression='zip',
    serialize=True
)

from src.tgbot import bot_inicialize_and_start


@logger.catch
def main() -> None:
    # Preparing the bot
    asyncio.run(bot_inicialize_and_start())


if __name__ == '__main__':
    main()
