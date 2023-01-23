from django.test import TestCase, Client
from posts.models import Post, Author


class PostViewsTest(TestCase):

    def setUp(self):    
        Post.objects.create(title="rok", content="rok 2023")
        Author.objects.create(nick='adam', email='adam@gmail.com')
        self.client = Client()


    def test_posts_list_POST(self):
        data = {'title':'latoooo', 'content':'example'}
        response = self.client.post('/posts/posts_list/', kwargs=data)
        self.assertEqual(response.status_code, 200)


    def test_posts_list_GET(self):
        response = self.client.get('/posts/posts_list/')
        self.assertEqual(response.status_code, 200)


    def test_post_details(self):
        p1 = Post.objects.get(title="rok")
        response = self.client.get(f"/posts/post_list/{p1.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/p_details.html')


    def test_author_details(self):
        a1 = Author.objects.get(nick="adam")
        response = self.client.get(f"/posts/authors/{a1.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/a_details.html')
