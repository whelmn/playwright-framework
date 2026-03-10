from playwright.sync_api import Page, Playwright
import pytest
from pages.login_page import LoginPage
import json
from pathlib import Path



@pytest.fixture
def login_page(page: Page, grab_json_file):
    page.goto(grab_json_file["urls"]["sauce_login"])
    yield page

@pytest.fixture
def logged_in_page(login_page, grab_json_file):
    login = LoginPage(login_page)
    login.login(grab_json_file["users"]["standard_user"]["username"], grab_json_file["users"]["standard_user"]["password"])
    yield login_page

@pytest.fixture(scope="session", autouse=True)
def sauce_test_id(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(scope="session")
def grab_json_file():
    path = Path(__file__).parent.parent.parent / "test-data" / "users.json"
    with path.open() as f:
        return json.load(f)