from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_button = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def add_product_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        ).click()