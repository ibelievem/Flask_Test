# __author__: xws    
# time: 2019/8/31 2:03


# 线上环境和开发环境相同的配置放在此处
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "asdasfsdf"
    DATABASE_URI = 'sqlite://:memory:'


# 线上环境
class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True


# 测试环境
class TestingConfig(Config):
    TESTING = True
