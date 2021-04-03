from selenium import webdriver
from accounts.models import Staff
from django.contrib.staticfiles.testing import LiveServerTestCase, StaticLiveServerTestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
import time, os
from random import choice
from selenium.webdriver.support.ui import Select

class TestTenantPage(LiveServerTestCase):
    def setUp(self):
        super(TestTenantPage, self).setUp()
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        
        self.client = Client()

        #create staff user
        self.staff = User.objects.create_user(username = 'sky', is_active = True, password = 'testing12#')
        self.browser.get("http://127.0.0.1:8000/login")
        #self.browser.find_element_by_name('username').send_keys('sky')
        self.browser.find_element_by_name('username').send_keys('tenant3')
        #self.browser.find_element_by_name('password').send_keys('testing12#')
        self.browser.find_element_by_name('password').send_keys('cohort4meixuan')
        self.browser.find_element_by_name('login').click()

    # this is gonna be run after every test functions
    def tearDown(self):
        self.browser.close()
        super(TestTenantPage, self).tearDown()

    def test_search(self):
        self.browser.get('http://127.0.0.1:8000/search/')
        #select filter search
        select = Select(self.browser.find_element_by_id('id_tenant'))
        select.select_by_visible_text('Japanese Food')
        #click search button
        self.browser.find_element_by_xpath('//button[@class="searchButton"]').click()
    
    def test_chart(self):
        expected_url = 'http://127.0.0.1:8000/chart/'
        self.browser.get('http://127.0.0.1:8000/chart/')
        self.assertEquals(self.browser.current_url,expected_url)
    
    def test_upload_image(self):
        expected_url = 'http://127.0.0.1:8000/upload_image/'
        self.browser.get('http://127.0.0.1:8000/upload_image/')
        #self.assertEquals(self.browser.current_url,expected_url)
        self.browser.find_element_by_xpath('//input[@class="uploadImage"]').send_keys(os.getcwd()+ "/image/dummy.jpg")
        #self.browser.find_element_by_id('id_actual_img').send_keys(os.getcwd()+ "/image/dummy.jpg")
        self.browser.find_element_by_xpath('//button[@class="uploadSubmit"]').click()
    

    # it's commented coz it can only run once!
    def test_register(self):

        #can only run once
        expected_url = "http://127.0.0.1:8000/login/"
        self.browser.get("http://127.0.0.1:8000/register/")
        time.sleep(0.5)
        self.browser.find_element_by_id('id_username').send_keys('def1')
        time.sleep(0.5)
        self.browser.find_element_by_id('id_email').send_keys('abc@mail.com')
        time.sleep(0.5)
        self.browser.find_element_by_id('id_password1').send_keys('testing123!')
        time.sleep(0.5)
        self.browser.find_element_by_id('id_password2').send_keys('testing123!')
        time.sleep(0.5)
        self.browser.find_element_by_name('register').click()
        time.sleep(0.5)
        
        #check if successfully register
        self.assertEquals(self.browser.current_url, expected_url)

        self.browser.find_element_by_name('username').send_keys('def1')
        time.sleep(0.5)
        self.browser.find_element_by_name('password').send_keys('testing123!')
        time.sleep(0.5)
        self.browser.find_element_by_name('login').click()

        after_login_url = "http://127.0.0.1:8000/tenant_only/"
        self.assertEquals(self.browser.current_url, after_login_url)
