from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_successful_login(login_page, grab_json_file):
    login = LoginPage(login_page)
    login.login(grab_json_file["users"]["standard_user"]["username"], grab_json_file["users"]["standard_user"]["password"])
    expect(login_page).to_have_url(grab_json_file["urls"]["sauce_inventory"])

def test_unsuccessful_login(login_page, grab_json_file):
    login = LoginPage(login_page)
    login.login(grab_json_file["users"]["incorrect_password_user"]["username"], grab_json_file["users"]["incorrect_password_user"]["password"])
    expect(login.get_error_modal).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_locked_out_login(login_page, grab_json_file):
    login = LoginPage(login_page)
    login.login(grab_json_file["users"]["locked_out_user"]["username"], grab_json_file["users"]["locked_out_user"]["password"])
    expect(login.get_error_modal).to_have_text("Epic sadface: Sorry, this user has been locked out.")