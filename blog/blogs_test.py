import unittest
from blogs import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog_test = Blog(':memory:')
        self.addPostsForTest()
        
    def addPostsForTest(self, count=6):
        for number in range(count):
            # TODO: what if count > 10? if > 31?
            self.blog_test.addPost(f'Post {number}', f'2022-07-1{number}', 'Post test')
            
    def test_add_post(self):
        test_title = 'Post 7'
        test_date = '2022-07-17'
        test_body = 'Post test'
        # TODO: can we call `addPostsForTest(count=1)`
        date = self.blog_test.addPost(test_title, test_date, test_body)
        self.assertEqual(date, test_date)
    
    def test_get_posts_len(self):
        # TODO: expected_len_list
        len_list = 5
        self.assertEqual(len(self.blog_test.getPosts()), len_list)
    
    def test_get_posts_by_date(self):
        test_date = '2022-07-15'
        posts_by_date = self.blog_test.getPostsByDate(test_date)
        for post in posts_by_date:
           self.assertEqual(post['date'], test_date)

    def test_get_post_by_sku(self):
        test_sku = 'post_5'
        test_title = 'Post 5'
        post, = self.blog_test.getPostBySku(test_sku)
        self.assertEqual(post['title'], test_title) 

unittest.main()