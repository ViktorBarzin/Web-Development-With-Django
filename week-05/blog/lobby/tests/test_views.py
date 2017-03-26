from django.test import TestCase, Client
from lobby.services import create_blogpost, get_all_blogs, get_all_public_posts


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_only_public_posts(self):
        # Create a private post
        private_post = create_blogpost('private', 'can\'t see me', [], True)
        response = self.client.get('/')
        self.assertNotContains(response, 'private')



