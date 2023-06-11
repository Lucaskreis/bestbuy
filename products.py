class Product:
    def __init__(self, name, price, quantity):
        self.active = True
        self.price = price
        self.quantity = quantity
        try:
            if name != "":
                self.name = name
        except NoneType:
            print("You should write a valid product name")

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_quantity(self):
        print(self.quantity)
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = self.quantity + new_quantity
        if self.quantity == 0:
            Product.deactivate(self)
        else:
            Product.activate(self)
        return Product.get_quantity(self)

    def show(self):
        print(f"{self.name}, Price:{self.price}, Quantity:{self.quantity}, {self.active}")


class NonStockedProduct(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.active = True
        self.quantity = None


    def is_active(self):
        super().is_active()


    def activate(self):
        super().active()


    def deactivate(self):
        super().deactivate()


    def show(self):
        print(f"{self.name}, Price:{self.price}, {self.active}")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def is_active(self):
        super().is_active()

    def activate(self):
        super().active()

    def deactivate(self):
        super().deactivate()


    def get_quantity(self):
        super().get_quantity()


    def set_quantity(self, quantity, maximum):
        super().set_quantity(quantity)
        if self.quantity > self.maximum:
            print("Quantity exceeds maximum")
