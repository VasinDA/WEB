import sqlite3
class Blog:
    def __init__(self):
        self.connect = sqlite3.connect('data.db', check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS posts (
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

    def addPost(self, title, date, body):
        sku = title.replace(' ', '_').lower()
        date = {'id': None, 'sku': sku, 'title': title, 'date': date, 'body': body}
        sql = 'INSERT INTO posts VALUES(:id, :sku, :title, :date, :body);'
        self.cursor.execute(sql, date)
        self.connect.commit()
        sql = 'SELECT date FROM posts ORDER BY ID DESC LIMIT 1'
        self.cursor.execute(sql)
        for date in self.cursor:
            date, = date
        return date
       
    def getPosts(self, count = 5):
        sql = 'SELECT title, date, body FROM posts ORDER BY date LIMIT ?;'
        posts = self.getDateFromDataBase(sql, count)
        return posts

    def getPostsByDate(self, date):
        sql = 'SELECT title, date, body FROM posts WHERE date=?;'
        posts = self.getDateFromDataBase(sql, date)
        return posts

    def getPostBySku(self, sku):
        sql = 'SELECT title, date, body FROM posts WHERE sku=? LIMIT 1;'
        post = self.getDateFromDataBase(sql, sku)
        return post

    def getDateFromDataBase(self, sql, date):
        date = [date]
        self.cursor.execute(sql, date)
        posts = [{'title': title, 'date': date, 'body': body} for title, date, body in self.cursor]
        return posts