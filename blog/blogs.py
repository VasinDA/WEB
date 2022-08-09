import sqlite3
from model.post import Post

class Blog:
    def __init__(self, name_db):
        self.connect = sqlite3.connect(name_db, check_same_thread=False)
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
        post = Post(title, date, body)
        data = (None, post.getSku(), post.getTitle(), post.getDate(), post.getBody())
        sql = 'INSERT INTO posts VALUES(?, ?, ?, ?, ?);'
        self.cursor.execute(sql, data)
        self.connect.commit()
        id = self.cursor.lastrowid
        post = self.getPostById(id)
        return post
       
    def getPosts(self, count = 5):
        sql = 'SELECT title, date, body FROM posts ORDER BY date LIMIT ?;'
        posts = self.getDataFromBase(sql, count)
        return posts

    def getPostById(self, id):
        sql = "SELECT title, date, body FROM posts WHERE id=?;"
        post, = self.getDataFromBase(sql, id)
        return post

    def getPostsByDate(self, date):
        sql = 'SELECT title, date, body FROM posts WHERE date=?;'
        posts = self.getDataFromBase(sql, date)
        return posts

    def getPostBySku(self, sku):
        sql = 'SELECT title, date, body FROM posts WHERE sku=? LIMIT 1;'
        post, = self.getDataFromBase(sql, sku)
        return post

    def getDataFromBase(self, sql, data):
        self.cursor.execute(sql, [data])
        posts = [Post(title, date, body) for title, date, body in self.cursor]
        return posts
   