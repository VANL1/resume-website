from django.test import TestCase


class HomePageTests(TestCase):
    def test_home_page_renders_resume(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Junior Python-разработчик')
        self.assertContains(response, 'Что я умею')
        self.assertContains(response, 'https://t.me/Vanli1')

    def test_home_page_has_contacts(self):
        response = self.client.get('/')

        self.assertContains(response, 'kotovvasili1@yandex.ru')
        self.assertContains(response, 'https://github.com/VANL1')
