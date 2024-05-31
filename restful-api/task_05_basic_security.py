#!/usr/bin/python3
"API Security and Authentication Techniques"

from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
"""
These lines imports the necessary modules from Flask.
This line imports the generate_password_hash and check_password_hash functions
from the werkzeug.security module. These functions are used for password
hashing and verification.
Thess lines imports the necessary functions and
classes from the Flask-JWT-Extended
library for implementing JWT-based authentication:
- JWTManager: A class used to initialize and configure the JWT extension.
- jwt_required: A decorator used to protect routes
and ensure a valid JWT token is provided.
- create_access_token: A function used to generate a new JWT access token.
- get_jwt_identity: A function used to retrieve
the identity (e.g., username) from the JWT token.
"""

# In-memory data store
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

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
"""
This line creates an instance of the Flask application using the Flask class.
The JWT_SECRET_KEY configuration is set to a secret key value, which is used
for signing and verifying JWT tokens.
"""

jwt = JWTManager(app)
"""
This line initializes the JWTManager with the Flask application instance.
"""


# Basic HTTP Authentication
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Missing credentials'}), 401
    """
    This route handles Basic HTTP Authentication for login. It checks if the
    request contains valid authentication credentials (username and password).
    If the credentials are missing, it returns a 401 Unauthorized error with
    a JSON response indicating that the credentials are missing.
    """

    user = next((user for user in users
                if user['username'] == auth.username), None)
    if not user or not check_password_hash(user['password'], auth.password):
        return jsonify({'message': 'Invalid credentials'}), 401
    """
    This block checks if the provided username and password match a user in the
    users list. It uses the check_password_hash function from werkzeug.security
    to verify the password. If the credentials are invalid, it returns a 401
    Unauthorized error with a JSON response indicating that the credentials are
    invalid.
    """

    return jsonify({'message': 'Login successful'})
    """
    If the credentials are valid, it returns a JSON response indicating that
    the login was successful.
    """


# Token-based Authentication with JWT
@app.route('/jwt-login', methods=['POST'])
def jwt_login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Missing credentials'}), 401
    """
    This route handles JWT-based authentication for login. It checks if the
    request contains valid authentication credentials (username and password).
    If the credentials are missing, it returns a 401 Unauthorized error with
    a JSON response indicating that the credentials are missing.
    """

    user = next((user for user in users if
                user['username'] == auth.username), None)
    if not user or not check_password_hash(user['password'], auth.password):
        return jsonify({'message': 'Invalid credentials'}), 401
    """
    This block checks if the provided username and password match a user in the
    users list. It uses the check_password_hash function from werkzeug.security
    to verify the password. If the credentials are invalid, it returns a 401
    Unauthorized error with a JSON response indicating that the credentials are
    invalid.
    """

    access_token = create_access_token(identity=user['username'])
    return jsonify({'access_token': access_token})
    """
    If the credentials are valid, it generates a new JWT access token using the
    create_access_token function from Flask-JWT-Extended, with the user's
    username as the identity. It then returns a JSON response containing the
    access token.
    """


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user}!'})
    """
    This route is protected by the @jwt_required() decorator, which ensures
    that a valid JWT token is provided in the request headers. If a valid token
    is provided, it retrieves the current user's identity (username) from the
    token using the get_jwt_identity function from Flask-JWT-Extended. It then
    returns a JSON response with a greeting message that includes the user's
    identity.
    """


# Role-based Access Control
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only_route():
    current_user = get_jwt_identity()
    user = next((user for user in users
                if user['username'] == current_user), None)
    if not user or user['role'] != 'admin':
        return jsonify({'message': 'Access denied'}), 403
    """
    This route is protected by the @jwt_required() decorator, which ensures
    that a valid JWT token is provided in the request headers. It retrieves the
    current user's identity (username) from the token using the
    get_jwt_identity function from Flask-JWT-Extended. It then checks if the
    user's role is 'admin' by looking up the user in the users list. If the
    user is not an admin or the user is not found, it returns a 403 Forbidden
    error with a JSON response indicating that access is denied.
    """

    return jsonify({'message': 'This route is accessible only to admins'})
    """
    If the user is an admin, it returns a JSON response indicating that the
    route is accessible only to admins.
    """


if __name__ == '__main__':
    app.run()
    """
    This is a Python idiom that checks if the script is being run directly (not
    imported as a module). If this condition is true, it starts the Flask
    development server by calling app.run(). The development server will run
    until you stop it manually (e.g., by pressing Ctrl+C in the terminal).
    """
