import asyncio
from pyrogram import idle
from Kora import app

async def main():
    try:
        await app.send_message(6495253163, "**I'm Started Successfully ✨**")
        print("Client Started!")
    except Exception as e:
        print(f"Error : {e}")
    await idle()

if __name__ == "__main__" :
    asyncio.run(main())
    LOGGER.info("Client Stopped!")
