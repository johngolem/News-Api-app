import urllib.request,json
from .models import NewsSource



#Fetch API key
api_key = None

#Fetch News Base Url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BBC_NEWS_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_result = None
        
        if get_news_response['sources']:
            news_result_list = get_news_response['sources']
            news_result = process_results(news_result_list)
    return news_result



def process_results(news_list):
    '''
    Function that processes the news sources result and transform them to a list of objects
    Args:
        sources_list: a list of dictionaries that contain news sources details
    Returns:
        sources_result: a list of news sources objects
    '''
    news_result = []
    for new_item in news_list:
        id = new_item.get('id')
        title = new_item.get('title')
        description = new_item.get('description')
        url = new_item.get('url')
        urlToImage = new_item.get('urlToImage')
        publishedAt = new_item.get('publishedAt')
        content = new_item.get('content')
        if url:
            news_object = NewsSource(id,title,description,url,urlToImage,publishedAt,content)
            news_result.append(news_object)
    return news_result
