# waiter program
# creating a menu

starters = ["Chicken Bites", "Halloumi Sticks", "Wedges", "King Prawns"]

mains = ["whole Chicken Meal", "Lobster Meal", "Prawn Tempura Meal", "Sirloin Steak Meal", "Wagyu Burger Meal"]

desserts = ["Strawberry Ice Cream", "Carrot Cake", "Chocolate Fudge with Cream"]

drinks = ["Water", "Wine", "Soft Drinks Bottomless"]

print("Please have a look at our Menu")
print("*Starters")
print(starters[0])
print(starters[1])
print(starters[2])
print(starters[3])
print("*Mains")
print(mains[0])
print(mains[1])
print(mains[2])
print(mains[3])
print(mains[4])
print("*Desserts")
print(desserts[0])
print(desserts[1])
print(desserts[2])
print("*Drinks")
print(drinks[0])
print(drinks[1])
print(drinks[2])

customer_order = ["customer order"]
print(customer_order)

print("What would you like for your starter?")
starter = input()
customer_order.append(starter)
print(customer_order)


print("What would you like for your main?")
main = input()
customer_order.append(main)
print(customer_order)

print("What would you like for your dessert?")
dessert = input()
customer_order.append(dessert)
print(customer_order)

print("What would you like for your drink?")
drink = input()
customer_order.append(drink)
print(customer_order)




print("For starter you will have " + starter + ", For main you will have " + main + ", For dessert you will have " + dessert + ", For your drink you will have " + drink)