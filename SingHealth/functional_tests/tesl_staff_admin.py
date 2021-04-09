from selenium import webdriver
from accounts.models import Staff
from django.contrib.staticfiles.testing import LiveServerTestCase, StaticLiveServerTestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
import time
from random import choice
from selenium.webdriver.support.ui import Select
import os


class TestStaffPage(LiveServerTestCase):

    # a superuser is created
    # username = pip
    # password = testing123!

    # this is gonna be run before every test functions
    def setUp(self):
        super(TestStaffPage, self).setUp()
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.browser.get("http://127.0.0.1:8000/admin")

        #pre-login
        self.browser.find_element_by_id('id_username').send_keys('sky_test')
        self.browser.find_element_by_id('id_password').send_keys('testing12#')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        
        #create staff user
        self.staff = User.objects.create_user(username = 'sky', is_active = True, password = 'testing12#')

    # this is gonna be run after every test functions
    def tearDown(self):
        self.browser.close()
        super(TestStaffPage, self).tearDown()

    def test_logout(self):
        #click logout button
        self.browser.find_element_by_xpath('//a[@href="/admin/logout/"]').click()
        expected_url = 'http://127.0.0.1:8000/admin/logout/'
        self.assertEqual(self.browser.current_url, expected_url)
        self.browser.find_element_by_xpath('//a[@href="/admin/"]').click()
        self.browser.find_element_by_id('id_username').send_keys('sky_test')
        time.sleep(0.5)
        self.browser.find_element_by_id('id_password').send_keys('testing12#')
        time.sleep(0.5)
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/admin/')


    def test_add_audit(self):
        print(self.browser.current_url)
        self.browser.find_element_by_xpath('//a[@href="/admin/accounts/audit/add/"]').click()
        #select from dropdown menu
        #status
        select = Select(self.browser.find_element_by_id('id_status'))
        # select by visible text
        select.select_by_visible_text('Pending')
        #Tenants
        select = Select(self.browser.find_element_by_id('id_tenant'))
        select.select_by_visible_text('Japanese Food')
        #Staff
        select = Select(self.browser.find_element_by_id('id_staff'))
        select.select_by_visible_text('LI MEIXUAN')
        #Upload Image - seems removed by me
        #self.browser.find_element_by_id('id_actual_img').send_keys(os.getcwd()+ "/image/dummy.jpg")
        self.browser.find_element_by_name('_save').click()

        self.browser.get("http://127.0.0.1:8000/admin")
        self.browser.find_element_by_xpath('//a[@href="/admin/accounts/audit/"]').click()
        #Action
        select = Select(self.browser.find_element_by_xpath('//select[@name="action"]'))
        select.select_by_visible_text('Delete selected audits')
        
        #select audit to be deleted

        #remember to change this
        
        self.browser.find_element_by_xpath('//input[@value="11"]').click()
        #click the Go button
        self.browser.find_element_by_xpath('//button[@value="0"]').click()
        #oh im so sure i wanna delete u, bye friend
        self.browser.find_element_by_xpath('//input[@value="Yes, I’m sure"]').click()

    def test_add_staff(self):
        #click the cutie add button
        self.browser.find_element_by_xpath('//a[@href="/admin/accounts/staff/add/"]').click()
        #fill in the name and email
        self.browser.find_element_by_id('id_name').send_keys('Sky')
        self.browser.find_element_by_id('id_email').send_keys('dummy@mail.com')
        #click save button
        self.browser.find_element_by_xpath('//input[@value="Save"]').click()
        #Select Action
        select = Select(self.browser.find_element_by_xpath('//select[@name="action"]'))
        select.select_by_visible_text('Delete selected staffs')
        #select staff to be deleted
        self.browser.find_element_by_xpath('//input[@value="12"]').click()
        #click the Go button
        self.browser.find_element_by_xpath('//button[@value="0"]').click()
        #confirm delete
        self.browser.find_element_by_xpath('//input[@value="Yes, I’m sure"]').click()

    def test_tenants_scores(self):
        #click the cutie add button
        self.browser.find_element_by_xpath('//a[@href="/admin/accounts/tenant_score/add/"]').click()
        #fill in the name and score
        self.browser.find_element_by_id('id_name').send_keys('Chicken Rice')
        self.browser.find_element_by_id('id_score').send_keys('100')
        #click save button
        self.browser.find_element_by_xpath('//input[@value="Save"]').click()
        #Select Action
        select = Select(self.browser.find_element_by_xpath('//select[@name="action"]'))
        select.select_by_visible_text('Delete selected tenant_scores')
        #select entry to be deleted
        self.browser.find_element_by_xpath('//input[@value="8"]').click()
        #click the Go button
        self.browser.find_element_by_xpath('//button[@value="0"]').click()
        #confirm delete
        self.browser.find_element_by_xpath('//input[@value="Yes, I’m sure"]').click()

    def test_add_tenant(self):
        #click the cutie add button
        self.browser.find_element_by_xpath('//a[@href="/admin/accounts/tenant/add/"]').click()
        #fill in the name
        self.browser.find_element_by_id('id_name').send_keys('Sky')
        #Select Status
        select = Select(self.browser.find_element_by_id('id_status'))
        select.select_by_visible_text('Pass')
        #Fill in Category and Description
        description = "This is for testing purpose!"
        self.browser.find_element_by_id('id_category').send_keys('Food')
        self.browser.find_element_by_id('id_description').send_keys(description)
        #upload image
        self.browser.find_element_by_id('id_actual_img').send_keys(os.getcwd()+ "/image/dummy.jpg")
        #click save button
        self.browser.find_element_by_xpath('//input[@value="Save"]').click()
        time.sleep(5)
        #select = Select(self.browser.find_element_by_xpath('//select[@name="action"]'))
        #Select Action
        select = Select(self.browser.find_element_by_xpath('//select[@name="action"]'))
        select.select_by_visible_text('Delete selected tenants')
        #select tenant to be deleted
        self.browser.find_element_by_xpath('//input[@value="8"]').click()
        #click the Go button
        self.browser.find_element_by_xpath('//button[@value="0"]').click()
        #confirm delete
        self.browser.find_element_by_xpath('//input[@value="Yes, I’m sure"]').click()


    #this test is to test if the button work, but there are certain button that will end up keep looping, therefore i commented them
    #or maybe i should remove them... 
    """ def test_button(self):
        self.browser.get("http://127.0.0.1:8000/admin")

        self.browser.find_element_by_id('id_username').send_keys('sky_test')
        time.sleep(0.5)
        self.browser.find_element_by_id('id_password').send_keys('testing12#')
        time.sleep(0.5)
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        links = self.browser.find_elements_by_xpath("//a[@href]")
        while (links):
            random_link = choice(links)
            print(random_link.get_attribute("href"))
            
            error_url = "http://127.0.0.1:8000/#"
            if (self.browser.current_url == error_url):
                self.tearDown()

            self.browser.get(random_link.get_attribute("href"))
            links = self.browser.find_elements_by_xpath("//a[@href]")
        self.browser.close() """

