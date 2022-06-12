import pytest
from selenium.webdriver.common.by import By

from base.browser import RahulShettyAcademy
from locators.locators import Locators

@pytest.mark.usefixtures('open_browser')
class WebElements(RahulShettyAcademy):

    def __init__(self, driver):
        self.driver = driver

    def get_title_url(self):
        driver = self.driver
        rahull_title = driver.title
        rahull_url = driver.current_url
        return rahull_title, rahull_url


    def add_mango(self):
        self.driver.find_element(By.XPATH, Locators.add_mango_btn).click()
        self.driver.find_element(By.XPATH, Locators.card_btn).click()
        mango_quantity = self.driver.find_element(By.CSS_SELECTOR, Locators.mango_one_kg).text
        mango_price_str = self.driver.find_element(By.XPATH, Locators.mango_price).text
        return mango_quantity, mango_price_str


    def mango_in_cart(self):
        self.driver.find_element(By.XPATH, Locators.add_mango_btn).click()
        self.driver.find_element(By.XPATH, Locators.card_btn).click()
        mango_shown = self.driver.find_element(By.CSS_SELECTOR, Locators.mango_img).get_attribute("src")
        return mango_shown

    def proceed_checkout(self):
        driver = self.driver
        self.driver.find_element(By.XPATH, Locators.add_mango_btn).click()
        self.driver.find_element(By.XPATH, Locators.card_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.proceed_checkout).click()
        cart_page = driver.find_element(By.CSS_SELECTOR, Locators.prod_table)
        item_mango= driver.find_element(By.XPATH, Locators.one_item).text
        return cart_page

    def proceed_checkout_one_item(self):
        driver = self.driver
        self.driver.find_element(By.XPATH, Locators.add_mango_btn).click()
        self.driver.find_element(By.XPATH, Locators.card_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.proceed_checkout).click()
        item_mango= driver.find_element(By.XPATH, Locators.one_item).text
        return item_mango


    def place_order(self):
        self.driver.find_element(By.XPATH, Locators.add_mango_btn).click()
        self.driver.find_element(By.XPATH, Locators.card_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.proceed_checkout).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.place_order).click()
        self.driver.find_element(By.XPATH, Locators.terms_condition).click()

    def proceed_to_success_page(self):
        WebElements.place_order(self)
        self.driver.find_element(By.XPATH, Locators.proceed).click()
        succ_message = self.driver.find_element(By.XPATH, Locators.success_message).text
        #status = succ_message.is_displayed()
        return succ_message
