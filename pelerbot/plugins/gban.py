import asyncio
import time

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from pelerbot import COMMAND_HANDLER
from pelerbot.utils.basic import *
from pelerbot.utils.ping import get_readable_time
from pelerbot.db.mongodatabase import (add_banned_user,
                                       get_banned_count,
                                       get_banned_users,
                                       get_served_chats,
                                       is_banned_user,
                                       remove_banned_user)
from pelerbot.plugins.help import *

BANNED_USERS = filters.user()

@Client.on_message(filters.me & filters.command("gban", COMMAND_HANDLER))
async def gbanuser(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("`Reply to a user's message or give username/user id.`")
        user = message.text.split(None, 1)[1]
        user = await client.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    if user_id == message.from_user.id:
        return await message.reply_text("`You want to gban yourself? How Fool!`")
    is_gbanned = await is_banned_user(user_id)
    if is_gbanned:
        return await message.reply_text("{0} is already **gbanned**".format(mention))
    if user_id not in BANNED_USERS:
        BANNED_USERS.add(user_id)
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text(
        "**Initializing Gobal Ban on {0}**\n\nExpected Time : {1}.".format(mention, time_expected)
    )
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await client.ban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await add_banned_user(user_id)
    await message.reply_text(
        "**Gbanned Successfully**\n\nBanned **{0}** from **{1}** chats.".format(mention, number_of_chats)
    )

    

@Client.on_message(filters.me & filters.command("ugban", COMMAND_HANDLER))
async def gungabn(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("`Reply to a user's message or give username/user id.`")
        user = message.text.split(None, 1)[1]
        user = await client.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    is_gbanned = await is_banned_user(user_id)
    if not is_gbanned:
        return await message.reply_text("{0} is not **gbanned**".format(mention))
    if user_id in BANNED_USERS:
        BANNED_USERS.remove(user_id)
    served_chats = []
    chats =await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text(
        "**Ungbanning {0}**\n\nExpected Time : {1}.".format(mention, time_expected)
    )
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await client.unban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await remove_banned_user(user_id)
    await message.reply_text(
        "**UnGbanned Successfully**\n\nUnbanned **{0}** in **{1}** chats.".format(mention, number_of_chats)
    )
