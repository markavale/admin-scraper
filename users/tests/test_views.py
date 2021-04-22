from .test_setup import TestSetUp
from django.conf import settings

User = settings.AUTH_USER_MODEL

class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        print(self.user_a.username)
        print(self.user_a.email)
        print(self.user_a.password)
        print(self.user_a)
        print(self.user_data)
        res = self.client.post(
            self.register_url, self.user_data, format="json")
        print("res------------------")        
        print(res)
        self.assertEqual(res.data['username'], self.user_data.useraname)
        self.assertEqual(res.data['email'], self.user_data.email)
        self.assertEqual(res.data['password1'], self.user_data.password1)
        self.assertEqual(res.data['password2'], self.user_data.password2)
        self.assertEqual(res.status_code, 201)

    # def test_user_cannot_login_with_unverified_email(self):
    #     self.client.post(
    #         self.register_url, self.user_data, format="json")
    #     res = self.client.post(self.login_url, self.user_data, format="json")
    #     self.assertEqual(res.status_code, 401)

    # def test_user_can_login_after_verification(self):
    #     response = self.client.post(
    #         self.register_url, self.user_data, format="json")
    #     email = response.data['email']
    #     user = User.objects.get(email=email)
    #     user.is_verified = True
    #     user.save()
    #     res = self.client.post(self.login_url, self.user_data, format="json")
    #     self.assertEqual(res.status_code, 200)
