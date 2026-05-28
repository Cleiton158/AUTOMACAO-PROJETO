from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

import time


def test_purchase_flow():

    chrome_options = Options()

    # Deixe comentado para ver o navegador abrindo
    # chrome_options.add_argument("--headless")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://www.saucedemo.com/")
    time.sleep(20)

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")
    time.sleep(20)

    products_page.add_product_to_cart()
    time.sleep(20)

    products_page.open_cart()
    time.sleep(20)

    cart_page.checkout()
    time.sleep(20)

    checkout_page.fill_checkout_information()
    time.sleep(2)

    checkout_page.finish_purchase()
    time.sleep(20)

    assert "checkout-complete" in driver.current_url

    driver.quit()