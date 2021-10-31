#from flask import Blueprint
#main = Blueprint('main',__name__)
#from . import views,errors


### WHAT SHOULD BE THERE BEFORE FOLDER STRUCTURE CHANGED AND WE INTRODUCED BLUE PRINTS


from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')



from app import views