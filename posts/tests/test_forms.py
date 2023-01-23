from django.test import TestCase
from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


class PostFormTest(TestCase):

    def test_post_save_correct_data(self):
        data = {"title": 'trojkat', 'content': 'test content'}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        p = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.title, 'trojkat')
        self.assertIsNotNone(p.id)
        self.assertEqual(p.content, 'test content')


class AuthorFormTest(TestCase):
    def test_author_save_correct_data(self):
        data = {"nick": 'bigos', 'email': 'bigos@example.com'}
        self.assertEqual(len(Author.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        a = form.save()
        self.assertIsInstance(a, Author)
        self.assertEqual(a.nick, 'bigos')
        self.assertIsNotNone(a.id)
        self.assertEqual(a.email, 'bigos@example.com')        