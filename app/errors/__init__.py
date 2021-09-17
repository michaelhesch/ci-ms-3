from flask import Blueprint

bp = Blueprint('errors', __name__)

# Handlers module must be imported after blueprint is instantiated
# As handlers is dependeng upon blueprint existing
# This produces a PEP8 warning from http://pep8online.com/
# but not via PyCharm.  This is required for proper app function
from app.errors import handlers
