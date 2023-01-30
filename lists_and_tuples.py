# Lists

# Lists == Arrays , its all about capturing and managing data

# here's our first list

shopping_list = ["milk", "eggs", "bread", "fruit", "cheese"]

# print(type(shopping_list)) # <class 'list'>
# print(shopping_list)
# print(shopping_list[0]) # milk, note that it takes away the formatting ([ " ,)
# print(shopping_list[3]) # fruit
# print(shopping_list[-1]) # cheese
# print(shopping_list[-4]) # milk

# rewriting a value in out list
# shopping_list[0] = "sugar"
# print(shopping_list[0])
# print(shopping_list) # milk has been overwritten with the value sugar

# List methods

# add to a list
shopping_list.append("vegetables")
# print(shopping_list)
# print(shopping_list[5])
# print(shopping_list[-1])
# print(len(shopping_list)) # because we added vegetables we have a length of 6

# remove from list

# shopping_list.remove("bread")
# print(len(shopping_list))
# print(shopping_list)

# remove last item of list without specifying it

# shopping_list.pop()
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)

# Mixed data type list
# square brackets for a list
# mixture = [1, 2, 3.5, "one", "two", "three"]
#
# print(mixture)
#
# # List slicing
#
# print(mixture[1:3]) # (2, 3.5)
# print(mixture[1::]) # reverse the order. prints everything after what index u choose
# print(mixture[::2]) # bounces over the amount of indexes specified

#tuples

# exactly the same as lists, except they are immutable (un-editable
# tuples are useful for elements you want to ensure some data stays the same

essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))

# essentials[0] = "beans" , # will not work with tuples


