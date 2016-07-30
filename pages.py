from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
import time



# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocatars.LOGO) else False

        
    def click_join_us_button(self):
        self.driver.find_element(*MainPageLocatars.JOIN_US).click()
        time.sleep(2)
        return homePage(self.driver)

    def click_qa_link(self):
       frame = self.driver.find_element_by_xpath('//*[@id="grnhse_iframe"]')
       self.driver.switch_to.frame(frame)
       self.driver.find_element(*MainPageLocatars.QA_LINK).click()
       time.sleep(2)
       #self.driver.implicitly_wait(30)  # seconds
       link = self.driver.current_url
       return link

class homePage(Page):
    pass
