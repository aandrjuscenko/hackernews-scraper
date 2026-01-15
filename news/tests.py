from django.test import TestCase
from .models import Article
from django.utils import timezone

# Create your tests here.

class ArticleModelTest(TestCase):

    def setUp(self):
        # Create Article object for testing 
        self.article = Article.objects.create(
            title="Test Article",
            link="http://example.com",
            points=10,
            created_at=timezone.now()
        )

    def test_article_creation(self):
        # Check that the Article object was created correctly
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.link, "http://example.com")
        self.assertEqual(self.article.points, 10)
        self.assertIsNotNone(self.article.created_at)

    def test_article_str(self):
        # Check that __str__ returns the article title
        self.assertEqual(str(self.article), "Test Article")
