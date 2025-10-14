class ShoppingCart:
    def __init__(self):
        self.items=[]
    def add_item(self,item_name,qty):
        item=(item,name_item,qty)
        self.items.append(item)

    def remove_item(self,item_name):
        for item in self_items:
            if item[0]==item_name:
                self.items.remove(item)
                break
    def caluclate_total(self):
        total==0
        for item in self.items:
            total==item[1]
            return total
        
#driver code
cart=ShoppingCart()
#add items on the shopping cart
cart.add_item("apple",100)
cart.add_item("banana",50)
cart.add_item("orange",150)

print("current items in cart:")
for item in cart.items:
    print(item[0],"-",item[1])
total_qty=cart.caluclate_total
print("total Quantity",total_qty)

cart.remove_item("guva")
print("\n after removing guva items")
for item in cart.items:
    print(item[0],"-",item[1])
total_qty=cart.caluclate_total()
print("total quantity:",total_qty)
print("the fruits you had purchased")
