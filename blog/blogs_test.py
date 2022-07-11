import unittest
from blogs import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog = Blog()
        self.title = 'Post 6'
        self.date = '2022-07-18'
        self.data_list = [['Post 1', '2022-07-11', 'Post 1'], ['Post 2', '2022-07-12', 'Post 2'], ['Post 3', '2022-07-14', 'Post 3'], 
        ['Post 4', '2022-07-15', 'Post 4'], ['Post 5',  '2022-07-17', 'Post 5'], ['Post 6',  '2022-07-18', 'Post 6']]
        for title, date, body in self.data_list:
            self.blog.addPost(title, date, body)        
            
    def test_add_post(self):
        test_posts_list =  [{'title': 'Post 1', 'date': '2022-07-11', 'body': 'Post 1'}, {'title': 'Post 2', 'date': '2022-07-12', 'body': 'Post 2'}, 
        {'title': 'Post 3', 'date': '2022-07-14', 'body': 'Post 3'},  {'title': 'Post 4', 'date': '2022-07-15', 'body': 'Post 4'},  
        {'title': 'Post 5', 'date': '2022-07-17', 'body': 'Post 5'}, {'title': 'Post 6', 'date': '2022-07-18', 'body': 'Post 6'}, 
        {'title': 'Post 7', 'date': '2022-07-19', 'body': 'Post 7'}]
        title = 'Post 7'
        date = '2022-07-19'
        body = 'Post 7'
        self.blog.addPost(title, date, body)
        self.assertEqual(self.blog.posts, test_posts_list)
    
    def test_get_posts(self):
        len_list = 5
        self.assertEqual(len(self.blog.getPosts()), len_list)
    
    def test_get_posts_by_date(self):
        posts_by_date = self.blog.getPostsByDate(self.date)
        for post in posts_by_date:
           self.assertEqual(post['date'], self.date)

    def test_get_post_by_sku(self):
        sku = 'post_6'
        post = self.blog.getPostBySku(sku)
        self.assertEqual(post['title'], self.title) 

unittest.main()
