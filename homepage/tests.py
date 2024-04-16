from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomepageView

class HomepageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("homepage")
        self.response = self.client.get(url)

    def test_url_exists(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'homepage/homepage.html')
        self.assertContains(self.response, "<title>Homepage</title>", html=True)

    def test_resolve_homepage_url(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomepageView.as_view().__name__)

