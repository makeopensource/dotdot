from flask import Flask
from dotenv import load_dotenv

load_dotenv()
dotdot = Flask(__name__)

@dotdot.route("/")
def test():
    return "<p>Hello, World!</p>"
