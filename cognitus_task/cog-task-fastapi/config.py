from dotenv import find_dotenv, load_dotenv
import os
import redis
load_dotenv(find_dotenv())

class Settings(object):
 PROJECT_NAME: str
 REDIS_URL = os.getenv("REDIS_URL", "localhost")
 REDIS_PORT = os.getenv("REDIS_PORT", 6379)
 REDIS_DB = os.getenv("REDIS_DB", 0)
 REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
 REDIS_URI: str
 AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID") 
 DATABASE_HOST = os.getenv("DATABASE_HOST", "")
 DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
 DATABASE_USER = os.getenv("DATABASE_USER", "")
 DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "")
 DATABASE_NAME = os.getenv("DATABASE_NAME", "")
 SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
 DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME
 )

settings = Settings()
settings.PROJECT_NAME = "Cognitus Multi-Label Classification Service"
REDIS_URI = 'redis://%s:%d/%d' % (settings.REDIS_URL, settings.REDIS_PORT, settings.REDIS_DB)
settings.REDIS_URI = REDIS_URI
rc = redis.Redis(settings.REDIS_URL)

