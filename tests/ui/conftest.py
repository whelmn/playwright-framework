from playwright.sync_api import Page
import pytest

@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    yield page