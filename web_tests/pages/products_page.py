from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")

    cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):

        self.driver.find_element(*self.add_to_cart_button).click()

    def open_cart(self):

        self.driver.find_element(*self.cart_button).click()