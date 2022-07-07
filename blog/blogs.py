class Blog:
    def __init__(self):
        self.posts = []

    def getPosts(self, count = 5):
        if len(self.posts) < 5:
            posts = self.posts.copy()
            return posts
        if len(self.posts) >= 5:
            posts = self.posts[0:count]
            return posts

    def getPostsByDate(self, date):
        pass

    def getPostBySku(self, sku):
        pass

    def addPost(self, title, date, body):
       self.posts.append({'title': title, 'date': date, 'body': body})