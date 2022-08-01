import sqlite3
from model.news import GetNews

class News:
    def __init__(self, name_db):
        # TODO: do we want to remove it?
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
        news = GetNews(title, date, body)
        data = (None, news.getSku(), news.getTitle(), news.getDate(), news.getBody())
        sql = 'INSERT INTO news VALUES(?, ?, ?, ?, ?);'
        self.cursor.execute(sql, data)
        self.connect.commit()

    def getNews(self, count = 5):
        sql = 'SELECT title, date, body FROM news ORDER BY date LIMIT ?;'
        news = self.getDataFromBase(sql, count)
        return news
    
    def getDataFromBase(self, sql, data):
        self.cursor.execute(sql, [data])
        news = [GetNews(title, date, body) for title, date, body in self.cursor]
        return news