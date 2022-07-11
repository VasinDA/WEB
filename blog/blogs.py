class Blog:
    def __init__(self):
        self.posts = []

    def addPost(self, title, date, body):
        title = str(title).capitalize()
        self.posts.append({'title': title, 'date': date, 'body': body})
        
    def getPosts(self, count = 5):
        if len(self.posts) < 5:
            return self.posts
        if len(self.posts) >= 5:
            posts = self.posts[:count]
            return posts

    def getPostsByDate(self, date):
        posts = self.posts.copy()
        posts = list(filter(lambda posts_item: posts_item['date'] == date, posts))
        return posts

    def getPostBySku(self, sku):
        posts = self.posts.copy()
        title = str(sku).replace('_', ' ')
        title = title.capitalize()
        posts = list(filter(lambda posts_item: posts_item['title'] == title, posts))
        post = posts[0]
        return post
