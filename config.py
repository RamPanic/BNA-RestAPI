
""" Flask configuration. """

class Config:

    """ Base config """
    
    HOST = ""
    PORT = 5000
    
    JSON_SORT_KEYS = False

class ProdConfig(Config):

    """ Base config production """

    ENV = 'production'
    DEBUG = False

class DevConfig(Config):

    """ Base config development """
    
    ENV = 'development'
    DEBUG = True


config = {
 
    'dev': DevConfig,
    'prod': ProdConfig

}
