#!/usr/bin/python3
"Develop a Simple API using Python with Flask"

from flask import Flask
from flask import jsonify
from flask import request
import json

"""
This line imports the necessary modules from the Flask framework:
- Flask: The main Flask class used to create a Flask application instance.
- jsonify: A helper function to convert Python data structures to JSON format.
- request: An object that represents the incoming HTTP request.
"""

# In-memory data store
users = {}
"""
This is an in-memory data store (a Python dictionary) that holds user data.

"""


app = Flask(__name__)
"""
This line creates an instance of the Flask application using the Flask class.
The __name__ parameter is a Python built-in variable that represents the name
of the current module. This is a common convention in Flask applications, as
it helps Flask determine the root path of the application.
"""


@app.route('/')   # Creating Your First Endpoint
def home():
    text = "Welcome to the Flask API!"
    return text
    """
    This defines a route for the root URL (/) using the @app.route decorator.
    The home() function is associated with this route and returns the string
    "Welcome to the Flask API!" when the root URL is accessed.
    """


@app.route('/data')   # Serving JSON Data
def get_data():
    return jsonify(list(users.keys))
    """
    This defines a route for the /data URL.
    The get_data() function is associated with this route
    and returns a JSON response containing a list of all
    user objects using jsonify(list(users.values())).
    """


@app.route('/status')   # Expanding Your API
def get_status():
    return "OK"
    """
    This defines a route for the /status URL. The get_status() function is
    associated with this route and returns the string "OK".
    """


@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404
        """
        This defines a route for the /users/<username> URL,
        where <username> is a dynamic part of the URL path.
        The get_user(username) function is associated with this route
        and returns a JSON response containing the user object corresponding
        to the provided username. If the username is not found in the
        users dictionary, an empty dictionary {} is returned.
        """


# Handling POST Requests
@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.json or "username" not in request.json:
        return jsonify({"error": "Username is required"}), 400

    new_user = request.get_json()
    username = new_user['username']
    users[username] = {
        "username": user_data.get("username"),
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201
    """
    This defines a route for the /add_user URL that accepts POST requests.
    The add_user() function is associated with this route
    and performs the following tasks:
    1. new_user = request.get_json() parses the incoming JSON data
    from the request body.
    2. username = new_user['username'] extracts the username from
    the parsed JSON data.
    3. users[username] = new_user adds the new user
    to the users dictionary using the username as the key.
    4. return jsonify(new_user), 201 returns a JSON response
    containing the added user data and a 201 status code (Created).
    """


if __name__ == "__main__":
    app.run()
    """
    This is a Python idiom that checks if the script
    is being run directly (not imported as a module).
    If this condition is true, it starts the Flask
    development server by calling app.run().
    The development server will run until
    you stop it manually (e.g., by pressing Ctrl+C in the terminal).
    """
