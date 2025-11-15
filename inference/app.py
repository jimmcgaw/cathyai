from flask import Flask
from transformers import pipeline


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, Gunicorn from factory!"
    
    return app


app = create_app()