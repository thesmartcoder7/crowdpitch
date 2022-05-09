from flask import render_template, url_for, redirect, request, session
from .models import App
from . import app
from config import Config

app.secret_key = Config.SECRET_KEY


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        session["user"] = request.form["s-name"]
        session["email"] = request.form["s-email"]
        session["password"] = request.form["s-password"]
        # if request.form["l-email"] and request.form["l-password"]:
        #     session["email"] = request.form["l-email"]
        #     session["password"] = request.form["l-password"]
         
        return redirect(url_for('user', username = session["user"]))
    else:
        return render_template('index.html')


@app.route('/user')
def user():
    if 'user' in session:
        username = session["user"]
        print(username)
        return App.render(render_template('user.html', user = username))
    else:
        return redirect(url_for('home'))


@app.route('/logout')
def sign_out():
    session.clear()
    return redirect(url_for('home'))