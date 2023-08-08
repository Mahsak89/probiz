from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class LoginUserViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.login_url = reverse('login')

    def test_login_user_get(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')

    def test_login_user_post_valid(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.login_url, data)

        # Redirects to 'index' page after successful login
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        # Check if the user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)


class LogoutUserViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.logout_url = reverse('logout')

    def test_logout_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)

        # Redirects to 'index' page after successful logout
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        # Check if the user is logged out
        self.assertFalse('_auth_user_id' in self.client.session)
