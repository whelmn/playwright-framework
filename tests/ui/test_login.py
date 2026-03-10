from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login(login_page, grab_json_file):
    login = LoginPage(login_page)
    login.login(grab_json_file["users"]["standard_user"]["username"], grab_json_file["users"]["standard_user"]["password"])
    expect(login_page).to_have_url(grab_json_file["urls"]["sauce_inventory"])