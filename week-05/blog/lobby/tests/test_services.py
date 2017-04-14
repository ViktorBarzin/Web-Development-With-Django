from django.test import TestCase
from lobby import services

from faker import Factory
faker = Factory.create()


class ServicesTests(TestCase):
    def setUp(self):
        pass

    def test_extract_tags_splits_correctly(self):
        tags_string = ''
        for i in range(3):
            tags_string += faker.word() + ' '
        self.assertEqual(tags_string.split(), [x.name for x in services.extract_tags(tags_string)])



