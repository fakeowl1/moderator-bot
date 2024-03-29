from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.client.telegram import TelegramAPIServer
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.client.session.aiohttp import AiohttpSession


import config
import utils


storage = MemoryStorage()

# Create client connection
tgc = utils.TelegramClient(config.api_id, config.api_hash, config.bot_token)

scheduler = AsyncIOScheduler()

session = AiohttpSession(
    api=TelegramAPIServer.from_base(config.telegram_api_server),
)

bot = Bot(
    token=config.bot_token,
    session=session,
    parse_mode="Markdown"
)

dp = Dispatcher(storage=storage)
