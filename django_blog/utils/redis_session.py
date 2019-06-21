import redis

session = redis.Redis(host='redis', port=6379, db=0)

REDIS_CLIENT = redis.StrictRedis('redis', db=1, charset="utf-8", decode_responses=True)

