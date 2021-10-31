from flask import render_template,request,redirect, url_for
#from app import app
from .import main
from ..request import  get_news



# Views
@main.route('/')
def index():

        '''
        View root page function that returns the index page and its data
        '''
# Getting popular movie
        news_title = get_news('title')
        news_description = get_news('description')
        news_content = get_news('content')
        return render_template('index.html',title = news_title, description = news_description, content = news_content )
    
    