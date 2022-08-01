class Post:
    def __init__(self, title, date, body):
        self.post = {'id': id, 'title': title, 'date': date, 'body': body} 
          
    def getSku(self):
        sku = self.getTitle().replace(' ', '_').lower()
        return sku

    def getTitle(self):
        title = self.post['title']
        return title
    
    def getDate(self):
        date = self.post['date']
        return date
    
    def getBody(self):
        body = self.post['body']
        return body