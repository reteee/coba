from pyrogram import Client, filters
from pyrogram.types import message
from pelerbot import COMMAND_HANDLER
from pelerbot.db.gbandb import *
from pelerbot.utils.basic import *
from pelerbot.plugins.help import *





@Client.on_message(filters.me & filters.command("gban", COMMAND_HANDLER))
async def gbun_him(client: Client, message: Message):
    gbun = await message.edit_text("`Processing..`")
    r_msg = message.reply_to_message
    gban_rsn = get_arg(message)
    owner = await client.get_me()
    if r_msg:
        if gban_rsn:
            gban_rson = gban_rsn
        else:
            gban_rson = "That guy is a creepy scammer!"
        gban_uid = r_msg.from_user.id
    elif gban_rsn:
        gets_user_arg = gban_rsn.split(None)
        gban_rson = gets_user_arg[1]
        gban_uid = gets_user_arg[0]
        if gban_uid.isnumeric():
            gban_uid = gban_uid
        else:
            if "@" in gban_uid:
                usr_name = gban_uid.replace("@", "").split(None)[0]
            else:
                usr_name = gban_uid
            get_usr_info = await NEXAUB.get_users(usr_name)
            gban_uid = get_usr_info.id
    else:
        return await gbun.edit("`Give a User ID, Username or Reply to a user message to Gban`")
    if gban_uid == owner.id:
        return await gbun.edit("`You are trying to gban yourself?`")
    is_gbanned = await get_gban_reason(gban_uid)
    if is_gbanned:
        return await gbun.edit("`Si goblok is already GBANNED!`")
    await gbun.edit("`Fetching Chats For Gban Process...`")
    f_chats = await get_ma_chats()
    if not f_chats:
        return await gbun.edit("`No Chats to Gban!`")
    total_f_chats = len(f_chats)
    for gokid in f_chats:
        ub_failed = 0
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(gban_uid))
        except:
            ub_failed += 1
    await gban_user(gban_id=gban_uid, gban_reason=gban_rson)
    await gbun.edit(f"**#USER_GBANNED** \n\n**User:** `{gban_uid}` \n**Reason:** `{gban_rson}` \n**Total Chats:** `{total_f_chats-ub_failed}`")
