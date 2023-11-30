class BaseConfig:
    TESTING = False
    # normal configuration is that we're currently not testing

class DevelopmentConfig(BaseConfig):
    pass
# not sure, seems to mean 'break'? or return nothing?

class TestingConfig(BaseConfig):
    TESTING = True
# confirms that we're now in testing

class ProductionConfig(BaseConfig):
    pass

