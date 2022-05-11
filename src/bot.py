import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage import redis

from settings import config


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    conf = config.load_config()

    storage = redis.RedisStorage2(
        host=conf.cache_config.host,
        port=conf.cache_config.port,
        password=conf.cache_config.password)

    bot = Bot(token=conf.tg_bot.token)
    bot['config'] = conf

    dp = Dispatcher(bot, storage=storage)
    config.register_all_services(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
