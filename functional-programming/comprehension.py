# Comprehension
# -> A quick way for us to creat lists or sets or directory in Python instead of looping.

# list
my_list = [char for char in "hello"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num * 2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# set
my_list_1 = {char for char in "hello"}
my_list2_1 = {num for num in range(0, 100)}

# print(my_list_1)
# print(my_list2_1)


# directory
simple_dict = {"a": 1, "b": 2}

my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict2)
