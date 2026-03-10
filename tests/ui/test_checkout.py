from playwright.sync_api import expect
from pages.cart_page import CartPage

def test_checkout(add_to_cart):
    cart = CartPage(add_to_cart)
    cart.click_cart()
    cart.click_checkout()
    cart.checkout_information()
    cart.finish_checkout()
    expect(cart.get_checkout_success).to_contain_text("Thank you for your order!")