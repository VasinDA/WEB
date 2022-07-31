import unittest
from news import GetNews

class TestGetNews(unittest.TestCase):
    def setUp(self):
        # TODO: the same as for `post_test.py`.
        
        self.test_dict = GetNews('News 1', '2022-07-27', 'News test')
        
    def test_get_title(self):
        test_title = 'News 1'
        self.assertEqual(self.test_dict.geTitle(), test_title)

    def test_get_date(self):
        test_date = '2022-07-27'
        self.assertEqual(self.test_dict.getDate(), test_date)

    def test_get_body(self):
        test_body = 'News test'
        self.assertEqual(self.test_dict.getBody(), test_body)

unittest.main()