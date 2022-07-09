class Blog:
    def __init__(self):
        self.posts = []

    def getPosts(self, count = 5):
        if len(self.posts) < 5:
            return self.posts
        if len(self.posts) >= 5:
            posts = self.posts[0:count]
            return posts

    def getPostsByDate(self, date):
        posts = self.posts.copy()
        if date:
            posts = list(filter(lambda posts_item: posts_item['date'] == date, posts))
        return posts

    def getPostBySku(self, sku):
        posts = self.posts.copy()
        if sku:
            posts = list(filter(lambda posts_item: posts_item['sku'] == sku, posts))
        return posts

    def addPost(self, title, date, body):
       self.posts.append({'title': title, 'date': date, 'body': body})