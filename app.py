import os
from flask import Flask, Blueprint
from dotenv import load_dotenv
from flask_cors import CORS


def registerBlueprints():
    api = Blueprint('api', __name__)
    app.register_blueprint(api, url_prefix='/')

    views = Blueprint('views', __name__)
    app.register_blueprint(views, url_prefix='/')


load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("jwt-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

registerBlueprints()

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)

