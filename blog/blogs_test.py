import unittest
from blogs import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog_test = Blog(':memory:')
        self.addPostsForTest()
        self.test_date = '2022-07-01'
        
    def addPostsForTest(self, count=6):
        # TODO: what if count > 10? if > 31?
        count = count if count < 32 else 31
        for number in range(1, count+1):
            post = self.blog_test.addPost(f'Post {number}', f'2022-07-{number:02d}', 'Post test')
        return post
            
    def test_add_post(self):
        # TODO: can we call `addPostsForTest(count=1)`
        post = self.addPostsForTest(count=1)
        self.assertEqual(post.getDate(), self.test_date)
    
    def test_expected_len_list(self):
        # TODO: expected_len_list
        len_list = 5
        self.assertEqual(len(self.blog_test.getPosts()), len_list)
    
    def test_get_posts_by_date(self):
        posts_by_date = self.blog_test.getPostsByDate(self.test_date)
        for post in posts_by_date:
           self.assertEqual(post.getDate(), self.test_date)

    def test_get_post_by_sku(self):
        test_sku = 'post_5'
        test_title = 'Post 5'
        post = self.blog_test.getPostBySku(test_sku)
        self.assertEqual(post.geTitle(), test_title) 

unittest.main()