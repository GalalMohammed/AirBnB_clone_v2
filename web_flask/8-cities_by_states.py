#!/usr/bin/python3
"""starts a Flask web application.

Example:
    $ python3 -m web_flask.8-cities_by_states

"""
from flask import Flask, render_template
from models import storage
from models.state import State

# Create a Flask application instance
app = Flask(__name__)


@app.teardown_appcontext
def after_request(exception):
    """remove the current SQLAlchemy Session.
    """
    storage.close()


# Define a route for the root URL ("/cities_by_states")
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """"display list of all states objects with their cities.

    Returns:
        str.

    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    # Start the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0')
