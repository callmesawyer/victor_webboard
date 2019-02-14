from django.test import TestCase
from django.urls import resolve, reverse
from .views import home


class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_homt_url_resolves_home_vies(self):
		view = resolve('/')
		self.assertEquals(view.func, home)
