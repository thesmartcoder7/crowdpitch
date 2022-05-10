from flask import render_template, url_for, redirect, request, session
from . import app
from config import Config
from datetime import timedelta


app.secret_key = Config.SECRET_KEY
app.permanent_session_lifetime = timedelta(weeks=1)

@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        session.permanent = True
        session["user"] = request.form["s-name"]
        session["email"] = request.form["s-email"]
        session["password"] = request.form["s-password"]
        
        return redirect(url_for('user', username = session["user"]))
    else:
        return render_template('index.html')



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        session["email"] = request.form["l-email"]
        session["password"] = request.form["l-password"]
        return redirect(url_for('user', username = session["email"]))
    else:
        return render_template('index.html')



@app.route('/logout')
def sign_out():
    session.clear()
    return redirect(url_for('home'))