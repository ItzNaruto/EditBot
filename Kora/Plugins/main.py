from Kora import app 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("start"))
async def start(client, message):
    user_mention = message.from_user.mention
    start_text = f"""
👋 **Hello {user_mention}!**

I'm your **Edit Guardian Bot**, here to keep our conversations transparent and safe! 

🚫 **Edited Message Deletion:** I will delete any edited messages to maintain clarity.

📣 **Notifications:** You will be notified each time a message is deleted.

**How to Get Started:**
1. **Add me to your group**.
2. I will begin protecting the group instantly.

Click the button below to add me and safeguard our discussions!
"""
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ Add Me To Your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton("🗯️ Support", url="https://t.me/SupportChat"),
             InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/KoraXD")],
        ]
    )
    await message.reply_text(start_text, reply_markup=keyboard)

@app.on_message(filters.group & filters.edited)
async def check_edit(client, message):
    user_mention = message.from_user.mention

    if message.from_user.id != 6495253163:
        await message.delete()
        await message.chat.send_message(f"❌ {user_mention} just edited a message. The edited message has been deleted to maintain transparency.")
