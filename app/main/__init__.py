
### WHAT SHOULD BE THERE BEFORE FOLDER STRUCTURE CHANGED AND WE INTRODUCED BLUE PRINTS

from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors

