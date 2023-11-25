import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

load_dotenv()


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("jwt-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    

CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from website.apis import api

from website.views import views

app.register_blueprint(api, url_prefix='/')
app.register_blueprint(views, url_prefix='/')




if __name__ == "__main__":
    app.run(debug=True)