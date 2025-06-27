# tests.py
from django.test import TestCase
from .models import Author, Post

class BlogSimpleTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            full_name="Test Author",
            email="author@test.com",
            biography="Simple bio",
            country="Testland"
        )
        self.post = Post.objects.create(
            author=self.author,
            title="Test Post",
            description="Test Description",
            text="Some test text"
        )

    def test_author_str(self):
        self.assertEqual(str(self.author), "author@test.com")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post by Test Author")
