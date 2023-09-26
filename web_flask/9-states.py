#!/usr/bin/python3
"""starts a Flask web application.

Example:
    $ python3 -m web_flask.9-states

"""
from flask import Flask, render_template
from models import storage
from models.state import State

# Create a Flask application instance
app = Flask(__name__)


@app.teardown_appcontext
def after_request(_):
    """remove the current SQLAlchemy Session.
    """
    storage.close()


# Define a route for the root URL ("/states/<id>")
@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state(id=None):
    """"display list of all state cities objects if id is specified,
        all states otherwise.

    Returns:
        str.

    """
    if id:
        context = storage.all(State).get('State.' + id)
    else:
        context = sorted(
                storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', context=context, id=id)


if __name__ == '__main__':
    # Start the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0')
