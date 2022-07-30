from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]


def capitalize_name(name: str):
    return name.upper()


print(list(map(capitalize_name, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()

print(list(zip(my_strings, my_numbers)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_scores(item):
    return (item * 50) / 100 > 50


print(list(filter(filter_scores, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores).
# What is the total?


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, [*my_numbers, *scores], 0))
