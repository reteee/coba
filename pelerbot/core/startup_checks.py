import asyncio
from pyrogram.errors import YouBlockedUser
from pelerbot import SANSBOT
from pelerbot.core.database.confdb import set_log_channel, get_log_channel, set_arq_key, get_arq_key
from config import *

# Log Channel Checker
async def check_or_set_log_channel():
    try:
        al_log_channel = await get_log_channel()
        if al_log_channel:
            return [True, al_log_channel]
        else:
            log_channel = await SANSBOT.create_channel(title="Peler Userbot Logs", description="Logs of your Peler Userbot")
            welcome_to_nexaub = f"""
**Heya! I am Peler Userbot**
 If you found any error, bug or even a Feature Request please report it at **@PelerSupport**
**⌲ Quick Start,**
If you don't know how to use this Userbot please send `{Config.CMD_PREFIX}help` in any chat. It'll show all plugins your userbot has. You can use those plugin names to get info about how to use it. Also check out.
 **~ Peler **"""
            log_channel_id = log_channel.id
            await set_log_channel(log_channel_id)
            await SANSBOT.send_message(chat_id=log_channel_id, text=welcome_to_nexaub, disable_web_page_preview=True)
            return [True, log_channel_id]
    except Exception as e:
        print(f"Error \n\n{e} \n\nPlease check all variables and try again! \nReport this with logs at @NexaBotSupport if the problem persists!")
        exit()


# ARQ API KEY Checker
async def check_arq_api():
    try:
        try:
            await SANSBOT.send_message("ARQRobot", "/start")
        except YouBlockedUser:
            await SANSBOT.unblock_user("ARQRobot")
            await asyncio.sleep(0.2)
            await SANSBOT.send_message("ARQRobot", "/start")
        await asyncio.sleep(0.5)
        await SANSBOT.send_message("ARQRobot", "/get_key")
        get_h = (await SANSBOT.get_history("ARQRobot", 1))[0]
        g_history = get_h.text
        if "X-API-KEY:" not in g_history:
            peler_user = await SANSBOT.get_me()
            arq_acc_name = peler_user.first_name if peler_user.first_name else f"Unknown_{peler_user.id}"
            await asyncio.sleep(0.4)
            await SANSBOT.send_message("ARQRobot", f"{arq_acc_name}")
            await asyncio.sleep(0.3)
            gib_history = (await SANSBOT.get_history("ARQRobot", 1))[0]
            g_history = gib_history.text
            arq_api_key = g_history.replace("X-API-KEY: ", "")
        else:
            arq_api_key = g_history.replace("X-API-KEY: ", "")
        is_arqed = await get_arq_key()
        if is_arqed is None:
            await set_arq_key(arq_api_key)
        else:
            pass
    except Exception as e:
        print(f"Error \n\n{e} \n\nThere was a problem while obtaining ARQ API KEY. However you can set it manually. Send, \n{Config.CMD_PREFIX}setvar ARQ_API_KEY your_api_key_here")