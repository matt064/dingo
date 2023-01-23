from django.test import TestCase
from posts.models import Post, Author


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="kwadrat", content='4 boki')
        Post.objects.create(title="snieg", content='nie ma sniegu')

    def test_post_str(self):
        p1 = Post.objects.get(title="kwadrat")
        p2 = Post.objects.get(title="snieg")

        self.assertEqual(str(p1), "id:1, title:kwadrat")
        self.assertEqual(str(p2), "id:2, title:snieg")


class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick= "wiechu", email="wiechu@example.com")

    def test_author_str(self):
        a1 = Author.objects.get(nick= "wiechu")

        self.assertEqual(str(a1), "wiechu")
