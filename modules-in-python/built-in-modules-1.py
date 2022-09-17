import random

# Random from 0 to 1
print(random.random())

# Random int from 0000 to 9999
print(random.randint(0000, 9999))

# Print all methods
print(dir(random))

# Choose between numbers
print(random.choice([1, 2, 3, 4, 5]))

# Shuffle numbers
my_list = [1, 2, 3, 4]
random.shuffle(my_list)
print(my_list)

