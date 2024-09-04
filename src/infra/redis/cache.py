from redis.asyncio import Redis


class RedisClient:
    def __init__(self, host='172.25.203.181', port=6379, ttl=1000):
        self.__db = 0
        self.redis = Redis(host=host, port=port, db=self.__db, decode_responses=True)
        self.ttl = ttl

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db: int):
        self.__db = db

    async def set(self, key: str, value: str):
        await self.redis.set(key, value, ex=self.ttl)

    async def get(self, key: str):
        return await self.redis.get(key)

    async def close(self):
        await self.redis.close()
