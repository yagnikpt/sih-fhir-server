import os
from typing import TypedDict
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

client = AsyncMongoClient(os.getenv("DB_URL"))


class Movie(TypedDict):
    name: str
    year: int


async def get_db():
    try:
        database: AsyncDatabase[Movie] = client["fhir_records"]
        yield database
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise e


async def get_codesystem_collection(db):
    return db["codesystems"]


async def get_conceptmap_collection(db):
    return db["conceptmaps"]
