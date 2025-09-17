from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import os

class MongoDB:
    client: AsyncIOMotorClient = None
    engine: AIOEngine = None

    async def connect(self):
        self.client = AsyncIOMotorClient(os.getenv("DATABASE_URL"))
        self.engine = AIOEngine(client=self.client, database=os.getenv("DATABASE_NAME", "faststudy"))
        print("Connected to MongoDB.")

    async def close(self):
        self.client.close()
        print("Closed MongoDB connection.")

mongodb = MongoDB()
