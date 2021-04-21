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
        #emulate the phone
        mobile_emulation = { "deviceName": "iPhone X" }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.browser = webdriver.Chrome(executable_path = 'functional_tests/chromedriver',options=chrome_options)
        self.browser.maximize_window()

        self.client = Client()

        #create staff user
        self.staff = User.objects.create_user(username = 'sky', is_active = True, password = 'testing12#')
        self.browser.get("http://127.0.0.1:8000/login")

        #self.browser.find_element_by_name('username').send_keys('sky')
        
        self.browser.find_element_by_name('username').send_keys('tenant3')
        time.sleep(1)
        #self.browser.find_element_by_name('password').send_keys('testing12#')
        self.browser.find_element_by_name('password').send_keys('cohort4meixuan')
        time.sleep(1)
        self.browser.find_element_by_name('login').click()
        time.sleep(1)

    # this is gonna be run after every test functions
    def tearDown(self):
        self.browser.close()
        super(TestTenantPage, self).tearDown()

    """ def test_search(self):
        self.browser.get('http://127.0.0.1:8000/search/')
        time.sleep(1)

        #select filter search
        select = Select(self.browser.find_element_by_id('id_tenant'))
        select.select_by_visible_text('Gom Gom')
        time.sleep(1)
        
        #click search button
        self.browser.find_element_by_xpath('//button[@class="searchButton"]').click()
        time.sleep(1) """
    
    def test_chart(self):
        """ 
            this test is to check whether if tenant can 
            view the chart and download the excel 
        """
        #view chart
        expected_url = 'http://127.0.0.1:8000/chart/'
        self.browser.get('http://127.0.0.1:8000/chart/')
        self.assertEquals(self.browser.current_url,expected_url)

        #download excel
        export_excel = self.browser.find_element_by_xpath('//a[@href="/export_excel/ "]')
        self.browser.execute_script("arguments[0].click();", export_excel)
        time.sleep(1)

    def test_updates(self):
        self.browser.get('http://127.0.0.1:8000/tenant_only/')
        time.sleep(1)

        #click the update button
        updateButton = self.browser.find_element_by_xpath('//a[@class="updateButton"]')
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", updateButton)
        time.sleep(2)

        expected_url = 'http://127.0.0.1:8000/upload_image/'
        self.assertEquals(self.browser.current_url,expected_url)
    
    def test_upload_image(self):
        expected_url = 'http://127.0.0.1:8000/upload_image/'
        self.browser.get('http://127.0.0.1:8000/upload_image/')
        time.sleep(1)

        #check if successfully login
        self.assertEquals(self.browser.current_url,expected_url)
        
        #select tenant
        select = Select(self.browser.find_element_by_xpath('//select[@id="id_tenant"]'))
        select.select_by_visible_text('Gom Gom')
        time.sleep(1)

        self.browser.find_element_by_xpath('//input[@id="id_actual_img"]').send_keys(os.getcwd()+ "/image/images/spongebob.png")
        self.browser.find_element_by_xpath('//button[@class="uploadSubmit"]').click()
        time.sleep(1)
    
    def test_logout(self):
        expected_url = 'http://127.0.0.1:8000/login/'
        self.browser.get('http://127.0.0.1:8000/tenant_only/')
        time.sleep(1)
        
        #click logout button
        self.browser.find_element_by_xpath('//a[@class="logout"]').click()
        time.sleep(1)

        self.assertEquals(self.browser.current_url,expected_url)


    