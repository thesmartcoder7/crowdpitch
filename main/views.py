from flask import render_template, url_for, redirect, request, session
from .models import App
from .models import User
from . import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/<username>',  methods=["POST", "GET"])
def user(username):
    if request.method == 'POST':
        user = User.query.filter_by(name=username).first()
        return App.render(render_template('user.html', user = user))
    else:
        return redirect(url_for('home'))
     

@app.errorhandler(404)
def four_Ow_four(error):
    return render_template('notfound.html'),404



