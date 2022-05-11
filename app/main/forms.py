from flask import url_for, redirect, request, session
from .. import app, db
from ..models import User
from config import Config
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from .greeting import send_email


app.secret_key = Config.SECRET_KEY
app.permanent_session_lifetime = timedelta(weeks=1)

@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        present_user = User.query.filter_by(name=request.form['s-name']).first()
        if present_user:
            print("user exists")
            # add a flash message that a user exists
            return redirect(url_for('home'))
        else:
            user = User(request.form["s-name"], request.form["s-email"], generate_password_hash(request.form["s-password"]))
            db.session.add(user)
            db.session.commit()
            send_email(user.name, user.email)
            return redirect(url_for('user', username = user.name))
    else:
        return redirect(url_for('home'))



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['l-email']).first()
        if user:
            if check_password_hash(user.password, request.form['l-password']) == True:
                session["user"] = user.name
                return redirect(url_for('user', username = user.name), code=307)
            else:
                # add password or username wrong flash message
                return redirect(url_for('home'))
        else:
             # add signup flashmessage
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/logout')
def sign_out():
    session.clear()
    return redirect(url_for('home'))