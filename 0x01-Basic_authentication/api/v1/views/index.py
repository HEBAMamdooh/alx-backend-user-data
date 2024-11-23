#!/usr/bin/env python3
"""
Index module for the API views.
"""
from flask import Blueprint, jsonify, abort

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Return the status of the API."""
    return jsonify({"status": "OK"})


@app_views.route("/unauthorized", methods=["GET"], strict_slashes=False)
def unauthorized():
    """Raise a 401 Unauthorized error."""
    abort(401)


@app_views.route("/forbidden", methods=["GET"], strict_slashes=False)
def forbidden():
    """Raise a 403 Forbidden error."""
    abort(403)
