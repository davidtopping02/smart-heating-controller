from flask import Flask
from .routes import setup_routes  # Import routes from the `routes.py` file


def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Set up routes
    setup_routes(app)

    return app
