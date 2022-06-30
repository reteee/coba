from pelerbot.db import mongodb

gbun = mongodb.gbun


async def gban_user(user, reason="#GBanned"):
    user.id = int(user)
    gbuned = await gbun.find_one({"user": user.id})
    if gbuned:
        return True
    else:
        await gbun.insert_one({"user": user.id, "reason": reason})


async def ungban_user(user):
    user.id = int(user)
    ungbuned = await gbun.find_one({"user": user.id})
    if ungbuned:
        await gbun.delete_one({"user": user.id})
    else:
        return False

    
async def get_gban_reason(user):
    user.id = int(user)
    pr_gbanned = await gbun.find_one({"user": user.id})
    if pr_gbanned:
        return pr_gbanned["reason_for_gban"]
    else:
        return None


async def gban_list():
    return [lo async for lo in gbun.find({})]


async def gban_info(user):
    kk = await gbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
