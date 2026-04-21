from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Твои данные
API_ID = 2040
API_HASH = 'b18441a1ff607e10a989891a5462e627'

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("\nТВОЯ СТРОКА СЕССИИ (СКОПИРУЙ ЕЁ ПОЛНОСТЬЮ):\n")
    print(client.session.save())
    print("\n-------------------------------------------")