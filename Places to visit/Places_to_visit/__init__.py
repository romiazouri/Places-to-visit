"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Places_to_visit.views
