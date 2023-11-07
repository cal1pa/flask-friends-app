from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

# create server
app = Flask(__name__)
CORS(app)  # CORS IS USED TO FACILITATE COMMUNICATION BETWEEN THE SERVER AND THE CLIENT

# configure database
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://xivfcjxq:efgeL_IGeNxxRMHD9jNb9X4laEReMXv-@trumpet.db.elephantsql.com/xivfcjxq"
db = SQLAlchemy(app)

# as route uses app we import it after it being defined
from application import routes
