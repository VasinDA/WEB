import sqlite3
from model.news import GetNews

class News:
    def __init__(self, name_db):
        self.news = []
        self.connect = sqlite3.connect(name_db, check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT,
            title TEXT,
            date TEXT,
            body TEXT
            );
        """
        self.cursor.executescript(sql)

    def __del__(self):
        self.connect.close() 

    def addNews(self, title, date, body):
        sku = title.replace(' ', '_').lower()
        date = {'id': None, 'sku': sku, 'title': title, 'date': date, 'body': body}
        sql = 'INSERT INTO news VALUES(:id, :sku, :title, :date, :body);'
        self.cursor.execute(sql, date)
        self.connect.commit()

    def getNews(self, count = 5):
        sql = 'SELECT title, date, body FROM news ORDER BY date LIMIT ?;'
        news = self.getDataFromBase(sql, count)
        return news
    
    def getDataFromBase(self, sql, data):
        self.cursor.execute(sql, [data])
        news = [GetNews(title, date, body) for title, date, body in self.cursor]
        return news