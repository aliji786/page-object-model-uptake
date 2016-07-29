from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
import users
from selenium.webdriver.support.ui import WebDriverWait


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocatars.LOGO) else False

        
    def click_join_us_button(self):
        self.driver.find_element(*MainPageLocatars.JOIN_US).click()
        return homePage(self.driver)

    def click_qa_link(self):
        self.driver.find_element(*MainPageLocatars.QA_LINK).click()
        return homePage(self.driver)

    
class homePage(Page):
    pass
