# Dictionaries

# Dictionaries use key/value pairs

# key = a reference to a particular object
# value = data storage mechanism you want to use, not just the data but how the data is stored

# Create a dictionary

# student_1 = {
#     "name": "Susan",
#     "stream": "DevOps",
#     "completed_lessons": 4,
#     "completed_lesson_names": ["variables", "data_types", "set_up"]
# }

# Access data within a dictionary

# print(student_1["stream"]) # DevOps

# Access a particular element of a list
# print(student_1["completed_lesson_names"][2]) # set_up

# Changing a value in a dictionary

# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])

# Removing items from a dictionary

# student_1["completed_lesson_names"].remove("data_types")
# print(student_1["completed_lesson_names"])
#
# # dictionary methods
#
# # Keys
# print(student_1.keys())
#
# # get the value of a key back without []
# print(student_1.get("name"))
#
# # get the value of a dictionary
#
# print(student_1.values())

# outputs array of tuples(unchangeable) with key value pairs in dictionary
# print(student_1.items())

my_dict = {
    "name": "Ahimba",
    "job_title": "Junior_DevOps",
    "experience_in_years": 0,
    "certifications": ["ISTQB", "Certificate of higher education"]
}

print(my_dict)