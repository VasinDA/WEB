class GetNews:
    def __init__(self, title, date, body):
        self.news = {'title': title, 'date': date, 'body': body} 
        
    def getSku(self):
        sku = self.getTitle().replace(' ', '_').lower()
        return sku

    def getTitle(self):
        title = self.news['title']
        return title
    
    def getDate(self):
        date = self.news['date']
        return date
    
    def getBody(self):
        body = self.news['body']
        return body