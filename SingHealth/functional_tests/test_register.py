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
        #emulate the phone
        mobile_emulation = { "deviceName": "iPhone X" }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.browser = webdriver.Chrome(executable_path = 'functional_tests/chromedriver',options=chrome_options)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.close()
        super(TestRegisterPage, self).tearDown()

    def test_register_successful(self):
        expected_url = "http://127.0.0.1:8000/login/"
        self.browser.get("http://127.0.0.1:8000/register/")
        
        #dummy testing data
        username = 'Test5'
        email = 'abc@mail.com'
        password = 'testing123!'
        
        #fill in username
        self.browser.find_element_by_id('id_username').send_keys(username)
        time.sleep(1)
        
        #fill in email
        self.browser.find_element_by_id('id_email').send_keys(email)
        time.sleep(1)

        #fill in password
        self.browser.find_element_by_id('id_password1').send_keys(password)
        time.sleep(1)
        
        #confirm password
        self.browser.find_element_by_id('id_password2').send_keys(password)
        time.sleep(1)
        
        #click regsiter button
        self.browser.find_element_by_name('register').click()
        time.sleep(3)

        #check if successfully register
        self.assertEquals(self.browser.current_url, expected_url)

        #go to login page and fill in username
        self.browser.find_element_by_name('username').send_keys(username)
        time.sleep(1)

        #fill in password
        self.browser.find_element_by_name('password').send_keys(password)
        time.sleep(1)
        
        #click login button
        self.browser.find_element_by_name('login').click()
        time.sleep(2)

        #check if successfully login, login with tenant account will direct to this page
        after_login_url = "http://127.0.0.1:8000/tenant_only/"
        self.assertEquals(self.browser.current_url, after_login_url)

    def test_register_unsuccessful(self):
        """ 
            This test register with a registered username
        """
        expected_url = "http://127.0.0.1:8000/login/"
        self.browser.get("http://127.0.0.1:8000/register/")
        
        #dummy testing data
        username = 'Test1'
        email = 'abc@mail.com'
        password = 'testing123!'
        
        #fill in username
        self.browser.find_element_by_id('id_username').send_keys(username)
        time.sleep(1)
        
        #fill in email
        self.browser.find_element_by_id('id_email').send_keys(email)
        time.sleep(1)
        
        #fill in password
        self.browser.find_element_by_id('id_password1').send_keys(password)
        time.sleep(1)
        
        #confirm password
        self.browser.find_element_by_id('id_password2').send_keys(password)
        time.sleep(1)
        
        #click regsiter button
        self.browser.find_element_by_name('register').click()
        time.sleep(1)

        #check the register should be unsuccessful
        if (self.browser.current_url != expected_url):
            unsuccessful = False
        self.assertEquals(unsuccessful, False)

    def test_register_invalid_email(self):
        """ 
            This test register with an invalid email
        """
        expected_url = "http://127.0.0.1:8000/login/"
        self.browser.get("http://127.0.0.1:8000/register/")
        
        #dummy testing data
        username = 'Testing'
        email = 'gadfgsyghd'
        password = 'testing123!'
        
        #fill in username
        self.browser.find_element_by_id('id_username').send_keys(username)
        time.sleep(1)
        
        #fill in email
        self.browser.find_element_by_id('id_email').send_keys(email)
        time.sleep(1)
        
        #fill in password
        self.browser.find_element_by_id('id_password1').send_keys(password)
        time.sleep(1)
        
        #confirm password
        self.browser.find_element_by_id('id_password2').send_keys(password)
        time.sleep(1)
        
        #click regsiter button
        self.browser.find_element_by_name('register').click()
        time.sleep(3)

        #check the register should be unsuccessful
        if (self.browser.current_url != expected_url):
            unsuccessful = False
        self.assertEquals(unsuccessful, False)

    def test_register_simple_password(self):
        """ 
            This test register with a registered username
        """
        expected_url = "http://127.0.0.1:8000/login/"
        self.browser.get("http://127.0.0.1:8000/register/")
        
        #dummy testing data
        username = 'Testing'
        email = 'abc@mail.com'
        password = 'testing123'
        
        #fill in username
        self.browser.find_element_by_id('id_username').send_keys(username)
        time.sleep(1)
        
        #fill in email
        self.browser.find_element_by_id('id_email').send_keys(email)
        time.sleep(1)
        
        #fill in password
        self.browser.find_element_by_id('id_password1').send_keys(password)
        time.sleep(1)
        
        #confirm password
        self.browser.find_element_by_id('id_password2').send_keys(password)
        time.sleep(1)
        
        #click regsiter button
        self.browser.find_element_by_name('register').click()
        time.sleep(3)

        #check the register should be unsuccessful
        if (self.browser.current_url != expected_url):
            unsuccessful = False
        self.assertEquals(unsuccessful, False)