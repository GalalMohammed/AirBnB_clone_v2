#!/usr/bin/python3
"""starts a Flask web application.

Example:
    $ python3 -m web_flask.2-c_route

"""
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display 'Hello HBNB!'.

    Returns:
        str.
    
    """
    return "Hello HBNB!"


# Define a route for the root URL ("/hbnb") with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display 'HBNB'.

    Returns:
        str.

    """
    return "HBNB"


# Define a route for the root URL ("/c/<text>") with strict_slashes=False
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """"display 'C' followed by the value of text.
        '_' will be replaced with ' '.

    Args:
        text (str): value.

    Returns:
        str.

    """
    return "C " + text.replace('_', ' ')


if __name__ == '__main__':
    # Start the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0')
