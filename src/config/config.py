from os import getenv

from loguru import logger


class BotConfig:
    """
    Class for storing information about the bot.
    """
    
    if getenv('BOT_TOKEN'):
        BOT_TOKEN: str = getenv('BOT_TOKEN') # type: ignore
    else:
        logger.critical('The "BOT_TOKEN" environment variable is not present in the system.')


class DBConfig:
    """
    Class for storing information about the DB.
    """

    if getenv('DB_HOST') and getenv('DB_PORT'):
        DB_HOST: str = getenv('DB_HOST') # type: ignore
        DB_PORT: int = int(getenv('DB_PORT')) # type: ignore
    else:
        logger.critical('The "DB_HOST" or "DB_PORT" environment variable is not present in the system.')
