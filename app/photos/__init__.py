from flask import Blueprint

bp = Blueprint('photos', __name__)

# Routes module must be imported after blueprint is instantiated
# As routes is dependeng upon blueprint existing
# This produces a PEP8 warning from http://pep8online.com/
# but not via PyCharm.  This is required for proper app function
from app.photos import routes
