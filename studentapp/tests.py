from django.test import TestCase, Client
from django.urls import reverse
from studentapp.models import Student

class TestStudent(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get(self):
        Student.objects.create(name='Student-1', qualification='B.Tech', photo="/home/itrois054/Pictures/forest-wallpaper-hd-12.jpg")
        res = self.c.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')
        self.assertContains(res, 'Student-1')
        self.assertContains(res, 'B.Tech')
        
    def test_post_success(self):
        data = {"name": "Jayasri", "qualification": "B.Tech", "photo": "/home/itrois054/Pictures/forest-wallpaper-hd-12.jpg"}
        res = self.c.post(reverse('home'), data)
        self.assertEqual(res.status_code, 200)

