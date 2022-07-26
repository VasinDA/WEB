import sqlite3

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
        sku = title.replace(' ', '_').lower()
        date = {'id': None, 'sku': sku, 'title': title, 'date': date, 'body': body}
        sql = 'INSERT INTO posts VALUES(:id, :sku, :title, :date, :body);'
        self.cursor.execute(sql, date)
        self.connect.commit()
        # TODO: if you want to get last added record - it's better to do it by ID
        # TODO: lwt's try `self.cursor.lastrowid`
        sql = "SELECT date FROM posts WHERE id=?;"
        id = [self.cursor.lastrowid]
        self.cursor.execute(sql, id)
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

    def getDateFromDataBase(self, sql, data):
        data = [data]
        self.cursor.execute(sql, data)
        posts = [{'title': title, 'date': date, 'body': body} for title, date, body in self.cursor]
        return posts
    
    #def deleteRowsFromTable(self):
        #sql = 'DROP TABLE posts;'
        #self.cursor.execute(sql)
        #self.connect.commit