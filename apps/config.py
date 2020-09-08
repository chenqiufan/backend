from redis import StrictRedis

SECRET_KEY = "n1u0gpHMgW38x0Qm3p3Og4uvE9cLj2QbtoDays3+4KHpu374xJnd3KICtn+4mGGc"

# mysql
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zj122900@118.178.143.47:3306/phosphor?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# reids
REDIS_HOST = "118.178.143.47"
REDIS_POST = 6379

# session
SESSION_TYPE = 'redis'
# 开启签名Å
SESSION_USE_SIGNER = True

# session redis
SESSION_DB = 6
SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_POST,db=SESSION_DB)

SESSION_PERMANENT = False
# 过期时间
PERMANENT_SESSION_LIFETIME = 86400*2

# debug
DEBUG = True
