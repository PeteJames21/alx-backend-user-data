#!/usr/bin/env python3
"""
Module for session authentication views.
"""
from api.v1.views import app_views
from models.user import User
from flask import abort
from flask import jsonify
from flask import make_response
from flask import request
from os import environ


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Log in a user and return the jsonified user instance."""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Retrieve user object based on email
    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session ID for the user
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(environ.get('SESSION_NAME'), session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """Log out the user by destroying the session."""
    from api.v1.app import auth
    success = auth.destroy_session(request)
    if not success:
        abort(404)
    return jsonify({}), 200
