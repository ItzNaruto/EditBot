import asyncio
from pyrogram import idle
from Kora import app, LOGGER, OWNER_ID

async def main():
    try:                    
        await app.start()
        await app.send_message(OWNER_ID, "**I'm Started Successfully ✨**")
        LOGGER.info("Client Started")
    except Exception as e:
        LOGGER.info(f"Error : {e}")
    await idle()

if __name__ == "__main__" :
    asyncio.run(main())
    LOGGER.info("Client Stopped!")
