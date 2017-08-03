from flask import Flask
from controllers import nothing

application = Flask(__name__)

@application.route("/")
nothing.hello()