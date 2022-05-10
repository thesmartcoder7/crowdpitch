from . import app
from . import db
import jyserver.Flask as jsf


@jsf.use(app)
class App:
    def __init__(self):
        self.up_count = 0
        self.down_count = 0

    def upvote(self):
        self.up_count = self.up_count + 1
        self.js.document.querySelector('.upvote').innerText = self.up_count

    def downvote(self):
        self.down_count = self.down_count + 1
        self.js.document.querySelector('.downvote').innerText = self.down_count


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String,nullable = False)
    content = db.Column(db.String,nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments  = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    upvotes = db.relationship('UpVote', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relationship('DownVote', backref = 'pitch', lazy = 'dynamic')
    
    def __str__(self) -> str:
        return self.content



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    email = db.Column(db.String)
    image = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def __str__(self) -> str:
        return self.name



class Comment(db.Model):
    __tablename__ = 'comments'
    id  = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(255), nullable = False)



class UpVote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key =True)
    upvote = db.Column(db.Integer,default = 0)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

   

class DownVote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer,default = 0)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
