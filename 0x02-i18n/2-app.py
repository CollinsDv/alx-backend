#!/usr/bin/env python3
"""module: 2-app
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """selects language of choice"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """main landing page"""
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)
