import route as route
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return 'Welcome to the index page    <a href="/who"> Ve aqui </a>  '


@app.route("/who")
def who():
    return 'Who are you?  <a href="/"> Return </a>'
