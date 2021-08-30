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
def print():
    content = flask.request.json.get('content')
    sanitized = tp.sanitize(content)
    sanlist = tp.eightyCharChunk(sanitized)
    for sanstring in sanlist:
        tp.toprint(sanstring)
    return "stuff\n"

@dotdot.route("/print/test", methods=['POST'])
def print_test():
    tp.toprint('hello world!')
    return "stuff\n"

@dotdot.route("/print/raw", methods=['POST'])
def print_raw():
    content = flask.request.json.get('content')
    tp.toprint(content)
    return "stuff\n"

@dotdot.route("/print/ascii", methods=['POST'])
def print_ascii():
    content = flask.request.json.get('content')
    sanitized = tp.sanitize(content)
    asciii = word_to_ascii(phrase=sanitized, font_size=12, kerning=1).split('\n')
    for sanstring in asciii:
        if len(sanstring) > 80:
            raise CharacterLimitExceeded
        tp.toprint(sanstring)
    return "stuff\n"

@dotdot.route("/print/image")
def print_image():
    return "stuff\n"

@dotdot.route("/bell")
def bell():
    return "ding"
