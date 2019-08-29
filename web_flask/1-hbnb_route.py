#!/usr/bin/python3
"""1-hbnb_route module"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Starts a Flask web application
    Return: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Starts a Flask web application
    Return: HBNB
    """
    return "HBNB"


app.run(host='0.0.0.0')
