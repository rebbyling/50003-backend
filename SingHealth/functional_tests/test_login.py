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

        #emulate the phone
        mobile_emulation = { "deviceName": "iPhone X" }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.browser = webdriver.Chrome(executable_path = 'functional_tests/chromedriver',options=chrome_options)
        self.browser.maximize_window()
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

        time.sleep(5)
        self.browser.find_element_by_id('id_username').send_keys('staff2')
        time.sleep(1)
        self.browser.find_element_by_id('id_password').send_keys('cohort4meixuan')
        time.sleep(1)
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        time.sleep(1)
        self.assertEquals(self.browser.current_url, expected_url)
    
    def test_tenant_login(self):
        expected_url = "http://127.0.0.1:8000/tenant_only/"
        self.browser.get("http://127.0.0.1:8000/login")

        self.browser.find_element_by_name('username').send_keys('tenant3')
        time.sleep(1)

        #self.browser.find_element_by_name('password').send_keys('cohort4meixuan')
        self.browser.find_element_by_name('password').send_keys('cohort4meixuan')
        time.sleep(1)

        self.browser.find_element_by_name('login').click()
        time.sleep(1)

        self.assertEquals(self.browser.current_url, expected_url)

        

        