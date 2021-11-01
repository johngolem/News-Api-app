import unittest
from app.models import NewsSource



class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News_source Class
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_source = NewsSource("bbc-news","OP26: 'Window closing' to meet 1.5C warming target - Alok Sharma","The COP26 president has been addressing delegates on day one of the climate summit in Glasgow.","http://www.bbc.co.uk/news/uk-59110765","https://ichef.bbci.co.uk/news/1024/branded_news/0847/production/_121291120_cop26lead.jpg","021-10-31T13:07:22.7039942Z","By Sophie GallagherBBC News\r\nImage source, Press Association \r\nImage caption, Alok Sharma was addressing COP26 in Glasgow on Sunday morning\r\nThe window to keep within the 1.5 degree warming target \"i… [+2068 chars]")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))


