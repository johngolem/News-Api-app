from app import app
from flask import render_template



@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    message="newsapi website"
    return render_template('index.html', message=message)