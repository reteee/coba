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
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await gbun.edit("`Reply To User Or Mention To GBan Him`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await gbun.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    if not reason:
        reason = "Private Reason!"
    mee= await client.get_me()
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
    

@Client.on_message(filters.me & filters.command("ungban", COMMAND_HANDLER))
async def ungbun_him(client: Client, message: Message):
    ungbun= await message.edit_text("`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await ungbun.edit("`Reply To User Or Mention To Un-GBan Him`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await ungbun.edit(f"`404 : User Doesn't Exists!`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await ungbun.edit("`what a joke`")
        return
    if not await gban_info(userz.id):
        await ungbun.edit("`Un-Gban A Ungbanned User? Seriously? :/`")
        return
    await ungbun.edit("`Please, Wait Fectching Your Chats!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        ungbun.edit("`You Have No Chats! So Sad`")
        return
    await ungbun.edit("`Starting Un-GBans Now!`")
    for devils in chat_dict:
        try:
            await client.unban_chat_member(devils, int(userz.id))
        except:
            failed += 1
    await ungban_user(userz.id)
    ungbanned = f"**#Un_GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id}) \n**Affected Chats :** `{chat_len-failed}`"
    await ungbun.edit(ungbanned)
    
    
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
