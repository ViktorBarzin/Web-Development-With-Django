from django.test import TestCase
from faker import Factory

from lobby.models import BlogPost
from lobby.services import get_all_public_posts, create_blogpost


faker = Factory.create()

class BlogPostQuerysetTests(TestCase):
    def setUp(self):
        pass

    def test_get_public_posts_gets_public_posts_only(self):
        post = create_blogpost(faker.word(), faker.paragraph(), [], False)
        all_public_posts = get_all_public_posts()
        self.assertEqual(all_public_posts, list(BlogPost.objects.get_public_posts()))


