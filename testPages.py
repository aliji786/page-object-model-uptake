import unittest
from selenium import webdriver
from pages import *
from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By

# I am using python unittest for asserting cases.
# In this module, there should be test cases.


class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        self.driver.get("http://www.uptake.com")

    def test_page_load(self):
        print "\n" + str(test_cases(0))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_join_us_button(self):
        print "\n" + str(test_cases(1))
        page = MainPage(self.driver)
        self.driver.implicitly_wait(20)  # seconds
        joinUsPage = page.click_join_us_button()
        self.assertIn("/jobs", joinUsPage.get_url())

    def test_qa_link(self):
        print "\n" + str(test_cases(2))
        self.driver.get("http://www.uptake.com/jobs/")
        page = MainPage(self.driver)
        self.driver.implicitly_wait(20)  # seconds
        clickQaLink = page.click_qa_link()
        self.assertIn("?gh_jid=159311", clickQaLink.get_url())



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)

