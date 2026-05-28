from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "first-name")

    last_name = (By.ID, "last-name")

    postal_code = (By.ID, "postal-code")

    continue_button = (By.ID, "continue")

    finish_button = (By.ID, "finish")

    def fill_checkout_information(self):

        self.driver.find_element(*self.first_name).send_keys("Cleiton")

        self.driver.find_element(*self.last_name).send_keys("Silva")

        self.driver.find_element(*self.postal_code).send_keys("64000")

        self.driver.find_element(*self.continue_button).click()

    def finish_purchase(self):

        self.driver.find_element(*self.finish_button).click()