from aiogram import Dispatcher

from settings import settings as consts
from settings.data import CacheConfig, Config, TgBot, Miscellaneous
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.user import register_user
from tgbot.middlewares.db import DbMiddleware


def register_all_middlewares(dp: Dispatcher):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp: Dispatcher):
    register_admin(dp)
    register_user(dp)
    register_echo(dp)


def register_all_services(dp: Dispatcher):
    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)


def load_config() -> Config:
    """ load config with telegram-bot, database and extra fields """
    return Config(
        tg_bot=TgBot(
            token=consts.BOT_TOKEN, admin_ids=consts.ADMINS
        ),
        cache_config=CacheConfig(
            host=consts.REDIS_HOST,
            port=consts.REDIS_PORT,
            password=consts.REDIS_PASSWORD
        ),
        misc=Miscellaneous()
    )
