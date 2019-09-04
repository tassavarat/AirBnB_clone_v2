#!/usr/bin/python3
"""8-cities_by_states module
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def states():
    """Displays HTML page
    H1 tag: States
    UL tag: List of all State objects in DBStorage sorted by name
    LI tag: Description of one State: <state.id>: <B><state.name></B>
    """
    return render_template("10-hbnb_filters.html",
                           data=storage.all(State).values())


@app.teardown_appcontext
def storage_close(var=None):
    """Removes current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
