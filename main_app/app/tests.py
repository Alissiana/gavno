from django.urls import reverse
from rest_framework.test import APITestCase


class OdderTests(APITestCase):
    def test_odd_correct1(self):
        url = reverse('odder', args=[1, 2])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first": 1,
            "second": 2,
            "result": [1]
        })

    def test_odd_correct2(self):
        url = reverse('odder', args=[2, 4])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first": 2,
            "second": 4,
            "result": []
        })

    def test_odd_correct3(self):
        url = reverse('odder', args=[3, 3])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first": 3,
            "second": 3,
            "result": [3, 3]
        })

    def test_odd_correct4(self):
        url = reverse('odder', args=[44, 11])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first": 44,
            "second": 11,
            "result": [11]
        })

    def test_odd_correct5(self):
        url = reverse('odder', args=[53, 5])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first": 53,
            "second": 5,
            "result": [53, 5]
        })