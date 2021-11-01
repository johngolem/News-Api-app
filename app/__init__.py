from flask import Flask
from config import config_options

def create_app(config_name):
    app = Flask(__name__)
    

   
    
    #Registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #setting config
    from .request import configure_request
    configure_request(app)
    
    return app