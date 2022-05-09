from . import app
import jyserver.Flask as jsf


@jsf.use(app)
class App:
    def __init__(self):
        self.up_count = 0
        self.down_count = 0

    def upvote(self):
        self.up_count = self.up_count + 1
        self.js.document.querySelector('#upvote').innerHTML = self.up_count

    def downvote(self):
        self.down_count = self.down_count + 1
        print(self.down_count)
        self.js.document.querySelector('#downvote').innerHTML = self.down_count