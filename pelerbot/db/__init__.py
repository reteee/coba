from . import MONGO_DB
from motor.motor_asyncio import AsyncIOMotorClient

mongo_db = AsyncIOMotorClient(MONGO_DB)
db = mongo_db["SPAMBOT"]
SPAMBOT = 'SPAMBOT'
