from . import sans

conf = sans["config_db"]

# Database for log channel
async def set_log_channel(tgcc_id):
    log_chanel_id = tgcc_id
    p_log_c_id = await conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if p_log_c_id:
        return True
    else:
        await conf.insert_one({"_id": "LOG_CHANNEL_ID", "conf": log_chanel_id})

async def get_log_channel():
    log_channel = await conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if log_channel:
        return int(log_channel["conf"])
    else:
        return None

# Database for custom alive message

async def set_custom_alive_msg(a_text=None):
    if a_text is None:
        alive_msg = "Hi, I'm Using Peler Userbot"
    else:
        alive_msg = a_text
    p_alive_msg = await conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if p_alive_msg:
        await conf.update_one({"_id": "CUSTOM_ALIVE_MSG"}, {"$set": {"conf": alive_msg}})
    else:
        await conf.insert_one({"_id": "CUSTOM_ALIVE_MSG", "conf": alive_msg})

async def get_custom_alive_msg():
    alive_msg = await conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if alive_msg:
        return alive_msg["conf"]
    else:
        return None

# Database for arq client
async def set_arq_key(arq_key):
    p_arq_key = await conf.find_one({"_id": "ARQ_API_KEY"})
    if p_arq_key:
        await conf.update_one({"_id": "ARQ_API_KEY"}, {"$set": {"conf": arq_key}})
    else:
        await conf.insert_one({"_id": "ARQ_API_KEY", "conf": arq_key})

async def get_arq_key():
    p_arq = await conf.find_one({"_id": "ARQ_API_KEY"})
    if p_arq:
        return p_arq["conf"]
    else:
        None

# Database for set cutom variable
async def set_custom_var(var, value):
    p_variable = await conf.find_one({"_id": var})
    if p_variable:
        await sans_conf.update_one({"_id": var}, {"$set": {"conf": value}})
    else:
        await conf.insert_one({"_id": var, "conf": value})

async def get_custom_var(var):
    custom_var = await conf.find_one({"_id": var})
    if not custom_var:
        return None
    else:
        g_custom_var = custom_var["conf"]
        return g_custom_var