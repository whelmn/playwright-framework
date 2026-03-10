class BasePage:
    def __init__(self, page):
        self.page = page

    @property
    def cart_badge(self):
        return self.page.get_by_test_id("shopping-cart-badge")

    @property
    def cart_link(self):
        return self.page.get_by_test_id("shopping-cart-link")