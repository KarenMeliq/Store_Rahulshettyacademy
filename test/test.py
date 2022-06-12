import pytest
from selenium.webdriver.common.by import By

from GetElements.web_elements import WebElements
from base.browser import RahulShettyAcademy
from locators.locators import Locators


@pytest.mark.usefixtures('open_browser')
class Test_rahul_shetty_academy(RahulShettyAcademy):

    def test_rahul_title(self):
        result = WebElements.get_title_url(self)
        expected_result = ("GreenKart - veg and fruits kart","https://rahulshettyacademy.com/seleniumPractise/#/")
        assert expected_result == result


    def test_mango_price_quantity(self):
        mango_quantity_price = WebElements.add_mango(self)
        expected_result = ("1", "75")
        assert mango_quantity_price == expected_result


    def test_mango_on_overlay(self):
        result = WebElements.mango_in_cart(self)
        expected_result = "/images/mango.jpg"
        assert expected_result in result

    def test_card_page(self):
        result = WebElements.proceed_checkout(self)
        oneMango = "1"
        assert result.is_displayed()

    def test_proceed_checkout_one_item(self):
        result = WebElements.proceed_checkout_one_item(self)
        oneMango = "1"
        assert oneMango in result

    def test_terms_condition(self):
        WebElements.place_order(self)
        assert self.driver.find_element(By.XPATH, Locators.terms_condition).is_selected()

    def test_proceed(self):
        result = WebElements.proceed_to_success_page(self)
        success_text ="Thank you, your order has been placed successfully"
        assert success_text in result