from django.test import TestCase, Client


class GreetingsViewsTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    
    def test_greetings(self):
        response = self.client.get('/greetings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Hello World!', response.content.decode())

    
    def test_personal_greetings(self):
        name = 'Mateusz'
        response  = self.client.get(f'/greetings/{name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Hello Mateusz', response.content.decode())