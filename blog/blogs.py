class Blog:
    def __init__(self):
        self.posts = []

    def addPost(self, title, date, body):
        self.posts.append({'title': title, 'date': date, 'body': body})
        
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
        title = str(sku).replace('_', ' ')
        title = title.capitalize()
        posts = self.posts.copy()
        if title:
            posts = list(filter(lambda posts_item: posts_item['title'] == title, posts))
        return posts[0]