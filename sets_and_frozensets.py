# Sets and Frozen sets

# Lists and sets are very similar

# Sets are unordered

# create a set
#
car_parts = {"wheels", "exhaust", "doors"}
# print(car_parts)
# print(car_parts)

# remove things from a set

car_parts.discard("doors")
# print(car_parts)

# add things to a set
car_parts.add("windows")
print(car_parts)

# Frozen sets

# frozen sets are immutable versions of a set. still unordered and un- indexed
x = frozenset([1, 2, 3, 4, "five"])
print(x)