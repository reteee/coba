import os
import time
import requests
import re
import asyncio
import importlib
from datetime import datetime
from aiohttp import ClientSession
from pyrogram import Client, filters, idle
from pyrogram.types import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler


# the logging things
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

aiohttpsession = ClientSession()


# Configuration Things
if bool(os.environ.get("ENV", False)):


LOGGER = True
APP_ID = int(os.environ.get("APP_ID", "13135189"))
API_HASH = os.environ.get("API_HASH", "42186d1f48bd4d3c8233b269763b1361")
MAX_MESSAGE_LENGTH = 4096
COMMAND_HANDLER = os.environ.get("COMMAND_HANDLER", ["~", "!", "*"])
TMP_DOWNLOAD_DIRECTORY = os.environ.get(
        "TMP_DOWNLOAD_DIRECTORY", "/root/pelerbot/Downloads"
    )
OFFICIAL_UPSTREAM_REPO = os.environ.get(
        "OFFICIAL_UPSTREAM_REPO", None
    )
DATABASE_URL = os.environ.get("DATABASE_URL", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
OWNER_ID = int(os.environ.get("OWNER_ID", "5372076947"))
SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
TG_MAX_SELECT_LEN = int(os.environ.get("TG_MAX_SELECT_LEN", "100"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
OWNER_NAME = os.environ.get("OWNER_NAME", "Gaclexxx")
PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", "-1001773996149"))
LOG_GROUP = os.environ.get("LOG_GROUP", "-1001773996149")
PM_PERMIT = bool(os.environ.get("PM_PERMIT", False))
REMBG_API_KEY = os.environ.get("REMBG_API_KEY", None)
MEGANZ_PASSWORD = os.environ.get("MEGANZ_PASSWORD", None)
MEGANZ_EMAIL = os.environ.get("MEGANZ_EMAIL", None)
STRING_SESSION1 = os.environ.get("STRING_SESSION1", "BQCLtn1qIG49DC4xEzYfRBsNEEcLKuWjDIb4N4tZWh50ZhDzeLzQQ7x0Sgo3oLBhP168PRah-IhE1R01vITMs74qvUnoJ_SXwIDOxb3U3c9PJlX4en6JTt2WfZfq15cPUx9lDVEA-bTbMedYyC08-b83IFp0ls1nd3xph00hn3ztopvjvsjOFystEaLYTaYtNuFerrIRghjuR0uKz9Nc6CuH34Xmx2XLiwtvzvfPzaH-weUcPYOxPpXETNy6cyyuf_Y9fkdTOhVG7_ibWXCx_KoT-kDgCgwf_Xr_fNeUZpoSkK1Xd7NfLirpvHKxD2iMb7sFx9NiC0zHVaIbTRwFV2OiAAAAAUAzY5MA")
STRING_SESSION2 = os.environ.get("STRING_SESSION2", "BQBCHpVUdfkP7lydbY9g_fekagIleM4Pwyg_nkDf6gjz4VCvX7q26xMr0qwLdrd5v1BF_x1zyR_7MJkEoaAB7L5uOTaGhBQweFv1gkQDo5d3m2C2igU1flY7asBx0ge3S0SAnyLfG0DaqM5dPnj7NaIT_LubAAgq7RJRJ7LVk5-INtBuGJu8kIDFCGBvhbnYU4EMn-vLrIplYi434D0kWyJeXy_wjYKjvsexA9j4NZ0JAbmsl3IUDWuV4AK4YaeTIeGiLF1Ywi-YGQ1Ggsuia0MMyL-V69vqVlN3W5aq3Ts2QU7iD5EnkERUXsQu-0GJq5CfvHBKFSLXZFiKSEDvGOwWAAAAATOJJRMA")
STRING_SESSION3 = os.environ.get("STRING_SESSION3", "BQBdDdorx7074SzDFDCqRmgmXsGnjUnTxyjhHrFrotuuitLRupgOkF1u_6QZLVSvWCK0c3OA7zpUVbXcwpeHH8uR-PU5HfSBK6xB2sbWxAVJhNJtdbkYeGxQZr-81b-6yU4r5QGYBzcQiXAr-aglm_ZllPsWgoQKjP1mjJ68h4j3CXVakbqr36ZvSIKOKUtbI8Sj87rzrSbTFump5SdSQpnjsORxqqtsJgE8c_dxeN4aFetYBlsE-YCMZTs6jBIk0cMggM6pGys9dOV5SWtua5rBiD5QG-1mThj_tOF5xI9MozPRiq1VfK3iOPtbQVprmIpp3JelLj0qmnwV1HFoizNRAAAAAUYtUcsA")
STRING_SESSION4 = os.environ.get("STRING_SESSION4", "")
STRING_SESSION5 = os.environ.get("STRING_SESSION5", "")
STRING_SESSION6 = os.environ.get("STRING_SESSION6", "")
STRING_SESSION7 = os.environ.get("STRING_SESSION7", "")
STRING_SESSION8 = os.environ.get("STRING_SESSION8", "")
STRING_SESSION9 = os.environ.get("STRING_SESSION9", "")
STRING_SESSION10 = os.environ.get("STRING_SESSION10", "")
STRING_SESSION11 = os.environ.get("STRING_SESSION11", "")
STRING_SESSION12 = os.environ.get("STRING_SESSION12", "")
STRING_SESSION13 = os.environ.get("STRING_SESSION13", "")
STRING_SESSION14 = os.environ.get("STRING_SESSION14", "")
STRING_SESSION15 = os.environ.get("STRING_SESSION15", "")
STRING_SESSION16 = os.environ.get("STRING_SESSION16", "")
STRING_SESSION17 = os.environ.get("STRING_SESSION17", "")
STRING_SESSION18 = os.environ.get("STRING_SESSION18", "")
STRING_SESSION19 = os.environ.get("STRING_SESSION19", "")
STRING_SESSION20 = os.environ.get("STRING_SESSION20", "")
STRING_SESSION21 = os.environ.get("STRING_SESSION21", "")
STRING_SESSION22 = os.environ.get("STRING_SESSION22", "")
STRING_SESSION23 = os.environ.get("STRING_SESSION23", "")
STRING_SESSION24 = os.environ.get("STRING_SESSION24", "")
STRING_SESSION25 = os.environ.get("STRING_SESSION25", "")
STRING_SESSION26 = os.environ.get("STRING_SESSION26", "")
STRING_SESSION27 = os.environ.get("STRING_SESSION27", "")
STRING_SESSION28 = os.environ.get("STRING_SESSION28", "")
STRING_SESSION29 = os.environ.get("STRING_SESSION29", "")
STRING_SESSION30 = os.environ.get("STRING_SESSION30", "")
STRING_SESSION31 = os.environ.get("STRING_SESSION31", "")
STRING_SESSION32 = os.environ.get("STRING_SESSION32", "")
STRING_SESSION33 = os.environ.get("STRING_SESSION33", "")
STRING_SESSION34 = os.environ.get("STRING_SESSION34", "")
STRING_SESSION35 = os.environ.get("STRING_SESSION35", "")
STRING_SESSION36 = os.environ.get("STRING_SESSION36", "")
STRING_SESSION37 = os.environ.get("STRING_SESSION37", "")
STRING_SESSION38 = os.environ.get("STRING_SESSION38", "")
STRING_SESSION39 = os.environ.get("STRING_SESSION39", "")
STRING_SESSION40 = os.environ.get("STRING_SESSION40", "")
STRING_SESSION41 = os.environ.get("STRING_SESSION41", "")
STRING_SESSION42 = os.environ.get("STRING_SESSION42", "")
STRING_SESSION43 = os.environ.get("STRING_SESSION43", "")
STRING_SESSION44 = os.environ.get("STRING_SESSION44", "")
STRING_SESSION45 = os.environ.get("STRING_SESSION45", "")
STRING_SESSION46 = os.environ.get("STRING_SESSION46", "")
STRING_SESSION47 = os.environ.get("STRING_SESSION47", "")
STRING_SESSION48 = os.environ.get("STRING_SESSION48", "")
STRING_SESSION49 = os.environ.get("STRING_SESSION49", "")
STRING_SESSION50 = os.environ.get("STRING_SESSION50", "")

LOGGER = logging.getLogger(__name__) 


HELP_COMMANDS = {}


def load_cmds(ALL_PLUGINS):
    for oof in ALL_PLUGINS:
        if oof.lower() == "help":
            continue
        imported_module = importlib.import_module("pelerbot.plugins." + oof)
        if not hasattr(imported_module, "__PLUGIN__"):
            imported_module.__PLUGIN__ = imported_module.__name__

        if not imported_module.__PLUGIN__.lower() in HELP_COMMANDS:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one"
            )

        if hasattr(imported_module, "__help__") and imported_module.__help__:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module.__help__
    return "Done Loading Plugins and Commands!"

bottime = time.time()
  
if not STRING_SESSION1:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

if ALIVE_IMG:
    ALIVE_PIC = ALIVE_IMG
else: 
    ALIVE_PIC = 'https://telegra.ph/file/36af1236a81eaf4c12c17.jpg'

if MONGO_DB:
    MONGO_DB = MONGO_DB
else: 
    MONGO_DB = "mongodb+srv://erte:wakwaw123@botmusic.kgdrx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

if LOG_GROUP:
    Owner = LOG_GROUP
else:
    Owner = -1001577751864
  

if STRING_SESSION1:
    bot1 = Client(session_name= STRING_SESSION1, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot1 = None

if STRING_SESSION2:
    bot2 = Client(session_name= STRING_SESSION2, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot2 = None

if STRING_SESSION3:
    bot3 = Client(session_name= STRING_SESSION3, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot3 = None

if STRING_SESSION4:
    bot4 = Client(session_name= STRING_SESSION4, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot4 = None

if STRING_SESSION5:
    bot5 = Client(session_name= STRING_SESSION5, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot5 = None

if STRING_SESSION6:
    bot6 = Client(session_name= STRING_SESSION6, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot6 = None

if STRING_SESSION7:
    bot7 = Client(session_name= STRING_SESSION7, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot7 = None

if STRING_SESSION8:
    bot8 = Client(session_name= STRING_SESSION8, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot8 = None

if STRING_SESSION9:
    bot9 = Client(session_name= STRING_SESSION9, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot9 = None

if STRING_SESSION10:
    bot = Client(session_name= STRING_SESSION10, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot = None

if STRING_SESSION11:
    bot11 = Client(session_name= STRING_SESSION11, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot11 = None

if STRING_SESSION12:
    bot12 = Client(session_name= STRING_SESSION12, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot12 = None

if STRING_SESSION13:
    bot13 = Client(session_name= STRING_SESSION13, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot13 = None

if STRING_SESSION14:
    bot14 = Client(session_name= STRING_SESSION14, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot14 = None

if STRING_SESSION15:
    bot15 = Client(session_name= STRING_SESSION15, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot15 = None

if STRING_SESSION16:
    bot16 = Client(session_name= STRING_SESSION16, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot16 = None

if STRING_SESSION17:
    bot17 = Client(session_name= STRING_SESSION17, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot17 = None

if STRING_SESSION18:
    bot18 = Client(session_name= STRING_SESSION18, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot18 = None

if STRING_SESSION19:
    bot19 = Client(session_name= STRING_SESSION19, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot19 = None

if STRING_SESSION20:
    bot20 = Client(session_name= STRING_SESSION20, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot20 = None

if STRING_SESSION21:
    bot21 = Client(session_name= STRING_SESSION21, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot21 = None

if STRING_SESSION22:
    bot22 = Client(session_name= STRING_SESSION22, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot22 = None

if STRING_SESSION23:
    bot23 = Client(session_name= STRING_SESSION23, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot23 = None

if STRING_SESSION24:
    bot24 = Client(session_name= STRING_SESSION24, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot24 = None

if STRING_SESSION25:
    bot25 = Client(session_name= STRING_SESSION25, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot25 = None

if STRING_SESSION26:
    bot26 = Client(session_name= STRING_SESSION26, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot26 = None

if STRING_SESSION27:
    bot27 = Client(session_name= STRING_SESSION27, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot27 = None

if STRING_SESSION28:
    bot28 = Client(session_name= STRING_SESSION28, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot28 = None

if STRING_SESSION29:
    bot29 = Client(session_name= STRING_SESSION29, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot29 = None

if STRING_SESSION30:
    bot30 = Client(session_name= STRING_SESSION30, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot30 = None

if STRING_SESSION31:
    bot31 = Client(session_name= STRING_SESSION31, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot31 = None

if STRING_SESSION32:
    bot32 = Client(session_name= STRING_SESSION32, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot32 = None

if STRING_SESSION33:
    bot33 = Client(session_name= STRING_SESSION33, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot33 = None

if STRING_SESSION34:
    bot34 = Client(session_name= STRING_SESSION34, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot34 = None

if STRING_SESSION35:
    bot35 = Client(session_name= STRING_SESSION35, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot35 = None

if STRING_SESSION36:
    bot36 = Client(session_name= STRING_SESSION36, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot36 = None

if STRING_SESSION37:
    bot37 = Client(session_name= STRING_SESSION37, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot37 = None

if STRING_SESSION38:
    bot38 = Client(session_name= STRING_SESSION38, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot38 = None

if STRING_SESSION39:
    bot39 = Client(session_name= STRING_SESSION39, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot39 = None

if STRING_SESSION40:
    bot40 = Client(session_name= STRING_SESSION40, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot40 = None

if STRING_SESSION41:
    bot41 = Client(session_name= STRING_SESSION41, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot41 = None

if STRING_SESSION42:
    bot42 = Client(session_name= STRING_SESSION42, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot42 = None

if STRING_SESSION43:
    bot43 = Client(session_name= STRING_SESSION43, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot43 = None

if STRING_SESSION44:
    bot44 = Client(session_name= STRING_SESSION44, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot44 = None

if STRING_SESSION45:
    bot45 = Client(session_name= STRING_SESSION45, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot45 = None

if STRING_SESSION46:
    bot46 = Client(session_name= STRING_SESSION46, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot46 = None

if STRING_SESSION47:
    bot47 = Client(session_name= STRING_SESSION47, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot47 = None

if STRING_SESSION48:
    bot48 = Client(session_name= STRING_SESSION48, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot48 = None

if STRING_SESSION49:
    bot49 = Client(session_name= STRING_SESSION49, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot49 = None

if STRING_SESSION50:
    bot50 = Client(session_name= STRING_SESSION50, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="modules"))
else:
    bot50 = None



scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

if bot1:
    bot1.start()
    bot1.join_chat("logsku")
if bot2:
    bot2.start()
    bot2.join_chat("logsku")
if bot3:
    bot3.start()
    bot3.join_chat("logsku")
if bot4:
    bot4.start()
    bot4.join_chat("logsku")
if bot5:
    bot5.start()
    bot5.join_chat("logsku")
if bot6:
    bot6.start()
    bot6.join_chat("logsku")
if bot7:
    bot7.start()
    bot7.join_chat("logsku")
if bot8:
    bot8.start()
    bot8.join_chat("logsku")
if bot9:
    bot9.start()
    bot9.join_chat("logsku")
if bot:
    bot.start()
    bot.join_chat("logsku")
if bot11:
    bot11.start()
    bot11.join_chat("logsku")
if bot12:
    bot12.start()
    bot12.join_chat("logsku")
if bot13:
    bot13.start()
    bot12.join_chat("logsku")
if bot14:
    bot14.start()
    bot14.join_chat("logsku")
if bot15:
    bot15.start()
    bot15.join_chat("logsku")
if bot16:
    bot16.start()
    bot16.join_chat("logsku")
if bot17:
    bot17.start()
    bot17.join_chat("logsku")
if bot18:
    bot18.start()
    bot18.join_chat("logsku")
if bot19:
    bot19.start()
    bot19.join_chat("logsku")
if bot20:
    bot20.start()
    bot20.join_chat("logsku")
if bot21:
    bot21.start()
    bot21.join_chat("logsku")
if bot22:
    bot22.start()
    bot22.join_chat("logsku")
if bot23:
    bot23.start()
    bot23.join_chat("logsku")
if bot24:
    bot24.start()
    bot24.join_chat("logsku")
if bot25:
    bot25.start()
    bot25.join_chat("logsku")
if bot26:
    bot26.start()
    bot26.join_chat("logsku")
if bot27:
    bot27.start()
    bot27.join_chat("logsku")
if bot28:
    bot28.start()
    bot28.join_chat("logsku")
if bot29:
    bot29.start()
    bot29.join_chat("logsku")
if bot30:
    bot30.start()
    bot30.join_chat("logsku")
if bot31:
    bot31.start()
    bot31.join_chat("logsku")
if bot32:
    bot32.start()
    bot32.join_chat("logsku")
if bot33:
    bot33.start()
    bot33.join_chat("logsku")
if bot34:
    bot34.start()
    bot34.join_chat("logsku")
if bot35:
    bot35.start()
    bot35.join_chat("logsku")
if bot36:
    bot36.start()
    bot36.join_chat("logsku")
if bot37:
    bot37.start()
    bot37.join_chat("logsku")
if bot38:
    bot38.start()
    bot38.join_chat("logsku")
if bot39:
    bot39.start()
    bot39.join_chat("logsku")
if bot40:
    bot40.start()
    bot40.join_chat("logsku")
if bot41:
    bot41.start()
    bot41.join_chat("logsku")
if bot42:
    bot42.start()
    bot42.join_chat("logsku")
if bot43:
    bot43.start()
    bot43.join_chat("logsku")
if bot44:
    bot44.start()
    bot44.join_chat("logsku")
if bot45:
    bot45.start()
    bot45.join_chat("logsku")
if bot46:
    bot46.start()
    bot46.join_chat("logsku")
if bot47:
    bot47.start()
    bot47.join_chat("logsku")
if bot48:
    bot48.start()
    bot48.join_chat("logsku")
if bot49:
    bot49.start()
    bot49.join_chat("logsku")
if bot50:
    bot50.start()
    bot50.join_chat("logsku")

idle()

print("🎉 Successfully Deployed 🎉 @gaclexx")
print("Enjoy! Do visit @gaclexx")

