menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

print("Welcome to python restaurant")
print("pizza: Rs40\npasta: Rs50\n burger: Rs60\nsalad: Rs70\ncoffee: Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialable yet")    

another_order == input("Do you want to add another item? (yes/no)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2 ]
        print(f"Item {item_2} has been added to  order")

    else:
        print(f"Ordered item {item_2} is not avaialable t")    

print(f"The total amount of items is {order_total}")        