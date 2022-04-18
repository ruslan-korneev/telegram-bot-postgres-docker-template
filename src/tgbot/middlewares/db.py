from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    async def pre_process(self, obj, data, *args):
        pass
        # db_session = obj.bot.get('db')
        # Get data from table to handler
        # data['some_model'] = await Model.get()
