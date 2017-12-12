from django.test import TestCase
from django.test import Client

# Create your tests here.
class PageRiwayatUnitTest(TestCase):
    def test_page_profile_url_is_exist(self):
    	response = Client().get('/page_profile/')
    	self.assertEqual(response.status_code, 200)
