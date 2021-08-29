from flask import Flask
import flask
from dotenv import load_dotenv
import text_to_font as ttf
import toprint

load_dotenv()
dotdot = Flask(__name__)

@dotdot.route("/")
def test():
    return "<p>Hello, World!</p>"

@dotdot.route("/print", methods=['GET', 'POST'])
def print():
    if flask.request.method == 'POST':
        content = flask.request.json.get('content')
        sanitized = toprint.sanitize(content)
        sanlist = toprint.eightyCharChunk(sanitized)
        for sanstring in sanlist:
            toprint.toprint(sanstring)
    return "stuff"

@dotdot.route("/print/test")
def print_test():
    return "stuff\n"

@dotdot.route("/print/raw", methods=['GET', 'POST'])
def print_raw():
    if flask.request.method == 'POST':
        content = str(flask.request.json.get('content'))
        toprint.toprint(content)
    return "stuff\n"

@dotdot.route("/print/ascii")
def print_ascii():
    return "stuff\n"

@dotdot.route("/print/image")
def print_image():
    return "stuff\n"

@dotdot.route("/bell")
def bell():
    return "stuff\n"
