import unittest
from post import Post

class TestGetPost(unittest.TestCase):
    def setUp(self):
        # TODO: name should not contain a type. Myabe tst_post?
        self.tst_post = Post('Post 1', '2022-07-27', 'Post test')
        
    def test_get_title(self):
        expected_title = 'Post 1'
        self.assertEqual(self.tst_post.getTitle(), expected_title)

    def test_get_sku(self):
        expected_sku = 'post_1'
        self.assertEqual(self.tst_post.getSku(), expected_sku)

    def test_get_date(self):
        expected_date = '2022-07-27'
        self.assertEqual(self.tst_post.getDate(), expected_date)

    def test_get_body(self):
        expected_body = 'Post test'
        self.assertEqual(self.tst_post.getBody(), expected_body)

unittest.main()