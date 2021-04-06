#!/usr/bin/env python3
"""
Handles all routes for the Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Login route"""
    user_email = request.form.get("email")
    if not user_email:
        return jsonify({"error": "email missing"}), 400
    user_pwd = request.form.get("password")
    if not user_pwd:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": user_email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    for i in user:
        if not i.is_valid_password(user_pwd):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            session_id = auth.create_session(i.id)
            json_user = jsonify(i.to_json())
            json_user.set_cookie(getenv("SESSION_NAME"), session_id)
            return json_user


@app_views.route('auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """Logout route"""
    from api.v1.app import auth
    try:
        auth.destroy_session(request)
    except Exception:
        abort(404)
    else:
        return jsonify({}), 200
