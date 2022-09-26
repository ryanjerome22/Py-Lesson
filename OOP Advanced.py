class Item:
    def __init__(self, name):
        print(f"An intance created: {name} " )
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item("Phone")
item1.name = "Phone"
item1.price = 25
item1.number= 5

item2 = Item("Phone")
item2.name = "Laptop"
item2.price = 23
item2.number= 4