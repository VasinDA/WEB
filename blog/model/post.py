class Post:
    def __init__(self, title, date, body):
        self.post = {'title': title, 'date': date, 'body': body} 
        
    def geTitle(self):
        title = self.post['title']
        return title
    
    def getDate(self):
        date = self.post['date']
        return date
    
    def getBody(self):
        body = self.post['body']
        return body