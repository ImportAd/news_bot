import asyncio

from telethon import TelegramClient
import pandas as pd
import json
from pathlib import Path
import json
import os

from config import Config # import the api id, hash, session file
api_id = Config.api_id
api_hash = Config.api_hash
session_name = Config.session_name


async def collect_messages(chat_name, limit):
    """
    собирает сообщения из чата/группы
    принимает:
               chat_name - название чата без '@'
               limit - сколько последних сообщений выводить (None - все)
    возвращает словарь {"messages": messages, "channel": chat_info}
    """
    async with TelegramClient(session_name, api_id, api_hash) as client:
        chat_info = await client.get_entity(chat_name) # получение информации о чате/группе
        messages = await client.get_messages(entity=chat_info, limit=limit)
        return {"messages": messages, "channel": chat_info}


async def collect_message_chanle():
    limit=None
    chat_input = "Kollapsus" # название канала без "@"
    results = await collect_messages(chat_name = chat_input, limit=None)
    results.keys()
    print(len(results["messages"])) # всего постов в канале
    print(results["messages"][3].text)
    # print(results["channel"].to_dict())
    print(results.keys())
    print(type(results["messages"]))
    print(type(results["channel"]))

async def start():
    task1 = asyncio.create_task(collect_message_chanle())

    await task1

asyncio.run(start())