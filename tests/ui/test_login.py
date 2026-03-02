from playwright.sync_api import expect

def test_login(login_page):
    login_page.get_by_placeholder("Username").fill("standard_user")
    login_page.get_by_placeholder("Password").fill("secret_sauce")
    login_page.get_by_role("button", name="Login").click()
    expect(login_page).to_have_url("https://www.saucedemo.com/inventory.html")