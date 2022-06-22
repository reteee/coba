from pyrogram import Client, filters
from pyrogram.types import Message
from pelerbot.db.gmutedb import *
from pelerbot.utils.basic import *
from pelerbot.plugins.help import *
from pelerbot import COMMAND_HANDLER


@Client.on_message(filters.me & filters.command("gmute", COMMAND_HANDLER))
async def gmute_him(client: Client, message: Message):
    g = await message.edit_text("`Processing..`")
    text_ = message.reply_to_message.text
    user, reason = get_user(message, text_)
    mee = await client.get_me()
    if not text_:
        if user:
            user = user
        else:
            return await g.edit("`Reply To User Or Mention To Gmute Him`")
    userz.id = await client.get_users(user)
    failed = 0
    if userz.id = mee:
        return await g.edit("`I can't gmute myself.`")
    if is_gmuted(userz.id)
        return await g.edit("`User is already gmuted.`")
    if not reason:
        reason = "Just_Gmutted!"
    dlog = client.iter_dialogs()
    if not dlog:
        return await g.edit("`No Chats to Gmute!`")
        failed += 1
    await gmute(userz.id, reason)
    await g.edit(f"**#Gmutted** \n**User :** `{userz.id}` \n**Reason :** `{failed}`")
