from . import sans

gmut = sans["GMUTE"]


async def is_gmuted(sender_id):
    kk = await gmut.find_one({"sender_id": sender_id})
    if not kk:
        return False
    else:
        return True


async def gmute(sender_id, reason="#GMuted"):
    await gmut.insert_one({"sender_id": sender_id, "reason": reason})


async def ungmute(sender_id):
    await gmut.delete_one({"sender_id": sender_id})