class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop Name: {self.shop_name}")
        print(f"Store Type: {self.store_type}")

    def open_shop(self):
        print(f"The {self.shop_name} online shop is now open!")

    def set_number_of_units(self, number_of_units):
        self.number_of_units = number_of_units

    def increment_number_of_units(self, increment):
        self.number_of_units += increment


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products=None):
        super().__init__(shop_name, store_type)
        if discount_products is None:
            discount_products = []
        self.discount_products = discount_products

    def get_discount_products(self):
        print("Discount Products:")
        for product in self.discount_products:
            print(product)
