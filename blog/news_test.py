import unittest
from news import News

class TestNews(unittest.TestCase):
    def setUp(self):
        self.news_test = News(':memory:')
        self.addNewsForTest()
                
    def addNewsForTest(self, count=6):
        count = count if count < 32 else 31
        for number in range(1, count+1):
            self.news_test.addNews(f'News {number}', f'2022-07-{number:02d}', 'News test')
        return
            
    def test_add_news(self):
        test_date = '2022-07-06'
        sql = "SELECT date FROM news WHERE id=?;"
        id = self.news_test.cursor.lastrowid
        self.news_test.cursor.execute(sql, [id])
        last_date, = self.news_test.cursor.fetchone()
        self.assertEqual(last_date, test_date)
    
    def test_expected_len_list(self):
        len_list = 5
        self.assertEqual(len(self.news_test.getNews()), len_list)

unittest.main()