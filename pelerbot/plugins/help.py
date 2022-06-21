import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pelerbot.plugins import ALL_PLUGINS
from pelerbot import COMMAND_HANDLER
from pelerbot import HELP_COMMANDS


HELP_DEFAULT = f"""
To get help for any command, just type `{COMMAND_HANDLER}help plugin_name`
'plugin_name' should be the name of a proper plugin!

Get a list of all Plugins using:
`{COMMAND_HANDLER}help`
"""

@Client.on_message(filters.command("plugins", COMMAND_HANDLER) & filters.me)
async def list_plugins(c: Client, m: Message):
    # Some Variables
    mods = ""
    mod_num = 0
    # Some Variables
    plugins = list(HELP_COMMANDS.keys())
    for plug in plugins:
        mods += f"`{plug}`\n"
        mod_num += 1
    all_plugins = f"<b><u>{mod_num}</u> Modules Currently Loaded:</b>\n\n" + mods
    await m.edit_text(all_plugins)
    return


@Client.on_message(filters.command("help", COMMAND_HANDLER) & filters.me)
async def help_me(c: Client, m: Message):
    if len(m.command) == 1:
        await m.edit_text(HELP_DEFAULT)
    elif len(m.command) == 2:
        module_name = m.text.split(None, 1)[1]
        try:
            HELP = f"**Help for __{module_name}__**\n\n" + HELP_COMMANDS[module_name]
            await m.reply_text(HELP, parse_mode="md", disable_web_page_preview=True)
            await m.delete()
        except Exception as ef:
            await m.edit_text(f"<b>Error:</b>\n\n{ef}")
    else:
        await m.edit_text(f"Use `{COMMAND_HAND_LER}help` to view help")
    return
