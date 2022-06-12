import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class RahulShettyAcademy:

    URL = "https://rahulshettyacademy.com/seleniumPractise/#/"
    s = Service('..\\chromedriver.exe')

    @pytest.fixture()
    def open_browser(self):
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield self.driver
        self.driver.quit()


