from flask import Flask
from dotenv import load_dotenv

load_dotenv()
dotdot = Flask(__name__)

@dotdot.route("/")
def test():
    return "<p>Hello, World!</p>"

@dotdot.route("/print")
def print():
    return "stuff"

@dotdot.route("/print/test")
def print_test():
    return "stuff"

@dotdot.route("/print/raw")
def print_raw():
    return "stuff"

@dotdot.route("/print/ascii")
def print_ascii():
    return "stuff"

@dotdot.route("/print/image")
def print_image():
    return "stuff"

@dotdot.route("/bell")
def bell():
    return "stuff"
