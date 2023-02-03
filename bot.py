import time
import logging
from telethon import TelegramClient, events, sync, utils

# create logger
logger = logging.getLogger('Bot logger')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              "%d-%m-%Y %H:%M:%S")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
old_message = ''

# Setting configuration values for Telegram
api_id = 640814
api_hash = '1aa8f0b4777c1148238777c08d1c5ea4'
api_hash = str(api_hash)
phone = '+34665796478'
username = 'fabianskitr'

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

# Recieve channel message and formard event to different channel
@client.on(events.NewMessage) 

async def logging_eventos(event):
    try:
        entity = event.peer_id.channel_id

        if entity == 1667240577: # Dr.Profit from with id 1667240577
            forward_group_id = 1832633149 # Futures and spot channel id
            logger.info('Channel_name: Crypto VIP' + ' | from_id_channel: ' + str(entity))
            print(event.text)
            await client.send_message(forward_group_id , event.message)

        elif entity == 1842502885: # VIP Signals from id 1842502885
            forward_group_id = 1447470236 # Scalping channel id
            new_message = event.text
            if 'achieved' in event.text or 'stoploss' in event.text.lower():
                #if 'bybit' in event.text.lower():
                logger.info('Channel_name: Test' + ' | from_id_channel: ' + str(entity))
                print(event.text)
                await client.send_message(forward_group_id , event.message)
            elif 'pair' in event.text.lower():
                logger.info('Channel_name: Test' + ' | from_id_channel: ' + str(entity))
                print(event.text)
                old_message = event.text
                await client.send_message(forward_group_id , event.message)

        elif entity == 1827280350:
            forward_group_id  = 1827280350 # Test channel
            logger.info('Channel_name: Crypto VIP' + ' | from_id_channel: ' + str(entity))
            print(event.text)
            await client.send_message(forward_group_id , event.message)
            old_message = event.text

    except AttributeError:
        print('No such attribute channel_id')

client.start() 
client.run_until_disconnected()
