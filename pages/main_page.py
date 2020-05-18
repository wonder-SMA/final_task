from .base_page import BasePage
from selenium.webdriver.common.by import By
import pytest, time

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        time.sleep(5)