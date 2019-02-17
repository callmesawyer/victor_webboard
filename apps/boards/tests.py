from django.test import TestCase
from django.urls import resolve, reverse
from .views import home


class HomeTests(TestCase):
	def setUp(self):
		self.board = Board.objects.create(name='Django', description='Django Board.')
		url = reverse('home')
		self.response = self.client.get(url)

	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_homt_url_resolves_home_vies(self):
		view = resolve('/')
		self.assertEquals(view.func, home)

	def test_home_view_contains_link_to_topics_page(self):
		board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
		self.assertContains(self.response, 'href="{0}'.format(board_topics_url))

	def test_board_topics_view_contains_link_back_to_homepage(self):
		board_topics_url = reverse('board_topics', kwargs={'pk': 1})
		response = self.client.get(board_topics_url)
		homepage_url = reverse('home')
		self.assertContains(response, 'href="{0}"'.format(homepage_url))


class BoardTopicsTests(TestCase):

	def setUp(self):
		Board.objects.create(name='Django', description='Django board.')

	def test_board_topics_view_success_status_code(self): # is testing if Django is returning a status code 200 (success) for an existing Board.
		url = reverse('board_topics', kwargs={'pk':1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_board_topics_view_not_found_status_code(): # is testing if Django is returning a status code 404 (page not found) for a Board that doesn’t exist in the database.
		url = reverse('board_topics', kwargs={'pk':99})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)

	def test_board_topics_url_resolves_board_topics_view(self): # is testing if Django is using the correct view function to render the topics.
		view = resolve('/boards/1/')
		self.assertEquals(view.func, board_topics)
