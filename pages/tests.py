from django.test import TestCase
from django.shortcuts import reverse

from .models import CarClass


class PagesTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     cls.data = CarClass.objects.get().all()

    def test_home_by_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)

    def test_home_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_to_find_objects(self):
        data = CarClass.objects.create(title='italia',description='italian')
        response = self.client.get(reverse('home'))
        self.assertContains(response,data.title)


