from telethon import TelegramClient, events
from data import data
from sender import send_message_to_channel

api_id = data["api_id"]
api_hash = data["api_hash"]
channel = "@air_alert_ua"
test_channel = "testradar123"

client = TelegramClient("AutoRadar", api_id, api_hash)


@client.on(events.NewMessage(chats=channel))
async def handler(event):
    await send_message_to_channel(event.message.text)


async def main():
    print("Client started. Listening for new messages...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
