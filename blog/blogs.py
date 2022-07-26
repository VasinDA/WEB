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

    # TODO: Should return instance of `Post`
    def addPost(self, title, date, body):
        sku = title.replace(' ', '_').lower()
        date = {'id': None, 'sku': sku, 'title': title, 'date': date, 'body': body}
        sql = 'INSERT INTO posts VALUES(:id, :sku, :title, :date, :body);'
        self.cursor.execute(sql, date)
        self.connect.commit()
        sql = "SELECT date FROM posts WHERE id=?;"
        # TODO: id = self.cursor.lastrowid
        id = [self.cursor.lastrowid]
        self.cursor.execute(sql, id)
        # TODO: Please try `fetchone`
        for date in self.cursor:
            date, = date
        return date
       
    # TODO: should return list of Posts
    def getPosts(self, count = 5):
        sql = 'SELECT title, date, body FROM posts ORDER BY date LIMIT ?;'
        posts = self.getDateFromDataBase(sql, count)
        return posts

    # TODO: should return list of Posts
    def getPostsByDate(self, date):
        sql = 'SELECT title, date, body FROM posts WHERE date=?;'
        posts = self.getDateFromDataBase(sql, date)
        return posts

    # TODO: should return instance of Posts
    def getPostBySku(self, sku):
        sql = 'SELECT title, date, body FROM posts WHERE sku=? LIMIT 1;'
        post = self.getDateFromDataBase(sql, sku)
        return post

    # TODO: name?
    def getDateFromDataBase(self, sql, data):
        data = [data]
        # TODO: self.cursor.execute(sql, [data])
        self.cursor.execute(sql, data)
        posts = [{'title': title, 'date': date, 'body': body} for title, date, body in self.cursor]
        return posts
    
    #def deleteRowsFromTable(self):
        #sql = 'DROP TABLE posts;'
        #self.cursor.execute(sql)
        #self.connect.commit