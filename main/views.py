from flask import render_template, url_for, redirect, session
from .models import App
from . import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user')
def user():
    if 'user' in session:
        username = session["user"]
        print(username)
        return App.render(render_template('user.html', user = username))
    elif 'email' in session:
        username = session["email"]
        print(username)
        return App.render(render_template('user.html', user = username))
    else:
        return redirect(url_for('home'))


@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('notfound.html'),404



