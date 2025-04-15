import json
import logging
import os

import pytest
from dotenv import load_dotenv

import src.utils.logger as logger
from src.data.user import User
from src.pages.checkout_page import CheckoutPage
from src.pages.header_page import HeaderPage
from src.pages.product_page import ProductPage
from src.pages.shopping_cart_page import ShoppingCartPage

load_dotenv()
base_url = os.getenv('BASE_URL')
email_address = os.getenv('EMAIL_ADDRESS')
password = os.getenv('PASSWORD')


@pytest.fixture(scope="module")
def product_data():
    with open('src/data/product.json', 'r') as file:
        return json.load(file)


@pytest.fixture(scope="module")
def user_data():
    with open('src/data/user.json', 'r') as file:
        return json.load(file)


@pytest.mark.order(1)
def test_add_product_to_cart_and_checkout_as_guest(page, product_data, user_data):
    log = logger.custom_logger(logging.DEBUG)
    log.info("Starting product search test")
    header = HeaderPage(page)
    product_page = ProductPage(page)
    shopping_cart = ShoppingCartPage(page)
    checkout_page = CheckoutPage(page)

    user = User.from_dict(user_data)

    log.info("Navigating to home page")
    header.navigate_to(base_url)
    log.info("Searching for product and assert details")
    product_page.search_and_assert_product_details(product_data[1])
    log.info("Adding product to cart and verifying")
    product_page.add_product_to_cart_and_verify_product_added_to_cart(product_data[1])
    log.info("Navigating to shopping cart")
    product_page.navigate_to_shopping_cart()
    log.info("Asserting product details on shopping cart")
    shopping_cart.assert_product_details_on_shopping_cart(product_data[1])
    log.info("Continuing to checkout")
    shopping_cart.continue_to_checkout()
    log.info("Checking out as guest")
    checkout_page.checkout_as_a_guest(user)
