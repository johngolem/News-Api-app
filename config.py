class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = 'c445d1b3d30e47cbbb9c199771e8d3a9'
    BBC_NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}'
    #BBC_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    #ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'
    #NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
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