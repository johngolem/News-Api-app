import urllib.request,json
from .models import NewsSouce

#....
# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BBC_NEWS_API_BASE_URL']

#....