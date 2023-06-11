import products

class Store():
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.product = product
        self.list_of_products.append(self.product)
        for x in self.list_of_products:
            print(x.name)
        return self.list_of_products

    def remove_product(self, product):
        self.list_of_products.remove(self.product)
        return self.list_of_products

    def get_total_quantity(self):
        total_amount = 0
        for i in self.list_of_products:
            total_amount = total_amount + i.quantity
        print(f"Total of {total_amount} itens in store")
        return total_amount

    def get_all_products(self):
        active_products = []
        for i in self.list_of_products:
            if i.active is True:
                active_products.append(i)
        return active_products

    def order(self, shopping_list):
        total = 0
        for i in shopping_list:
            total = total + i[1] * i[2]
        print(f"Order made! Total payment: {total}")
        return total
