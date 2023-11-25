from flask import render_template

from app import views

@views.route('/', methods=['GET','POST'])
def index():
    return render_template("templates/index.html")