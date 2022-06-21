import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pelerbot.plugins import ALL_PLUGINS
from pelerbot.utils.basic import *
from pelerbot import *


heading = "──「 **{0}** 」──\n\n"


@Client.on_message(filters.command("help", COMMAND_HANDLER) & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command

    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        all_commands = ""
        all_commands += "Please specify which module you want help for!! \nUsage: `.help [module_name]`\n\n"
        
        ac = PrettyTable
        ac.header = False
        ac.title = "👉🏽Peler Modules👈🏽"
        ac.align = "l"
        

        for x in split_list(sorted(HELP_COMMANDS.keys()), 3):
            ac.add_row([x[0], x[1] if len(x) >= 3 else None])
               

        await message.edit(f"```{str(ac)}```")
        
    if help_arg:
        if help_arg in HELP_COMMANDS:
            commands: dict = HELP_COMMANDS[help_arg]
            this_command = "<b>Help For Command</b>\n"
            this_command += heading.format(str(help_arg)).upper()

            for x in commands:
                this_command += f"~➣ `{str(x)}`\n```{str(commands[x])}```\n"

            await message.edit(this_command, parse_mode="markdown")
        else:
            await message.edit(
                "`Please specify a valid module name.`", parse_mode="markdown"
            )

    await asyncio.sleep(200)
    await message.delete()


def add_command_help(module_name, commands):
    """
    Adds a modules help information.
    :param module_name: name of the module
    :param commands: list of lists, with command and description each.
    """

    # Key will be group name
    # values will be dict of dicts of key command and value description

    if module_name in HELP_COMMANDS.keys():
        command_dict = HELP_COMMANDS[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    HELP_COMMANDS[module_name] = command_dict
