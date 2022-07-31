import unittest
from post import Post

class TestGetPost(unittest.TestCase):
    def setUp(self):
        # TODO: name should not contain a type. Myabe tst_post?
        self.test_dict = Post('Post 1', '2022-07-27', 'Post test')
        
    def test_get_title(self):
        test_title = 'Post 1'
        self.assertEqual(self.test_dict.geTitle(), test_title)

    def test_get_date(self):
        test_date = '2022-07-27'
        self.assertEqual(self.test_dict.getDate(), test_date)

    def test_get_body(self):
        test_body = 'Post test'
        self.assertEqual(self.test_dict.getBody(), test_body)

unittest.main()