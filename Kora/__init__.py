import time
import logging
from pyrogram import Client

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                  logging.StreamHandler()], format="[KORA]: %(message)s")
StartTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

API_ID = 18641799
API_HASH = "2027706706fd39baf84c01ff5b95a6a6"
BOT_TOKEN = "7001280039:AAE1Zm4aDgrOcr2L9_pbivf6J7TBE0SJfWU"
BOT_USERNAME = "EditManagerBot"

app = Client(
    "Kora", 
    api_id=API_ID, 
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Kora/Plugins")
)
