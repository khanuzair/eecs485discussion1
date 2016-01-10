from flask import *
from extensions import mysql

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    return render_template("index.html")

@main.route('/Hello')
def hello():
	return "Hello World!"
