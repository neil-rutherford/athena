from flask import Flask
from app.db_utils import create_db

create_db()
app = Flask(__name__)

from app import routes
