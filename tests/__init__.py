from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app)

# expose `talisman` to allow importing it elsewhere
__all__ = ['talisman', 'app']

talisman = talisman