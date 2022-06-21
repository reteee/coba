import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pelerbot.db import gmute_db as db
from pelerbot import COMMAND_HANDLER
from pelerbot.utils.pyrohelpers import extract_user
from pelerbot.utils.parser import mention_markdown
from pelerbot.plugins.help import *


@Client.on_message(filters.command("gmute", COMMAND_HANDLER) & filters.me)
async def start_gmute(c: Client, m: Message):
    await m.edit_text("`Putting duct tape...`")
    user_id, user_first_name = await extract_user(m)
    if db.is_gmuted(user_id):
        await m.edit_text("`This user is already gmuted!`")
        return
    try:
        db.gmute(user_id)
    except Exception as e:
        await m.edit_text(f"<b>Error:</b>\n\n{str(e)}")
    else:
        await m.edit_text("`Successfully gmuted that person`")
        await c.send_message(
            "#GMUTE\nUser: {} in Chat {}".format(
                mention_markdown(user_first_name, user_id), m.chat.title
            ),
        )
    return


@Client.on_message(filters.command("ungmute", COMMAND_HANDLER) & filters.me)
async def end_gmute(c: Client, m: Message):
    await m.edit_text("`Removing duct tape...`")
    user_id, user_first_name = await extract_user(m)

    if not db.is_gmuted(user_id):
        await m.edit_text("`This user is not gmuted!`")
        return
    try:
        db.ungmute(user_id)
    except Exception as e:
        await m.edit_text(f"<b>Error:</b>\n\n{str(e)}")
    else:
        await m.edit_text("`Successfully ungmuted that person`")
        await c.send_message(
            "#UNGMUTE\nUser: {} in Chat {}".format(
                mention_markdown(user_first_name, user_id), m.chat.title
            ),
        )
    return


@Client.on_message(filters.command("gmutelist", COMMAND_HANDLER) & filters.me)
async def list_gmuted(c: Client, m: Message):
    await m.edit_text("`Loading users...`")
    users = db.get_gmute_users()
    if not users:
        await m.edit_text("`No users are gmuted!`")
        return
    users_list = "`Currently Gmuted users:`\n"
    u = 0
    for x in users:
        u += 1
        user = await c.get_users(x)
        users_list += f"[{u}] {mention_markdown(user.first_name, user.id)}: {user.id}\n"
    await m.edit_text(users_list)
    return


@Client.on_message(filters.group, group=5)
async def watcher_gmute(c: Client, m: Message):
    try:
        if db.is_gmuted(m.from_user.id):
            await asyncio.sleep(0.1)
            await c.delete_messages(chat_id=m.chat.id, message_ids=m.message_id)
    except AttributeError:
        pass
    except Exception as ef:
        print(ef)
    return


add_command_help(
    "gmute",
    [
        ["gmute", "as a reply to user or entering user id."],
        
        ["ungmute", "as a reply to user or entering user id."],
        
        ["gmutelist", "To view list of currently gmuted users."],
    ],
)
