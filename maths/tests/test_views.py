from django.test import TestCase, Client
from maths.models import Math, Result
from django.urls import reverse



class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        Result.objects.create(value=30)
        self.client = Client()


    def test_add(self):
        response = self.client.get('/maths/add/1/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/operation.html')
        self.assertEqual(response.context['wynik'], 2)


    def test_sub(self):
        response = self.client.get('/maths/sub/5/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/operation.html')
        self.assertEqual(response.context['wynik'], 4)


    def test_mul(self):
        response = self.client.get('/maths/mul/2/2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/operation.html')
        self.assertEqual(response.context['wynik'], 4)


    def test_div(self):
        response = self.client.get('/maths/div/10/2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/operation.html')
        self.assertEqual(response.context['wynik'], 5)


    def test_div_by_zero(self):
        response = self.client.get('/maths/div/10/0')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/operation.html')
        self.assertEqual(response.context['wynik'], 'Error')


    def test_maths_list(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        self.assertIn('<li><a href="/maths/histories/1">id:1, a=20, b=30, op=sub</a></li>', response.content.decode()) 


    def test_maths_details(self):
        m1 = Math.objects.get(operation="sub")
        response = self.client.get(f"/maths/histories/{m1.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/details.html')

    
    def test_results_list_POST(self):
        data = {'value': 30}
        response = self.client.post('/maths/results/', kwargs=data )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/results.html')
        for iteam in response.context['results']:
            self.assertEqual(iteam.value, 30)
            self.assertIsNone(iteam.error)


    def test_results_list_GET(self):
        response = self.client.get('/maths/results/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maths/results.html')        


class MathViewsPaginationTest(TestCase):
    fixtures = ['math', 'result']


    def setUp(self):
        self.client = Client()


    def test_get_first_5(self):
        response = self.client.get('/maths/histories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 5)

    
    def test_get_last_page(self):
        response = self.client.get('/maths/histories/?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['maths']), 1)