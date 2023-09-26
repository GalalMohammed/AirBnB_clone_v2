#!/usr/bin/python3
"""starts a Flask web application.

Example:
    $ python3 -m web_flask.7-states_list

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


# Define a route for the root URL ("/states_list")
@app.route('/states_list', strict_slashes=False)
def states_list():
    """"display list of all states objects.

    Returns:
        str.

    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    # Start the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0')
