from . import sans

rbans = sans["RBAN"]


async def rsans(user, reason="#MATHERCHOD"):
    await rbans.insert_one({"user": user, "reason": reason})


async def runsans(user):
    await rbans.delete_one({"user": user})


async def rban_list():
    return [lo async for lo in rbans.find({})]


async def sansub_info(user):
    kk = await rbans.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]