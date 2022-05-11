import typing

from aiogram.dispatcher.filters import BoundFilter

from settings.data import Config


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None) -> bool:
        self.is_admin = is_admin

    async def check(self, obj):
        if not self.is_admin:
            return False
        config: Config = obj.bot.get('config')
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin
