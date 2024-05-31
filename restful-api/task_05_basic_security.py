#!/usr/bin/python3
"API Security and Authentication Techniques"

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
# Importing password hashing functions from Werkzeug
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("admin_password"),
        "role": "admin"
    }
}
"""
This is an in-memory data store (a Python list) that holds user data. In this
example, it contains two users: an admin user and a regular user. The passwords
are hashed using the generate_password_hash function from werkzeug.security.
"""

app = Flask(__name__)  # Creating a Flask application instance
auth = HTTPBasicAuth()  # Creating an instance of HTTPBasicAuth


@auth.verify_password
def verify_password(username, password):
    """
    Callback function for Flask-HTTPAuth to
    verify the provided username and password.

    Args:
        username (str): The username provided for authentication.
        password (str): The password provided for authentication.

    Returns:
        str or None: Returns the username if
        the credentials are valid, otherwise returns None.
    """
    user = users.get(username)
    # Retrieve the user dictionary from
    # the users dictionary using the provided username
    if user and check_password_hash(user["password"], password):
        # If the user exists and the provided
        # password matches the hashed password
        return username
        # Return the username, indicating successful authentication
    return None
    # Return None, indicating authentication failure


@app.route("/")
def home():
    """
    Home route for the Flask API.

    This route is the default route for the Flask application.
    When a client accesses the root URL ("/"), this function
    is executed, and it returns a simple welcome message.

    Returns:
        str: A welcome message for the Flask API.
    """
    return "Welcome to the Flask API!"


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Route for basic authentication protected endpoint.

    This route is protected by basic authentication using Flask-HTTPAuth.
    Only authenticated users can access this route.

    Returns:
        str: A success message indicating that
        basic authentication was successful.
    """
    return "Basic Auth: Access Granted"

    jwt = JWTManager(app)
    """
    This line initializes the JWTManager with the Flask application instance.
    """


@app.route("/login", methods=["POST"])
def login():
    """
    Route for user login and JWT token generation.

    This route accepts a POST request with a JSON payload containing
    the username and password. If the credentials are valid, it generates
    and returns a JSON Web Token (JWT) access token.

    Request JSON Payload:
        {
            "username": "user1",
            "password": "password"
        }

    Returns:
        On success (200 OK):
            JSON response with the access token.
            {
                "access_token": "generated_access_token"
            }
        On failure (400 Bad Request):
            JSON response with an error message
            if username or password is missing.
            {
                "message": "Missing username or password"
            }
        On failure (401 Unauthorized):
            JSON response with an error message
            if the username or password is invalid.
            {
                "message": "Bad username or password"
            }
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Route for JWT authentication protected endpoint.

    This route is protected by JWT authentication using Flask-JWT-Extended.
    Only requests with a valid JWT access token can access this route.

    Returns:
        str: A success message indicating that
        JWT authentication was successful.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Route for admin-only access with role-based access control.

    This route is protected by JWT authentication using Flask-JWT-Extended.
    Only requests with a valid JWT access token and
    an 'admin' role can access this route.

    Returns:
        On success (200 OK):
            str: A success message indicating that admin access was granted.
        On failure (403 Forbidden):
            JSON response with an error message if
            the user does not have the 'admin' role.
            {
                "error": "Admin access required"
            }
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

    @jwt.unauthorized_loader
    def handle_unauthorized_error(err):
        """
        Error handler for unauthorized access with JWT authentication.

        This function is called when a request is made
        without a valid JWT access token.

        Args:
            err (Exception): The exception object raised by Flask-JWT-Extended.

        Returns:
            JSON response with an error message
            and a 401 Unauthorized status code.
            {
                "error": "Missing or invalid token"
            }
        """
        return jsonify({"error": "Missing or invalid token"}), 401

    @jwt.invalid_token_loader
    def handle_invalid_token_error(err):
        """
        Error handler for invalid JWT access tokens.

        This function is called when a request is made
        with an invalid JWT access token.

        Args:
            err (Exception): The exception object raised by Flask-JWT-Extended.

        Returns:
            JSON response with an error message
            and a 401 Unauthorized status code.
            {
                "error": "Invalid token"
            }
        """
        return jsonify({"error": "Invalid token"}), 401

    @jwt.expired_token_loader
    def handle_expired_token_error(err):
        """
        Error handler for expired JWT access tokens.

        This function is called when a request is made
        with an expired JWT access token.

        Args:
            err (Exception): The exception object raised by Flask-JWT-Extended.

        Returns:
            JSON response with an error message
            and a 401 Unauthorized status code.
            {
                "error": "Token has expired"
            }
        """
        return jsonify({"error": "Token has expired"}), 401

    @jwt.revoked_token_loader
    def handle_revoked_token_error(err):
        """
        Error handler for revoked JWT access tokens.

        This function is called when a request is
        made with a revoked JWT access token.

        Args:
            err (Exception): The exception object raised by Flask-JWT-Extended.

        Returns:
            JSON response with an error message and
            a 401 Unauthorized status code.
            {
                "error": "Token has been revoked"
            }
        """
        return jsonify({"error": "Token has been revoked"}), 401

    @jwt.needs_fresh_token_loader
    def handle_needs_fresh_token_error(err):
        """
        Error handler for requests that require a fresh JWT access token.

        This function is called when a request requires
        a fresh JWT access token,
        but the provided token is not fresh.

        Args:
            err (Exception): The exception object raised by Flask-JWT-Extended.

        Returns:
            JSON response with an error message
            and a 401 Unauthorized status code.
            {
                "error": "Fresh token required"
            }
        """
        return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
    """
    This is a Python idiom that checks if the script is being run directly (not
    imported as a module). If this condition is true, it starts the Flask
    development server by calling app.run(). The development server will run
    until you stop it manually (e.g., by pressing Ctrl+C in the terminal).
    """
