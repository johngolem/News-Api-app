class NewsSource:
    '''
    Movie class to define BBCnews Objects
    '''

    def __init__(self,id,title,descritpion,url,urlToImage,publishedAt,content):
        self.id =id
        self.title = title
        self.descritpion = descritpion
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content