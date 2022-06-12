
class Locators:
    add_mango_btn = '//*[@id="root"]/div/div[1]/div/div[18]/div[3]/button'
    card_btn = '//*[@id="root"]/div/header/div/div[3]/a[4]/img'
    mango_one_kg = 'div.cart-info tr:nth-child(1) > td:nth-child(3) > strong'
    mango_price ="(//p[@class='amount'][normalize-space()='75'])[1]"
    mango_img = 'img[class = "product-image"][src="./images/mango.jpg"]'
    proceed_checkout = "#root > div > header > div > div.cart > div.cart-preview.active > div.action-block > button"
    prod_table = ".products-wrapper"
    one_item = "(//p[@class='quantity'])[1]"
    place_order = "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > button:nth-child(14)"
    terms_condition = "(//input[@type='checkbox'])[1]"
    proceed = "//button[normalize-space()='Proceed']"
    success_message = "//*[contains(text(), 'Thank you, your order has been placed successfully')]"
