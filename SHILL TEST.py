from telethon import TelegramClient
import time
from telethon.tl.functions.channels import JoinChannelRequest
api_id = 24733307
api_hash = "91559d3ec9e5131ec6c2a2f8c9ab977d"
name = '6285641184294'
with TelegramClient(name, api_id, api_hash) as client:
    client.loop.run_until_complete(client(JoinChannelRequest('shilltest105')))
    while True:
        client.loop.run_until_complete(client.send_message('shilltest105', 'hi'))
        time.sleep(20)