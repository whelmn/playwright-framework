from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def checkout_button(self):
        return self.page.get_by_role("button", name="Checkout")

    @property
    def continue_button(self):
        return self.page.get_by_role("button", name="Continue")

    @property
    def finish_button(self):
        return self.page.get_by_role("button", name="Finish")

    @property
    def first_name_input(self):
        return self.page.get_by_placeholder("First Name")

    @property
    def last_name_input(self):
        return self.page.get_by_placeholder("Last Name")

    @property
    def zip_code_input(self):
        return self.page.get_by_placeholder("Zip/Postal Code")

    @property
    def get_checkout_success(self):
        return self.page.get_by_test_id("checkout-complete-container")

    def click_cart(self):
        self.cart_link.click()

    def click_checkout(self):
        self.checkout_button.click()

    def checkout_information(self, first_name="Test", last_name="User", zip_code="91722"):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()




