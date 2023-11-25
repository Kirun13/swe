from flask import Blueprint, render_template, request
from . import session

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    return render_template("templates/home.html")