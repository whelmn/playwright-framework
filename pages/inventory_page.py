from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def find_product(self):
        return self.page.get_by_test_id("item-4-title-link")

    @property
    def add_from_product_page(self):
        return self.page.get_by_role("button", name="Add to cart")

    @property
    def add_from_inventory_page(self):
        return self.page.get_by_test_id("add-to-cart-sauce-labs-backpack")

    @property
    def remove_button(self):
        return self.page.get_by_role("button", name="Remove")

    @property
    def get_inventory_dropdown(self):
        return self.page.get_by_test_id("product-sort-container")

    @property
    def get_first_products(self):
        return self.page.get_by_test_id("inventory-item-name").first

    @property
    def get_first_prices(self):
        return self.page.get_by_test_id("inventory-item-price").first

    def pdp_flow(self):
        self.find_product.click()
        self.add_from_product_page.click()

    def inventory_flow(self):
        self.add_from_inventory_page.click()

    def sort_by(self, option):
        self.get_inventory_dropdown.select_option(option)

