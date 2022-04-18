from dataclasses import dataclass
import os


# Environ Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = tuple(map(int, os.environ.get("ADMINS").split(',')))
USE_REDIS = bool(os.environ.get("USE_REDIS"))

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS')


@dataclass
class DbConfig:
    database: str
    user: str
    password: str
    host: str
    port: int


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config() -> Config:
    """ load config with telegram-bot, database and extra fields """
    return Config(
        tg_bot=TgBot(
            token=BOT_TOKEN,
            admin_ids=ADMINS,
            use_redis=USE_REDIS,
        ),
        db=DbConfig(
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASS,
            host="db",
            port=5432,
        ),
        misc=Miscellaneous()
    )
