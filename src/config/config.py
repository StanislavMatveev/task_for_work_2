from os import getenv

from loguru import logger


class BotConfig:
    """
    Class for storing information about the bot.
    """
    
    BOT_TOKEN: str | None = getenv('BOT_TOKEN')
    if not BOT_TOKEN:
        logger.critical('The "BOT_TOKEN" environment variable is not present in the system.')
