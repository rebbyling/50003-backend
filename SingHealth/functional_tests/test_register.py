from selenium import webdriver
from accounts.models import Staff
from django.contrib.staticfiles.testing import LiveServerTestCase, StaticLiveServerTestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
import time
from random import choice

class TestRegisterPage(LiveServerTestCase):

    def setUp(self):
        super(TestRegisterPage, self).setUp()
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

    def tearDown(self):
        self.browser.close()
        super(TestRegisterPage, self).tearDown()

    #It can only be ran once! change it
    def test_register(self):

        #can only run once
        expected_url = "http://127.0.0.1:8000/login/"
        self.browser.get("http://127.0.0.1:8000/register/")
        
        #dummy testing data
        username = 'def4'
        email = 'abc@mail.com'
        password = 'testing123!'
        
        #fill in username
        self.browser.find_element_by_id('id_username').send_keys(username)
        #fill in email
        self.browser.find_element_by_id('id_email').send_keys(email)
        #fill in password
        self.browser.find_element_by_id('id_password1').send_keys(password)
        #confirm password
        self.browser.find_element_by_id('id_password2').send_keys(password)
        #click regsiter button
        self.browser.find_element_by_name('register').click()
        time.sleep(2)

        #check if successfully register
        self.assertEquals(self.browser.current_url, expected_url)

        #go to login page and fill in username
        self.browser.find_element_by_name('username').send_keys(username)
        #fill in password
        self.browser.find_element_by_name('password').send_keys(password)
        #click login button
        self.browser.find_element_by_name('login').click()
        time.sleep(2)

        #check if successfully login, login with tenant account will direct to this page
        after_login_url = "http://127.0.0.1:8000/tenant_only/"
        self.assertEquals(self.browser.current_url, after_login_url)

