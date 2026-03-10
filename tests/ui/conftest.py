from playwright.sync_api import Page, Playwright
import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    yield page

@pytest.fixture
def logged_in_page(login_page):
    login = LoginPage(login_page)
    login.login("standard_user", "secret_sauce")
    yield login_page

@pytest.fixture(scope="session", autouse=True)
def sauce_test_id(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")