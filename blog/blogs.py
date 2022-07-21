import sqlite3
class Blog:
    def __init__(self):
        self.connect = sqlite3.connect('data.db')
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER AUTOINCREMENT,
            sku TEXT,
            title TEXT,
            date TEXT,
            body TEXT
            CONSTRAINT PK_posts PRIMARY KEY (id,sku)
        );
        """
        self.cursor.executescript(sql)

    def __del__(self):
        self.connect.close() 

    def addPost(self, title, date, body):
        title = str(title).capitalize()
        sku = title.replace(' ', '_')
        date = {'id': None, 'sku': sku, 'title': title, 'date': date, 'body': body}
        sql = 'INSERT INTO posts VALUES(:id, :sku, :title, :date, :body);'
        self.cursor.execute(sql, date)
        self.connect.commit()
        
    def getPosts(self, count = 5):
        sql = 'SELECT title, date, body FROM posts ORDER BY date LIMIT ?;'
        self.cursor.execute(sql, str(count))
        posts = [{'title': title, 'date': date, 'body': body} for title, date, body in self.cursor]
        return posts

    def getPostsByDate(self, date):
        sql = 'SELECT title, date, body FROM posts WHERE date=?;'
        date = [date]
        self.cursor.execute(sql, date)
        posts = [{'title': title, 'date': date, 'body': body} for title, date, body in self.cursor]
        return posts

    def getPostBySku(self, sku):
        sql = 'SELECT title, date, body FROM posts WHERE sku=? LIMIT 1;'
        sku = [sku]
        self.cursor.execute(sql, sku)
        post = [{'title': title, 'date': date, 'body': body} for title, date, body in self.cursor]
        return post


p = Blog()
p.addPost('Post 1', '2020-02-02', 'Post2')
print(p.getPosts())