import unittest
from news import GetNews

class TestGetNews(unittest.TestCase):
    def setUp(self):
        # TODO: the same as for `post_test.py`.
        self.test_news = GetNews('News 1', '2022-07-27', 'News test')
        
    def test_get_title(self):
        expected_title = 'News 1'
        self.assertEqual(self.test_news.getTitle(), expected_title)
    
    def test_get_sku(self):
        expected_sku = 'news_1'
        self.assertEqual(self.test_news.getSku(), expected_sku)

    def test_get_date(self):
        expected_date = '2022-07-27'
        self.assertEqual(self.test_news.getDate(), expected_date)

    def test_get_body(self):
        expected_body = 'News test'
        self.assertEqual(self.test_news.getBody(), expected_body)

unittest.main()