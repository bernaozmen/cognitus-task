import redis

class RedisCache():
    def __init__(self,host,port,db) -> None:
        self.r = redis.Redis(host=host, port=port, db=db, charset="utf-8", decode_responses=True)

    def setFromCache(self,b,t):
        self.r.set(b,t)

    def getFromCache(self,b,t):
        self.r.get(b,t)
