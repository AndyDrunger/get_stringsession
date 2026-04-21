from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Твои данные
API_ID = 38364566
API_HASH = '7104f653afd35202c38a17e08bfe7a35'

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("\nТВОЯ СТРОКА СЕССИИ (СКОПИРУЙ ЕЁ ПОЛНОСТЬЮ):\n")
    print(client.session.save())
    print("\n-------------------------------------------")