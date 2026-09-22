#menu of resturant
menu = {
    "Pizza": 99,
    "Burger": 49,
    "coffee": 30,
    "pasta": 80,
    "salad": 50
}

#Greeting the customer
print("Welcome to our superrrrr~ restaurant!")
print("Here is our menu:")
print("Pizza  : Rs99\nBurger : Rs49\ncoffee : Rs30\npasta  : Rs80 \nsalad  : Rs50 ")
#calculating the total bill
order_total = 0
item_1 = input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: Rs{order_total}")
else:
    print(f"oh noo we are sorry the item {item_1} you asked is not availabel for you i am sorry")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item_2 = input("Enter the second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order. Current total: Rs{order_total}")
    else:
        print(f"oh noo we are sorry the item {item_2} you asked is not availabel for you i am sorry")

print(f"now you have to pay for the food that you oder is {order_total} Rs")

