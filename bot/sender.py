from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from data import data
import logging

API_TOKEN = data["BOT_TOKEN"]
CHANNEL_ID = "@testingRadar1"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def send_message_to_channel(text: str):
    await bot.send_message(CHANNEL_ID, text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
