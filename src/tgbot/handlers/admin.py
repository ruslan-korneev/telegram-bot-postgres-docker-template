from aiogram import Dispatcher, types


async def admin_start(message: types.Message):
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, commands=["start"],
        state="*", is_admin=True
    )
