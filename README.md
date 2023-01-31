# tech201_collections
tech201_collections

# Lists

 Lists == Arrays , its all about capturing and managing data

 here's our first list

 shopping_list = ["milk", "eggs", "bread", "fruit", "cheese"]

 print(type(shopping_list)) # <class 'list'>  
 print(shopping_list)
 print(shopping_list[0]) # milk, note that it takes away the formatting ([ " ,)  
 print(shopping_list[3]) # fruit  
 print(shopping_list[-1]) # cheese  
 print(shopping_list[-4]) # milk  

# Rewriting a Value in our list
shopping_list[0] = "sugar"  
print(shopping_list[0])  
print(shopping_list) # milk has been overwritten with the value sugar

# List Methods

add to a list
 shopping_list.append("vegetables")  
print(shopping_list)    
print(shopping_list[-1])  
print(len(shopping_list)) # because we added vegetables we have a length of 6

# Remove from List

shopping_list.remove("bread")  
print(len(shopping_list))  
print(shopping_list)  

remove last item of list without specifying it

shopping_list.pop()  
print(shopping_list)  
shopping_list.pop()   
print(shopping_list)  
shopping_list.pop()  
print(shopping_list)  
shopping_list.pop()  
print(shopping_list)  

Mixed data type list
square brackets for a list
mixture = [1, 2, 3.5, "one", "two", "three"]

print(mixture)

# List slicing

print(mixture[1:3]) # (2, 3.5)  
print(mixture[1::]) # reverse the order. prints everything after what index u choose  
print(mixture[::2]) # bounces over the amount of indexes specified

# Tuples

exactly the same as lists, except they are immutable (un-editable
tuples are useful for elements you want to ensure some data stays the same

essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))

essentials[0] = "beans" , # will not work with tuples

# Dictionaries

##### Dictionaries use key/value pairs

key = a reference to a particular object  
value = data storage mechanism you want to use, not just the data but how the data is stored

### Create a dictionary  

student_1 = {  
     "name": "Susan",  
     "stream": "DevOps",  
     "completed_lessons": 4,  
     "completed_lesson_names": ["variables", "data_types", "set_up"]  
 }

###  Access data within a dictionary

print(student_1["stream"]) # DevOps  

Access a particular element of a list  
print(student_1["completed_lesson_names"][2]) # set_up

### Changing a value in a dictionary

student_1["completed_lessons"] = 3  
print(student_1["completed_lessons"])

### Removing items from a dictionary

student_1["completed_lesson_names"].remove("data_types")  
print(student_1["completed_lesson_names"])

### dictionary methods

### Keys
print(student_1.keys())

### get the value of a key back without [ ]
print(student_1.get("name"))

### get the values of a dictionary

print(student_1.values()) # this will print the values in the key:value pair  

### the following will give an output of an array of tuples(unchangeable) with key value pairs in dictionary
 
print(student_1.items())

my_dict = {  
     "name": "Ahimba",  
     "age": "30",  
     "job_title": "Junior_DevOps",  
     "education": "mathematics",  
     "university": "London Metropolitan",  
     "last_job_title": "Gaming Supervisor",  
     "work_experience_in_years": 10,  
     "certifications": ["ISTQB", "Certificate of higher education"]  
 }  

 print(my_dict)

# Sets and Frozen sets

##### Lists and sets are very similar

##### Sets are unordered

### create a set

car_parts = {"wheels", "exhaust", "doors"}  
print(car_parts)  
print(car_parts)  

### remove things from a set

car_parts.discard("doors")  
print(car_parts)  

### add things to a set
car_parts.add("windows")  
print(car_parts)  

### Frozen sets

#### frozen sets are immutable versions of a set. still unordered and un- indexed
x = frozenset([1, 2, 3, 4, "five"])  
print(x)