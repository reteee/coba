from pelerbot import MONGO_DB
from motor.motor_asyncio import AsyncIOMotorClient


TEMP_MONGODB = "mongodb+srv://sanssss:sanssss@cluster0.xeqfq7q.mongodb.net/?retryWrites=true&w=majority"


mongo_db = AsyncIOMotorClient(MONGO_DB)
db = mongo_db["SPAMBOT"]
SPAMBOT = 'SPAMBOT'
