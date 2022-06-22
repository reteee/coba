import os
from pelerbot import MONGO_DB
import motor.motor_asyncio

mongo_db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = mongo_db["SPAMBOT"]
SPAMBOT = 'SPAMBOT'
