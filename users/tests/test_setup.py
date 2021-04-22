from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from faker import Faker
from model_mommy import mommy
from django.conf import settings

User = settings.AUTH_USER_MODEL


class TestSetUp(APITestCase):

    def setUp(self):
        # self.register_url = reverse('register')
        self.client = APIClient()
        self.register_url = 'auth/registration/'
        self.login_url = reverse('login')
        self.fake = Faker()
        self.user_a = mommy.make('users.User')

        # self.user_data = {
        #     'email': self.fake.email().split('@')[0],
        #     'username': self.fake.username(),
        #     'password': self.fake.password(),
        # }
        self.user_data = {
            'email': 'testuseremail@gmail.com',
            'username': 'testuserusername',
            'password1': 'Testpassword123123',
            'password2': 'Testpassword123123'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
