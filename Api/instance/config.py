# DEBUG  = True
class Config(object):
    """
    Common configurations
    """
    DEBUG = True
    SECRET = "python4life"


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

class TestingConfig(Config):
    """
    Production configurations
    """
    DEBUG = True
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig
}
