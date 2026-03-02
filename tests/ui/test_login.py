from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login(login_page):
    login = LoginPage(login_page)
    login.login("standard_user", "secret_sauce")
    expect(login_page).to_have_url("https://www.saucedemo.com/inventory.html")