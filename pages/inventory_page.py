class InventoryPage:
    def __init__(self, page):
        self.page = page

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
    def cart_badge(self):
        return self.page.get_by_test_id("shopping-cart-badge")

    def pdp_flow(self):
        self.find_product.click()
        self.add_from_product_page.click()

    def inventory_flow(self):
        self.add_from_inventory_page.click()

