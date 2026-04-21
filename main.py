from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Твои данные
API_ID = 30758405
API_HASH = 'bc7e02c235c8bb64fbed12fe1ca7b339'

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("\nТВОЯ СТРОКА СЕССИИ (СКОПИРУЙ ЕЁ ПОЛНОСТЬЮ):\n")
    print(client.session.save())
    print("\n-------------------------------------------")