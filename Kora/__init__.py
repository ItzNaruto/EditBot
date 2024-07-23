import os
import logging
import time
from pyrogram import Client, filters, errors

# Time
StartTime = time.time()

# Logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Pyro Client
app = Client(
  "Kora", 
  api_id=API_ID, 
  api_hash=API_HASH, 
  bot_token=BOT_TOKEN
)

# Pyro Start
app.start()

# Vars
API_ID = 
API_HASH = ""
BOT_TOKEN = ""
BOT_ID = app.me.id
BOT_NAME = app.me.first_name
BOT_USERNAME = app.me.username

# Logs
print(f"[{BOT_USERNAME}] Is Starting. | Kora Project")
print(f"[{BOT_USERNAME}] Project Maintained By Kora")
print(f"[{BOT_USERNAME}] Is Alive")
