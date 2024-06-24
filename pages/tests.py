from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there!  I should not be on the page...")
        pass


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "about")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self. assertNotContains(self.response, "Hello, This does not feel like th right txt ...")
