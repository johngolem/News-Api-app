import os
class Config:
    '''
    General configuration parent class
    '''
    #NEWS_API_KEY = 'c445d1b3d30e47cbbb9c199771e8d3a9'
    BBC_NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}'
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}