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
        self.js.document.querySelector('.upvote').innerHTML = self.up_count

    def downvote(self):
        self.down_count = self.down_count + 1
        self.js.document.querySelector('.downvote').innerHTML = self.down_count


# model class for user
# model class for categories
# model class for pitches
# model class for votes
# model class for comments

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)

    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return self.name