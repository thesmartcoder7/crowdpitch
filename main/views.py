from flask import render_template, url_for, redirect, request, session
from .models import App
from . import app
from config import Config

app.secret_key = Config.SECRET_KEY


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



@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        session["user"] = request.form["s-name"]
        session["email"] = request.form["s-email"]
        session["password"] = request.form["s-password"]
        return redirect(url_for('user', username = session["user"]))
    else:
        return render_template('index.html')



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session["email"] = request.form["l-email"]
        session["password"] = request.form["l-password"]
        return redirect(url_for('user', username = session["email"]))
    else:
        return render_template('index.html')



@app.route('/logout')
def sign_out():
    session.clear()
    return redirect(url_for('home'))