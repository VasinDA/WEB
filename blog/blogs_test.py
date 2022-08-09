import unittest
from blogs import Blog

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.blog_test = Blog(':memory:')
        self.addPostsForTest()
        self.expected_date = '2022-07-01'
        
    def addPostsForTest(self, count=6):
        count = count if count < 32 else 31
        for number in range(1, count+1):
            post = self.blog_test.addPost(f'Post {number}', f'2022-07-{number:02d}', 'Post test')
        return post
            
    def test_add_post(self):
        post = self.addPostsForTest(count=1)
        self.assertEqual(post.getDate(), self.expected_date)
    
    def test_test_len_list(self):
        expected_len_list = 5
        self.assertEqual(len(self.blog_test.getPosts()), expected_len_list)
    
    def test_get_posts_by_date(self):
        posts_by_date = self.blog_test.getPostsByDate(self.expected_date)
        for post in posts_by_date:
           self.assertEqual(post.getDate(), self.expected_date)

    def test_get_post_by_sku(self):
        test_sku = 'post_5'
        expected_title = 'Post 5'
        post = self.blog_test.getPostBySku(test_sku)
        self.assertEqual(post.getTitle(), expected_title) 

unittest.main()git st