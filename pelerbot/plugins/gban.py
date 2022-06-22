import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from traceback import format_exc
from pelerbot import COMMAND_HANDLER
from pelerbot.utils.basic import *
from pelerbot.utils.gban_errors import *
from pelerbot.db.gbandb import *


@Client.on_message(filters.me & filters.command("gban", COMMAND_HANDLER))
async def gbun_him(client: Client, message: Message):
    gbun = await message.edit_text("`Processing..`")
    text_ = message.reply_to_message
    g_rsn = get_text(message)
    mee = await client.get_me()
    if text_:
        if g_rsn:
            grson = g_rsn
        else:
            grson = "That guy is a creepy scammer!"
        g_uid = text_.from_user.id
    elif g_rsn:
        gets_user_arg = g_rsn.split(None)
        g_rsn = gets_user_arg[1]
        g_uid = gets_user_arg[0]
        if g_uid.isnumberic():
            g_uid = g_uid
        else:
            if "@" in g_uid:
                usr_name = g_uid.replace("@", "").split(None)[0]
            else:
                usr_name = g_uid
            get_user_info = await client.get_users(usr_name)
            g_uid = get_user_info
    else:
        return await gbun.edit("`Reply To User Or Mention To GBan Him`")
    if g_uid == mee:
        return await gbun.edit("`You are trying to gban yourself?`")
    is_gbanned = await gban_info(g_uid)
    if is_gbanned:
        return await gbun.edit("`Sigoblok is already GBANNED!`")
    await gbun.edit("`Fetching Chats For Gban Process...`")
    f_chats = await iter_chat()
    if not f_chats:
        return await gbun.edit("`No Chats to Gban!`")
    total_f_chats = len(f_chats)
    for devils in f_chats:
        failed = 0
        try:
            await client.kick_chat_member(chat_id=devils, user_id=int(g_uid))
        except:
            failed += 1
    await gban_user(gban_id=g_uid, gban_reason=grson)
    await gbun.edit("**#GBanned** \n**User :** [{g_uid.first_name}](tg://user?id={g_uid}) \n**Reason :** `{grson}` \n**Affected Chats :** `{total_f_chats-failed}`")
    
    

@Client.on_message(filters.me & filters.command("ungban", COMMAND_HANDLER))
async def ungbun_him(client: Client, message: Message):
    ungbun = await message.edit_text("`Processing..`")
    ugtext_ = message.reply_to_message
    ugusr = get_text(message)
    if ugusr:
        if ugusr.isnumberic():
            unguid = ugusr
        else:
            if "@" in ugusr:
                usr_name = ugusr.replace("@", "").split(None)[0]
            else:
                usr_name = ugusr
            g_him = await client.get_users(usr_name)
            unguid = g_him.id
    else:
        unguid = ugtext_.from_user.id
    await ungbun.edit("`Wait Fectching Your Chats!`")
    ung_chat = await iter_chats()
    if not ung_chat:
        return await ungbun.edit("`No Chats to Gban!`")
    total_ung_chat = len(ung_chat)
    is_gbanned = await gban_info(unguid)
    if is_gbanned is None:
        return await ungbun.edit("`is this userr Gbanned?`")
    for good_job in ung_chat:
        failed = 0
        try:
            await client.unban_chat_member(chat_id=good_job, user_id=unguid)
        except:
            failed += 1
    await ungban_user(unguid)
    await ungbun.edit(f"**#Un_GBanned** \n**User :** [{unguid.first_name}](tg://user?id={unguid}) \n**Affected Chats :** `{total_ung_chat-failed}`")
    
    
@Client.on_message(filters.me & filters.command("gbanlist", COMMAND_HANDLER))
async def give_glist(client: Client, message: Message):
    oof = "**#GBanList** \n\n"
    glist = await message.edit_text("`Processing..`")
    list_ = await gban_list()
    if len(list_) == 0:
        await glist.edit("`No User is Gbanned Till Now!`")
        return
    for lit in list_:
        oof += f"**User :** `{lit['user']}` \n**Reason :** `{lit['reason']}` \n\n"
    await edit_or_send_as_file(oof, glist, client, "GbanList", "Gban-List")
