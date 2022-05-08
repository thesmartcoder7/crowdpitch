from flask import render_template
from . import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('user.html')