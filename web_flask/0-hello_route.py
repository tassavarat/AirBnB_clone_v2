#!/usr/bin/python3
"""0-hello_route module"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Starts a Flask web application
    Return: Hello HBNB!
    """
    app.url_map.strict_slashes = False
    return "Hello HBNB!"


app.run(host='0.0.0.0')
