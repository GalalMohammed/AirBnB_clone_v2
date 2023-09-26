#!/usr/bin/python3
"""starts a Flask web application.

Example:
    $ python3 -m web_flask.0-hello_route

"""
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == '__main__':
    # Start the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0')
