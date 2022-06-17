from helpers.SQL import sans

bann = sans["GBAN"]


async def gban_user(user, reason="#GBanned"):
    await bann.insert_one({"user": user, "reason": reason})


async def ungban_user(user):
    await bann.delete_one({"user": user})


async def gban_list():
    return [lo async for lo in bann.find({})]


async def gban_info(user):
    kk = await bann.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]