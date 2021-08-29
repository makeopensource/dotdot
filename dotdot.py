from flask import Flask
import flask
from dotenv import load_dotenv
from text_to_font.transformations import word_to_ascii
import toprint as tp

load_dotenv()
dotdot = Flask(__name__)


class CharacterLimitExceeded(Exception):
    """Printer exceeded line width of 80 characters"""
    pass


@dotdot.route("/")
def test():
    return "<p>Hello, World!</p>"

@dotdot.route("/print", methods=['POST'])
def print(response):
    content = flask.request.json.get('content')
    sanitized = tp.sanitize(content)
    sanlist = tp.eightyCharChunk(sanitized)
    for sanstring in sanlist:
        tp.toprint(sanstring)
    return response.status

@dotdot.route("/print/test", methods=['POST'])
def print_test(response):
    tp.toprint('hello world!')
    return response.status

@dotdot.route("/print/raw", methods=['POST'])
def print_raw(response):
    content = flask.request.json.get('content')
    tp.toprint(content)
    return response.status

@dotdot.route("/print/ascii", methods=['POST'])
def print_ascii(response):
    content = flask.request.json.get('content')
    sanitized = tp.sanitize(content).split('\n')
    for sanstring in sanitized:
        if len(sanstring) > 65:
            raise CharacterLimitExceeded
        tp.toprint(sanstring)
    return response.status

@dotdot.route("/print/image")
def print_image(response):
    return "stuff"

@dotdot.route("/bell")
def bell(response):
    return "ding"
