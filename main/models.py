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
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable = False)
    category = db.relationship('Category', backref = db.backref('pitch'), lazy = True)

    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable = False)
    comment = db.relationship('Comment', backref = db.backref('pitch'), lazy = True)

    vote_id = db.Column(db.Integer, db.ForeignKey('votes.id'), nullable = False)
    vote = db.relationship('Vote', backref = db.backref('pitch'), lazy = True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user = db.relationship('User', backref = db.backref('pitch'), lazy = True)



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


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)


class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key = True)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text)