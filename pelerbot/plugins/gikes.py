import asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client , filters
from pyrogram.types import Message
from pelerbot.utils.gban_errors import *
from pelerbot.utils.basic import *
from pelerbot import COMMAND_HANDLER

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""
Manage Tasks with your userbot easily, great plugin for people to manage their chats.
`{COMMAND_HANDLER}gikes`: Global Broadcast to the Group.
Usage: {COMMAND_HANDLER}gikes (input or reply to message)
"""

@Client.on_message(filters.me & filters.command("gikes", COMMAND_HANDLER))
async def gbroadcast(client: Client, message: Message):
    if text_ := get_text(message):
        msg = text_
    elif message.reply_to_message:
        msg = message.reply_to_message.text
    else:
        return await message.reply_text("`Input text or Reply to a message`")
    msg_ = await message.reply_text("`Processing..`")
    done =0
    err =0
    
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ["supergroup", "group"]:
            try:
                await client.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done += 1
                await asyncio.sleep(0.1)
            except Exception:
                err += 1
    await msg_.reply_text(
        f"`Message Sucessfully Send To {done} Chats! Failed In {err} Chats.`"
    )
