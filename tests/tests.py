import unittest
from app.models import Pitch, User, Comment, UpVote, DownVote


# from  import Pitch, User, Comment, UpVote, DownVote


class PitchTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_pitch = Pitch(category='invenstors', content='take it or leave it')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))


class UserTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.sam = User('samuel', 'samuel@martins.com', 'simplepass')

    def test_instance(self):
        self.assertTrue(isinstance(self.sam, User))


class CommentTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_comment = Comment(user_id=10, pitch_id=10, comment="sample comment")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


class UpVoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.up_vote = UpVote(user_id=10, pitch_id=10, upvote=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.up_vote, UpVote))


class DownVoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.down_vote = DownVote(user_id=10, pitch_id=10, downvote=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.down_vote, DownVote))


if __name__ == "__main__":
    unittest.main()
