#!/usr/bin/env python3
"""
Main application module for the API.
"""
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE", "auth")

if auth_type == "basic_auth":
    auth = BasicAuth()
else:
    auth = Auth()


@app.errorhandler(401)
def unauthorized(error):
    """Handler for 401 Unauthorized error."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """Handler for 403 Forbidden error."""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """Handler for filtering requests."""
    if not auth:
        return
    excluded_paths = [
        '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if not auth.authorization_header(request):
        abort(401)
    if not auth.current_user(request):
        abort(403)


if __name__ == "__main__":
    app.run(host=getenv("API_HOST", "0.0.0.0"),
            port=int(getenv("API_PORT", 5000)))
