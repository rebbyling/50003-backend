from selenium import webdriver
from random import choice
from django.contrib.staticfiles.testing import LiveServerTestCase
import time

class TestRegisterPage(LiveServerTestCase):

    def setUp(self):
        super(TestRegisterPage, self).setUp()
        #emulate the phone
        mobile_emulation = { "deviceName": "iPhone X" }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.browser = webdriver.Chrome(executable_path = 'functional_tests/chromedriver',options=chrome_options)
        self.browser.maximize_window()

        self.browser.get("http://127.0.0.1:8000/login")

        self.browser.find_element_by_name('username').send_keys('staff1')
        time.sleep(1)

        #self.browser.find_element_by_name('password').send_keys('cohort4meixuan')
        self.browser.find_element_by_name('password').send_keys('238819Lcf')
        time.sleep(1)

        self.browser.find_element_by_name('login').click()
        time.sleep(1)

    def tearDown(self):
        self.browser.close()
        super(TestRegisterPage, self).tearDown()

    def test_monkey(self):
        self.browser.get('http://127.0.0.1:8000/')
        links = self.browser.find_elements_by_xpath("//a[@href]")
        
        while (links):
            random_link = choice(links)
            print(random_link.get_attribute("href"))
            if (random_link.get_attribute("href") == 'http://127.0.0.1:8000/logout/'):
                continue
            else:
                try:
                    self.browser.get(random_link.get_attribute("href"))
                except Exception:
                    print ("Unexpected error:" + Exception)
                time.sleep(0.5)
            links = self.browser.find_elements_by_xpath("//a[@href]")
        driver.close()

        


