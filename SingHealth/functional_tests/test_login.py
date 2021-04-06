from selenium import webdriver
from accounts.models import Staff
from django.contrib.staticfiles.testing import LiveServerTestCase, StaticLiveServerTestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
import time
from random import choice

class TestLoginPage(LiveServerTestCase):

    def setUp(self):
        super(TestLoginPage, self).setUp()
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        
        self.client = Client()

        #create staff user
        self.staff = User.objects.create_user(username = 'sky', is_active = True, password = 'testing12#')

    # this is gonna be run after every test functions
    def tearDown(self):
        self.browser.close()
        super(TestLoginPage, self).tearDown()

    def test_admin_login(self):
        """
            Username : sky_test
            email : sky@mail.com
            password : Testing12#
        """
        expected_url = "http://127.0.0.1:8000/admin/"
        self.browser.get("http://127.0.0.1:8000/admin")

        self.browser.find_element_by_id('id_username').send_keys('staff2')
        time.sleep(0.5)
        self.browser.find_element_by_id('id_password').send_keys('cohort4meixuan')
        time.sleep(0.5)
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        time.sleep(1)
        self.assertEquals(self.browser.current_url, expected_url)
    
    def test_tenant_login(self):
        expected_url = "http://127.0.0.1:8000/tenant_only/"
        self.browser.get("http://127.0.0.1:8000/login")
        
        self.user = authenticate(username = 'sky', password = 'testing12#')
        if self.user is not None:
            self.user = User.objects.get(username = 'sky')
            print("test " + self.user.username)  # prints def
            print("test " + self.user.password)  # prints hashed password of testing123!
            self.login = self.client.login(username='sky', password='testing12#')
            self.assertEquals(self.login, True)

            self.browser.get("http://127.0.0.1:8000/login")
        
            self.browser.find_element_by_name('username').send_keys('tenant3')
            self.browser.find_element_by_name('password').send_keys('cohort4meixuan')
            self.browser.find_element_by_name('login').click()
            #self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
            # print(self.browser.page_source)

            self.assertEquals(self.browser.current_url, expected_url)
        else:
            print('fail!!! try harder')

