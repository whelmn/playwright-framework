class LoginPage:
    def __init__(self, page):
        self.page = page

    @property
    def username_input(self):
        return self.page.get_by_placeholder("Username")

    @property
    def password_input(self):
        return self.page.get_by_placeholder("Password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()