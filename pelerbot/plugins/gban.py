import asyncio
from pyrogram import Client , filters
from pyrogram.types import Message
from pelerbot.db.gbandb import *
from pelerbot.utils.basic import *
from pelerbot import COMMAND_HANDLER
from pelerbot.plugins.help import *




@Client.on_message(filters.me & filters.command("gban", COMMAND_HANDLER))
async def gbun_him(client: Client, message: Message):
    gbun = await message.edit_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await gbun.edit("`Reply To User Or Mention To GBan Him`")
        return
    try:
        userz = await client.get_users(user)
    except:
        userz.id = int(user)
    if not reason:
        reason = "Private Reason!"
    mee = await client.get_me()
    if userz.id == mee.id:
        await gbun.edit("`Why bothering yourself`")
        return
    if await gban_info(userz.id):
        await gbun.edit("`Re-Gban? Seriously? :/`")
        return
    await gbun.edit("`Please, Wait Fectching Your Chats!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        gbun.edit("`You Have No Chats! So Sad`")
        return
    await gbun.edit("`Starting GBans Now!`")
    for devils in chat_dict:
        try:
            await client.kick_chat_member(devils, int(userz.id))
        except:
            failed += 1
    await gban_user(userz.id, reason)
    gbanned = f"**#GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id}) \n**Reason :** `{reason}` \n**Affected Chats :** `{chat_len-failed}`"
    await gbun.edit(gbanned)
