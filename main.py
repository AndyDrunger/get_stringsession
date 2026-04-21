from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Твои данные
API_ID = 38861033
API_HASH = 'c8350d37381c29f603eef2892bb3b7f3'

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("\nТВОЯ СТРОКА СЕССИИ (СКОПИРУЙ ЕЁ ПОЛНОСТЬЮ):\n")
    print(client.session.save())
    print("\n-------------------------------------------")