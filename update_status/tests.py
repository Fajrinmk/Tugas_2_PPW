from django.test import TestCase
from django.test import Client
import environ
from .views import *
from .csui_helper import *
from .custom_auth import *
from .models import *


# Create your tests here.
env = environ.Env(DEBUG=(bool, False),)

class testUpdateStatus(TestCase):
    def test_update_status_session_url_is_exist(self):
        response = Client().get('/update_status/')
        self.assertEqual(response.status_code, 200)

    def test_update_status_session_login_page_is_working(self):
        response = Client().get('/update_status/')
        html_response = response.content.decode('utf8')
        self.assertIn("Gunakan <b> akun SSO </b> untuk login",html_response)

    def test_update_status_custom_auth(self):
        response = self.client.post(reverse('update-status:auth_login'),
                                    data={
                                        'username': 'hehe',
                                        'password': 'hehe'
                                    }, follow=True)
        self.assertIn('salah', response.content.decode('utf-8'))

        response = self.client.get(reverse('update-status:index'))
        self.assertIn('Login', response.content.decode('utf-8'))
        response = self.client.get(reverse('update-status:dashboard'), follow=True)
        self.assertIn('Login', response.content.decode('utf-8'))

        self.client.post(reverse('update-status:auth_login'), data={
            'username': env("SSO_USERNAME"),
            'password': env("SSO_PASSWORD"),
        }, follow=True)

        # response = self.client.get(reverse('update-status:index'), follow=True)
        # self.assertNotIn('Login', response.content.decode('utf8'))
        # reponse = self.client.get(reverse('update-status:auth_logout'), follow=True)

    def test_auth_logout(self):
        response_post = self.client.post('/update_status/custom_auth/logout/')
        response = self.client.get('/update_status/',follow=True)
        html_response = response.content.decode('utf8')
        self.assertIn('Anda berhasil logout. Semua session Anda sudah dihapus',html_response)
        response = self.client.post(reverse('update-status:auth_logout'),follow=True)
        self.assertIn('Anda berhasil logout. Semua session Anda sudah dihapus',html_response)