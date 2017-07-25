from django.test import TestCase, Client
from django.test import TestCase
from models import *
import datetime

#NOTE: all test functions must begin with test or it will e ignored

class UserAccountTest(TestCase):
    def setUp(self):
        Username.objects.create(username="RAQ")

    def test_username_exist(self):
        user = Username.objects.get(id=1)
        self.assertEquals(user.username, 'RAQ')

class LaptopNameTest(TestCase):
    def setUp(self):
        Laptop.objects.create(laptopname="Laptop1")

    def test_laptop_exist(self):
        laptop = Laptop.objects.get(laptopname="Laptop1")
        self.assertEqual(laptop.laptopname, "Laptop1")

class DateOutButtonTest(TestCase):
    def setUp(self):
        dateoutoutbutton = Dateout.objects.create(dateoutbutton ="y")

    def test_dateoutbutton_exists(self):
        dateoutbutton = Dateout.objects.get(id=1)
        self.assertEqual(dateoutbutton.dateoutbutton, "y")    

class DateOut_autoCreation_Test(TestCase):
    def setUp(self):
        dateoutbutton = Dateout.objects.create(dateoutbutton= "y")
    
    def test_dateout_exists(self):
        dateoutbutton = Dateout.objects.get(id=1)
        self.assertEqual(dateoutbutton.dateout, datetime.date.today())

class DateIn_Button_Test(TestCase):
    def setUp(self):
        dateinbutton = Datein.objects.create(dateinbutton = "y")
     
    def test_dateinbutton_exists(self):
        dateinbutton = Datein.objects.get(id=1)
        self.assertEqual(dateinbutton.dateinbutton, "y")

class Datein_autoCreation_test(TestCase):
    def setUp(self):
        dateinbutton=Datein.objects.create(dateinbutton = "y")

    def test_datein_exists(self):
        dateinbutton = Datein.objects.get(id=1)
        self.assertEqual(dateinbutton.datein, datetime.date.today())

class Url_get_test(TestCase):
    def test_index_url_exists(self):
        client=Client()
        index_url=client.get("/index")
        self.assertTemplateUsed(index_url, 'ams/index.html')
    
    def test_index_page_status_code(self):
        client = Client()
        index_url=client.get('/index')
        self.assertEqual(index_url.status_code, 200)

    def test_index_page_availble(self):
        client=Client()
        index_url=client.get('/index')
        self.assertNotEqual(index_url.status_code, 404)

class Laptopform_view(TestCase):
    def test_laptopsearch_exists(self):
        client=Client()
        laptopsearch_url=client.get('/laptopsearch')
        self.assertTemplateUsed(laptopsearch_url, 'ams/laptopsearch.html')

    def test_laptopsearch_page_status_code(self):
        client=Client()
        laptopsearch_url=client.get('/laptopsearch')
        self.assertEqual(laptopsearch_url.status_code,200)

    def test_laptopsearch_page_available(self):
        client=Client()
        laptopsearch_url=client.get('/laptopsearch')
        self.assertNotEqual(laptopsearch_url.status_code,404)

    def test_laptopsearch_laptopname_redirect(self):
        client=Client()
        laptopsearch_post=client.post('/laptopsearch')
        self.assertEqual(laptopsearch_post.status_code, 200)
