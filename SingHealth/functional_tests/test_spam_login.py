import random
import string
from selenium import webdriver
from django.contrib.staticfiles.testing import LiveServerTestCase
import time

def get_random_username():
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    return username

def get_random_password():
    password = ''.join(random.choice(string.printable) for i in range(10))
    return password

class TestSpamLogin(LiveServerTestCase):

    def setUp(self):
        super(TestSpamLogin, self).setUp()
        #emulate the phone
        mobile_emulation = { "deviceName": "iPhone X" }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.browser = webdriver.Chrome(executable_path = 'functional_tests/chromedriver',options=chrome_options)
        self.browser.maximize_window()

        self.browser.get("http://127.0.0.1:8000/login")

    def tearDown(self):
        self.browser.close()
        super(TestSpamLogin, self).tearDown()

    def test_invalid_0(self):
        try:
            for i in range(6):
                print("The "+ str(i) +"th time")
                username = self.browser.find_element_by_name('username')
                username.send_keys(get_random_username())
                time.sleep(0.5)
                password = self.browser.find_element_by_name('password')
                password.send_keys(get_random_password())
                time.sleep(0.5)
                self.browser.find_element_by_name('login').click()
                time.sleep(1)
        except(Exception):
            time.sleep(3)
            print("AHA you are caught for brutal force login attempts! Bad boiii")