from playwright.sync_api import expect
from pages.inventory_page import InventoryPage


def test_sort_by_az(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("az")
    expect(inventory.get_first_products).to_have_text("Sauce Labs Backpack")

def test_sort_by_za(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("za")
    expect(inventory.get_first_products).to_have_text("Test.allTheThings() T-Shirt (Red)")

def test_sort_by_lohi(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("lohi")
    expect(inventory.get_first_prices).to_have_text("$7.99")

def test_sort_by_hilo(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("hilo")
    expect(inventory.get_first_prices).to_have_text("$49.99")