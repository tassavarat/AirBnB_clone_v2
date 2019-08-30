#!/usr/bin/python3
"""1-hbnb_route module
Starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Return: Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Return: HBNB"""
    return "HBNB"


app.run(host='0.0.0.0')
