import products
import store

"""product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]"""
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]
best_buy = store.Store(product_list)


def start(best_buy):
    menu = int(input("""
   Store menu
   __________
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: 
"""))
    print(menu)
    if menu == 1:
        menu_1(best_buy)
        start(best_buy)
    elif menu == 2:
        print("   __________")
        best_buy.get_total_quantity()
        print("   __________")
        start(best_buy)
    elif menu == 3:
        print("   __________")
        total_cost(processing_order(best_buy))
        print("   __________")
        start(best_buy)
    elif menu == 4:
        print(" ")


def processing_order(best_buy):
    menu_1(best_buy)
    print("When you want to finish order, enter empty text.")
    shopping_cart = []
    list_of_itens = []
    list_of_quant = []
    choosen_product = "A"
    choosen_quantity = "A"
    bb_products = best_buy.get_all_products()
    while choosen_product != "" or choosen_quantity != "":
        choosen_product = input("Which product # do you want?")
        choosen_quantity = input("What amount do you want?")
        print("Product added to list!")
        if choosen_product != "" or choosen_quantity != "":
            if int(choosen_product) < len(bb_products) - 1:
                list_of_itens.append(int(choosen_product))
                list_of_quant.append(int(choosen_quantity))
                for i in range(len(bb_products)):
                    for j in range(len(list_of_itens)):
                        if i + 1 == list_of_itens[j]:
                            shopping_cart.append((bb_products[i].name, bb_products[i].price, list_of_quant[j]))
            else:
                print("Error processing the order")
                start(best_buy)
    return shopping_cart


def total_cost(shopping_cart):
    best_buy.order(shopping_cart)


def menu_1(best_buy):
    all_products = best_buy.get_all_products()
    print("   __________")
    for i in all_products:
        print(i.name)
    print("   __________")


start(best_buy)
