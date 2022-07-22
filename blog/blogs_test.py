import unittest
import sqlite3
from blogs import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog = Blog()
        self.test_title = 'Post 7'
        self.test_date = '2022-07-17'
        self.addPostsForTest()
        # TODO: could we create a funciton for geneting mock data like getPostsForTest(count=N)
        # TODO: please use for-loop and string templates.
        
    def addPostsForTest(count=6):
        for number in range(count):
            print(number)
            self.blog.addPost(f'Post {number}', f'2022-07-1{number}', 'Post test')
            
    def test_add_post(self):
        test_body = 'Post test'
        date = self.blog.addPost(self.test_title, self.test_date, body)
        self.assertEqual(date, self.test_date)
    
    # TODO: rename the test, like test_get_posts_len
    def test_get_posts_len(self):
        len_list = 5
        self.assertEqual(len(self.blog.getPosts()), len_list)
    
    def test_get_posts_by_date(self):
        posts_by_date = self.blog.getPostsByDate(self.test_date)
        for post in posts_by_date:
           self.assertEqual(post['date'], self.test_date)

    def test_get_post_by_sku(self):
        sku = 'post_7'
        post = self.blog.getPostBySku(sku)
        self.assertEqual(post['title'], self.test_date) 

unittest.main()
