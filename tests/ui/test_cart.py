from playwright.sync_api import expect
from pages.inventory_page import InventoryPage

def test_add_from_pdp(logged_in_page):
    cart = InventoryPage(logged_in_page)
    cart.pdp_flow()
    expect(cart.remove_button).to_be_visible()
    expect(cart.cart_badge).to_have_text("1")

def test_add_from_inventory_page(logged_in_page):
    cart = InventoryPage(logged_in_page)
    cart.inventory_flow()
    expect(cart.remove_button).to_be_visible()
    expect(cart.cart_badge).to_have_text("1")