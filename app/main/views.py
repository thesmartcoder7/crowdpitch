from flask import render_template, url_for, redirect, request, session
from ..models import App
from ..models import User, Pitch
from .. import app, db


@app.route('/pitch', methods=['POST','GET'])
def pitch():
    if request.method == "POST":
        present_user = User.query.filter_by(name=session.get('user')).first()
        print(session.get('user'))
        new_pitch = Pitch(category=request.form['category'], content=request.form['pitch-form'], user_id=present_user.id)       
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('user', username = session['user']), code=307)
    else:
        return redirect(url_for('user', username = session['user']), code=307)


@app.route('/')
def home():
    # all_pitches = Pitch.query.limit(5).all()
    # return render_template('index.html', pitches = all_pitches)
     # all_pitches = Pitch.query.limit(5).all()
    return render_template('index.html')


@app.route('/user/<username>',  methods=["POST", "GET"])
def user(username):
    present_user = User.query.filter_by(name=session.get('user')).first()
    all_pitches = Pitch.query.all()
    user_pitches = Pitch.query.filter_by(user_id=present_user.id).all()
    investors = Pitch.query.filter_by(category = 'investors').all()
    customers = Pitch.query.filter_by(category = 'customers').all()
    sales = Pitch.query.filter_by(category = 'sales').all()
    employees = Pitch.query.filter_by(category = 'employees').all()
    if request.method == 'POST':
        user = User.query.filter_by(name=username).first()
        return App.render(render_template(
            'user.html', 
            user = user, 
            all_pitches = all_pitches,
            user_pitches = user_pitches,
            investors = investors,
            customers = customers,
            sales = sales,
            employees = employees
            ))
    else:
        return redirect(url_for('home'))
     

@app.errorhandler(404)
def four_Ow_four(error):
    return render_template('notfound.html'),404



