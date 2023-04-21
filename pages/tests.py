from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.functional import lazy

from .models import CarClass,Car,CarBrand


class PagesTest(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.car_class = CarClass.objects.create(
            title='test',
            description='testing',
            image='media/image/15_2.jpg'
        )

        self.car_brand_name = CarBrand.objects.create(
            car_brand=self.car_class.id,
            title='test',
            description='testing',
            image='media/image/15_2.jpg'
        )

    # def test_home_by_url(self):
    #     response = self.client.get('')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_home_by_name(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_show_by_class_by_url(self):
    #     response = self.client.get(f'/{self.car_class.id}/')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_show_by_class_by_name(self):
    #     pk = self.car_class.id
    #     response = self.client.get(reverse('show_by_class',args={pk}))
    #     self.assertEqual(response.status_code, 200)

    # def test_car_show_by_url(self):
    #     response = self.client.get(f'/{self.car_class.id / self.car_brand_name.id}/')
    #     self.assertEqual(response.status_code, 200)

    def test_car_show_by_name(self):
        response = self.client.get(reverse('car_show', args={self.car_class.id}))
        self.assertEqual(response.status_code, 200)

    # def test_home_to_find_objects(self):
    #     car_class = CarClass.objects.create(title='italia', description='italian')
    #     response = self.client.get(reverse('home'))
    #     self.assertContains(response, car_class.title)

    # def test_comment_show_in_template(self):
