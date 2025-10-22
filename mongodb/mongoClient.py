from typing import Any
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017" # based url
DB_NAME = "rus"

client: MongoClient[Any] = MongoClient(MONGO_URI)
db = client[DB_NAME]

print(db)