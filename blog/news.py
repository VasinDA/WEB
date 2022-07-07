class News:
    def __init__(self):
        self.news = []
    
    def getList(self, date = None):
        news = self.news.copy()
        if date:
            news = list(filter(lambda news_item: news_item['date'] == date, news))
        return news

    def addNews(self, title, date, body):
        self.news.append({'title': title, 'date': date, 'body': body})
