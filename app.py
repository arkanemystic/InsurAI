# This file acts as the entry point for Gunicorn.
# It imports the Flask 'app' object from your existing server logic,
# allowing the production server to run it.

from server.server import app