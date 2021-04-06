from selenium import webdriver
from accounts.models import Staff
from django.contrib.staticfiles.testing import LiveServerTestCase, StaticLiveServerTestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
import time
from selenium.webdriver.support.ui import Select
import os

class TestStaffNormal(LiveServerTestCase):
    def setUp(self):
        super(TestStaffNormal, self).setUp()
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.browser.get("http://127.0.0.1:8000/login")

        #pre-login
        self.browser.find_element_by_name('username').send_keys('staff2')
        self.browser.find_element_by_name('password').send_keys('cohort4meixuan')
        self.browser.find_element_by_name('login').click()
    
    def tearDown(self):
        self.browser.close()
        super(TestStaffNormal, self).tearDown()

    def test_mail(self):
        dummy_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar odio non varius rhoncus. Praesent vitae efficitur urna. Proin feugiat dui ut scelerisque eleifend. In hac habitasse platea dictumst. Curabitur faucibus diam at elit cursus, non auctor tellus efficitur. Ut ut leo id neque egestas sollicitudin. Cras eu nunc tincidunt, pharetra libero quis, porta neque. Sed eu ultrices magna. Fusce facilisis vel leo a pretium. "

        self.browser.get("http://127.0.0.1:8000/mail")
        #fill in email
        self.browser.find_element_by_xpath('//input[@name="email"]').send_keys('jetxuen@outlook.com')
        #fill in subject
        self.browser.find_element_by_xpath('//input[@name="subject"]').send_keys('Non-compliance Issue')
        #fill in message
        self.browser.find_element_by_xpath('//textarea[@name="message"]').send_keys(dummy_text)
        #upload image
        self.browser.find_element_by_xpath('//input[@name="file"]').send_keys(os.getcwd()+ "/image/dummy.jpg")
        #click send
        upload = self.browser.find_element_by_xpath('//button[@class="uploadSubmit"]')
        self.browser.execute_script("arguments[0].click();", upload)

    def test_view_graph(self):
        #view graph and export are tested here
        self.browser.get('http://127.0.0.1:8000/tenantsD/1/')
        self.browser.find_element_by_xpath('//a[@href="/chart/"]').click()
        export_excel = self.browser.find_element_by_xpath('//a[@href="/export_excel/ "]')
        self.browser.execute_script("arguments[0].click();", export_excel)
        time.sleep(1)
        


